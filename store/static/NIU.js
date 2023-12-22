//this script is not in use bcs of bug with item image being "in front of" nav bar

window.onscroll = function() {myFunction()};

var navbar = document.getElementById("header");

var sticky = navbar.offsetTop;

function myFunction() {
  if (window.scrollY >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}