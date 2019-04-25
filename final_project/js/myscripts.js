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
function togglediv(x){
    var x = document.getElementById(x);
    if (x.style.display === "none"){
        x.style.display = "block";

    } else {
        x.style.display = "none";
    }
}

// Mousescroll /slide left function
$(function() {
    $('.capturescroll').mousewheel(function(event, delta) { //mousewhweel is an eventhandler //event is the default event (scrolling up/down// delta is the mouse up or down scroll
        const speed = 1
        const mousescroll = $('#horizontalscroll')
        const scrollable = mousescroll[0] //jquery array
        const scrollTopPosition = mousescroll.offset().top //position of horizontal scroll component
        const scrollTopPadding = Math.abs(delta) * speed //gives padding for better usability //buffer
        const scrollTop = $('body')[0].scrollTop - delta //checks where the user is in the body
        const width = scrollable.scrollWidth - mousescroll.width() - speed //width of combonanant minnus visible width - buffer
        if(scrollable.scrollLeft <= width && delta < 0 && scrollTop >= scrollTopPosition - scrollTopPadding //for scrolling down
            || scrollable.scrollLeft > 0 && delta > 0  && scrollTop <= scrollTopPosition + scrollTopPadding){ //for scrolling up
            scrollable.scrollLeft -= (delta * speed); //executes scrolling
            event.preventDefault(); //prevents event from default up or down scroll
            $('body')[0].scrollTop = scrollTopPosition //snap vertical scroll
        }
    });
 });

// Toggle Interests and change color
function swaptext(div) {
    var interests = [
        "Entrepreurship",
        "Design",
        "UI & UX",
        "Architecture",
        "Quality Products",
        "Business & Economics",
        "Self-Development",
        "Philosphy",
    ];
    var x = document.getElementById(div);
    var index = x.getAttribute("interestId");
    console.log(index);
    if (x.innerHTML === "Click me!") {
      x.innerHTML = interests[index];
      x.style.color = "#545454";
      x.style.backgroundColor = "#C3BFBF";
    } else {
      x.innerHTML = "Click me!";
      x.style.color = "#C3BFBF";
      x.style.backgroundColor = "#545454";
    }
}

// Down Arrow //adopted from https://codepen.io/nxworld/pen/OyRrGy
$(function() {
    $('a.arrow-down').click(function(e) {
      e.preventDefault();
      $('html, body').animate({ scrollTop: $($(this).attr('href')).offset().top}, 500, 'linear');
    });
  });