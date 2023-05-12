var theme = document.getElementById("theme");
var theme_text = document.getElementById("theme_text");


var switch_theme = () =>{
    if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
      document.documentElement.setAttribute('data-bs-theme','light')
      theme_text.innerHTML = "Light";
    }
    else {
      document.documentElement.setAttribute('data-bs-theme','dark')
      theme_text.innerHTML = "Dark";
    }
  }

theme.addEventListener("change", switch_theme);