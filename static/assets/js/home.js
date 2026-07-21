// ================================
// ATTENDX NAVBAR MENU
// ================================

const menuToggle = document.getElementById("menuToggle");
const navMenu = document.getElementById("navMenu");

// Open / Close Menu
menuToggle.addEventListener("click", () => {

    navMenu.classList.toggle("active");

    // Change Icon
    if (navMenu.classList.contains("active")) {
        menuToggle.innerHTML = "✖";
    } else {
        menuToggle.innerHTML = "☰";
    }

});

// Close Menu When Clicking Any Link
const navLinks = document.querySelectorAll(".nav-menu a");

navLinks.forEach(link => {

    link.addEventListener("click", () => {

        navMenu.classList.remove("active");
        menuToggle.innerHTML = "☰";

    });

});

// Close Menu When Screen Becomes Large
window.addEventListener("resize", () => {

    if (window.innerWidth > 992) {
        navMenu.classList.remove("active");
        menuToggle.innerHTML = "☰";
    }

});

// 2nd page

// ================================
// VBU Latest Updates Slider
// ================================

const slides = document.querySelectorAll(".slide");
const dots = document.querySelectorAll(".dot");
const progress = document.querySelector(".progress");

let currentSlide = 0;
let interval;

// Show Slide
function showSlide(index){

    slides.forEach((slide)=>{
        slide.classList.remove("active");
    });

    dots.forEach((dot)=>{
        dot.classList.remove("active");
    });

    slides[index].classList.add("active");
    dots[index].classList.add("active");

    progress.style.width = ((index + 1) / slides.length) * 100 + "%";
}

// Auto Slide
function startSlider(){

    interval = setInterval(()=>{

        currentSlide++;

        if(currentSlide >= slides.length){
            currentSlide = 0;
        }

        showSlide(currentSlide);

    },3000);

}

// Dot Click
dots.forEach((dot,index)=>{

    dot.addEventListener("click",()=>{

        clearInterval(interval);

        currentSlide = index;

        showSlide(currentSlide);

        startSlider();

    });

});

// Start
showSlide(currentSlide);
startSlider();



// 7 page

//===========================
// FAQ Accordion
//===========================

const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach(item => {

    const question = item.querySelector(".faq-question");

    question.addEventListener("click", () => {

        item.classList.toggle("active");

    });

});