//mobile menu variable
let navBtn = document.getElementById("toggle");
let menu = document.querySelector(".bottom-menu");

//popup variables
let popupbtn = document.querySelector(".bell-icon");
let popup = document.getElementById("myPopup");

let mobilepopupbtn = document.querySelector(".mobile-bell-icon");//For mobile
let mobilepopup = document.getElementById("mobilePopup");

//Modal form variables

//Mobile menu initialization script
navBtn.addEventListener("click", function(){
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
});

//notification popup
popupbtn.addEventListener("click", function() {
    popup.classList.toggle("show");
});
mobilepopupbtn.addEventListener("click", function() {
    mobilepopup.classList.toggle("show");
});



