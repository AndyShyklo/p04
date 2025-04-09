// Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
// JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
// SoftDev
// p04
// 2025-03-28

document.addEventListener("DOMContentLoaded", function () {

  const nav = document.getElementById("nav")
  nav.innerHTML = `
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">🔥🔥😵‍💫</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="/map">Map</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/profile">👤</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/settings">⚙</a>
        </li>
	<li class="nav-item">
	  <a class="nav-link" href="/login">Login</a>
	</li>        
        <li class="nav-item">
	  <a class="nav-link" href="/register">Register</a>
	</li>
    </div>
  </nav>`

});
