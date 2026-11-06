// Language switcher (Indonesian default). Text for each language sits in elements with data-l="id|en|ja".
(function () {
  var LANGS = ["id", "en", "ja"];
  function getSaved() { try { return localStorage.getItem("dri-lang"); } catch (e) { return null; } }
  function save(l) { try { localStorage.setItem("dri-lang", l); } catch (e) {} }
  function apply(l) {
    if (LANGS.indexOf(l) < 0) l = "id";
    document.body.classList.remove("lang-id", "lang-en", "lang-ja");
    document.body.classList.add("lang-" + l);
    document.documentElement.lang = l;
    document.querySelectorAll(".langs button").forEach(function (b) {
      b.setAttribute("aria-pressed", b.dataset.set === l ? "true" : "false");
    });
  }
  var q = new URLSearchParams(location.search).get("lang");
  apply(q || getSaved() || "id");
  document.addEventListener("click", function (e) {
    var b = e.target.closest(".langs button");
    if (!b) return;
    apply(b.dataset.set); save(b.dataset.set);
  });
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
