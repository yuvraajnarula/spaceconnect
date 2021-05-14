var preload = document.createElement("div");
    preload.className = "preloader";
    preload.innerHTML =
      '<div id="preloader"><div id="loader"></div></div>';
    document.body.appendChild(preload);
    window.addEventListener("load", function() {
      preload.className += " fade";
      setTimeout(function() {
        preload.style.display = "none";
      }, 1500);
    });
