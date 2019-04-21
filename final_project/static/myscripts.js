
src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">


// Menu Burger Animation adopted from FreeCodeCamp: https://www.w3schools.com/howto/howto_css_menu_icon.asp
function menuAnimation(x) {
    x.classList.toggle("change");
}

// Menu Overlay 
function togglenav(x){
    x.classList.toggle("open");
}

// ColorChange of the Navbar
function colorChange(x){
    x.classList.toggle("open");
}

// Hide and Show Projects
function togglediv(t){
    var x = document.getElementById(t);
    if (x.style.display === "none"){
        x.style.display = "block";

    } else {
        x.style.display = "none";
    }
}

// Mouse Wheel Function from https://codepen.io/chriscoyier/pen/WmyKWO
// $(document).ready(function() {
//     $('mousescroll').mousewheel(function(e, delta) {
//     this.scrollLeft -= (delta);
//     e.preventDefault();
//     });
// });

// document.getElementById("mousescroll").onscroll = function() {mouseWheel()};

// function mouseWheel() {
//   document.getElementById("demo").innerHTML = "You scrolled in div.";
// }

// document.getElementById("mousescroll").addEventListener("wheel", myFunction);

// function myFunction() {
//   this.style.fontSize = "35px";