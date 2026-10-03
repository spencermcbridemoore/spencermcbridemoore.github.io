/* Links each piece of slide text to its place on the slide image: hovering either one highlights both.
   Written without line comments and with explicit semicolons because the production build joins lines. */
(function () {
  "use strict";
  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };
  each(document.querySelectorAll(".sl"), function (block) {
    var stage = block.querySelector(".sl-fig > p");
    var text = block.querySelector(".sl-txt");
    var head = block.previousElementSibling;
    if (!head || head.tagName !== "H2" || !head.hasAttribute("data-k")) { head = null; }
    each(block.querySelectorAll("table[data-keys]"), function (table) {
      var keys = table.getAttribute("data-keys").split(" ");
      each(table.querySelectorAll("th, td"), function (cell, i) {
        if (keys[i] && keys[i] !== "-") { cell.setAttribute("data-k", keys[i]); }
      });
    });
    var boxes = [];
    each(block.querySelectorAll(".sl-r"), function (r) {
      var l = parseFloat(r.style.left), t = parseFloat(r.style.top), w = parseFloat(r.style.width), h = parseFloat(r.style.height);
      boxes.push({ k: r.getAttribute("data-k"), l: l, t: t, r: l + w, b: t + h, a: w * h });
    });
    var current = null;
    var mark = function (key, on) {
      each(block.querySelectorAll('[data-k="' + key + '"]'), function (n) { n.classList.toggle("on", on); });
      if (head && head.getAttribute("data-k") === key) { head.classList.toggle("on", on); }
    };
    var show = function (key) {
      if (key === current) { return; }
      if (current !== null) { mark(current, false); }
      current = key;
      if (key !== null) { mark(key, true); }
    };
    var keyOf = function (target) {
      var el = target && target.closest ? target.closest("[data-k]") : null;
      return el && !el.classList.contains("sl-r") ? el.getAttribute("data-k") : null;
    };
    if (text) {
      text.addEventListener("mouseover", function (e) { show(keyOf(e.target)); });
      text.addEventListener("mouseleave", function () { show(null); });
    }
    if (head) {
      head.addEventListener("mouseenter", function () { show(head.getAttribute("data-k")); });
      head.addEventListener("mouseleave", function () { show(null); });
    }
    if (stage) {
      stage.addEventListener("mousemove", function (e) {
        var rect = stage.getBoundingClientRect();
        if (!rect.width || !rect.height) { return; }
        var x = (e.clientX - rect.left) / rect.width * 100;
        var y = (e.clientY - rect.top) / rect.height * 100;
        var best = null;
        for (var i = 0; i < boxes.length; i += 1) {
          var bx = boxes[i];
          if (x >= bx.l && x <= bx.r && y >= bx.t && y <= bx.b && (best === null || bx.a < best.a)) { best = bx; }
        }
        show(best ? best.k : null);
      });
      stage.addEventListener("mouseleave", function () { show(null); });
    }
  });
})();
