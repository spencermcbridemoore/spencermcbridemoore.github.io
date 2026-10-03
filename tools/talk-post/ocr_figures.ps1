# Recognise the text in every fig*.png in a folder with Windows' built-in OCR and write, next to
# each image, a .tsv of words: line number, text, x, y, width, height (pixels, tab-separated).
# Called by make_figure_regions.py. Windows PowerShell 5.1; needs the en-US OCR language.
param([Parameter(Mandatory = $true)][string]$Dir)

Add-Type -AssemblyName System.Runtime.WindowsRuntime
[void][Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
[void][Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime]
[void][Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics, ContentType = WindowsRuntime]
[void][Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics, ContentType = WindowsRuntime]
[void][Windows.Storage.Streams.IRandomAccessStream, Windows.Storage.Streams, ContentType = WindowsRuntime]
[void][Windows.Globalization.Language, Windows.Globalization, ContentType = WindowsRuntime]

# WinRT calls are asynchronous; this waits for one and returns its result.
$asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
  })[0]
function Await($operation, [Type]$resultType) {
  $task = $asTask.MakeGenericMethod($resultType).Invoke($null, @($operation))
  [void]$task.Wait(120000)
  $task.Result
}

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new('en-US'))
if ($null -eq $engine) { $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages() }
if ($null -eq $engine) { throw 'No OCR language is installed.' }

$tab = [char]9
$inv = [Globalization.CultureInfo]::InvariantCulture
foreach ($image in Get-ChildItem -LiteralPath $Dir -Filter 'fig*.png') {
  $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($image.FullName)) ([Windows.Storage.StorageFile])
  $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
  $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
  $bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
  $result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
  $rows = New-Object System.Collections.Generic.List[string]
  $lineNumber = 0
  foreach ($line in $result.Lines) {
    foreach ($word in $line.Words) {
      $r = $word.BoundingRect
      $rows.Add((@($lineNumber, $word.Text, $r.X.ToString('F1', $inv), $r.Y.ToString('F1', $inv), $r.Width.ToString('F1', $inv), $r.Height.ToString('F1', $inv)) -join $tab))
    }
    $lineNumber++
  }
  $out = [IO.Path]::ChangeExtension($image.FullName, '.tsv')
  [IO.File]::WriteAllLines($out, $rows, (New-Object System.Text.UTF8Encoding($false)))
  '{0}: {1} words on {2} lines' -f $image.Name, $rows.Count, $lineNumber
  $stream.Dispose()
}
