/*! TeachAny 分页导航补丁（elementary 分页课件）
 * 用于替代已从 CDN 下架的 teachany-paged.js。
 * 自动扫描 .slide-page，注入底部导航条（上一页/页点/下一页 + 页码），
 * 支持点击页点跳转、键盘方向键/空格翻页、滚动时同步当前页。
 */
(function () {
  "use strict";
  if (window.__TeachAnyPagedPatchInit) return;
  window.__TeachAnyPagedPatchInit = true;

  function init() {
    var slides = Array.prototype.slice.call(document.querySelectorAll(".slide-page"));
    if (!slides.length) return;
    // 确保每个 slide 有 id
    slides.forEach(function (s, i) { if (!s.id) s.id = "slide-" + (i + 1); });
    var total = slides.length;
    var current = 1;

    // 注入导航条
    var bar = document.createElement("div");
    bar.className = "ta-playbar";
    bar.innerHTML =
      '<button type="button" class="ta-secondary" data-nav="prev">‹ 上一页</button>' +
      '<div class="ta-dots"></div>' +
      '<span class="ta-page-num">1 / ' + total + '</span>' +
      '<button type="button" data-nav="next">下一页 ›</button>';
    document.body.appendChild(bar);

    var dotsBox = bar.querySelector(".ta-dots");
    var numEl = bar.querySelector(".ta-page-num");
    var prevBtn = bar.querySelector('[data-nav="prev"]');
    var nextBtn = bar.querySelector('[data-nav="next"]');

    for (var i = 1; i <= total; i++) {
      (function (n) {
        var d = document.createElement("span");
        d.className = "ta-dot" + (n === 1 ? " active" : "");
        d.addEventListener("click", function () { goTo(n); });
        dotsBox.appendChild(d);
      })(i);
    }
    var dots = dotsBox.querySelectorAll(".ta-dot");

    function render() {
      dots.forEach(function (d, idx) { d.classList.toggle("active", idx + 1 === current); });
      numEl.textContent = current + " / " + total;
      prevBtn.disabled = current <= 1;
      nextBtn.disabled = current >= total;
    }
    function goTo(n) {
      if (n < 1 || n > total) return;
      current = n;
      slides[n - 1].scrollIntoView({ behavior: "smooth", block: "start" });
      render();
    }
    prevBtn.addEventListener("click", function () { goTo(current - 1); });
    nextBtn.addEventListener("click", function () { goTo(current + 1); });

    document.addEventListener("keydown", function (e) {
      var tag = (e.target && e.target.tagName) || "";
      if (tag === "INPUT" || tag === "TEXTAREA") return;
      if (e.key === "ArrowDown" || e.key === "ArrowRight" || e.key === " ") { e.preventDefault(); goTo(current + 1); }
      if (e.key === "ArrowUp" || e.key === "ArrowLeft") { e.preventDefault(); goTo(current - 1); }
    });

    // 滚动时同步当前页（取视口中最靠近顶部的 slide）
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        var best = 1, bestDist = Infinity;
        slides.forEach(function (s, idx) {
          var r = s.getBoundingClientRect();
          var dist = Math.abs(r.top);
          if (dist < bestDist) { bestDist = dist; best = idx + 1; }
        });
        if (best !== current) { current = best; render(); }
        ticking = false;
      });
    }, { passive: true });

    render();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
