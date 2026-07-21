// =====================================
// Mobile Sidebar Toggle
// =====================================

const menuBtn = document.getElementById("menuBtn");
const sidebar = document.getElementById("sidebar");

menuBtn.addEventListener("click", () => {

    sidebar.classList.toggle("active");

});

// =====================================
// Close Sidebar after Click (Mobile)
// =====================================

// const menuItems = document.querySelectorAll(".sidebar ul li");

// menuItems.forEach(item => {

//     item.addEventListener("click", () => {

//         if(window.innerWidth <= 768){

//             sidebar.classList.remove("active");

//         }

//         menuItems.forEach(i=>i.classList.remove("active"));

//         item.classList.add("active");

//     });

// });

// =====================================
// Close Sidebar on Outside Click
// =====================================

document.addEventListener("click",(e)=>{

    if(window.innerWidth<=768){

        if(
            !sidebar.contains(e.target)
            &&
            !menuBtn.contains(e.target)
        ){

            sidebar.classList.remove("active");

        }

    }

});

// =====================================
// Live Date & Time
// =====================================

function updateDateTime(){

const now=new Date();

const date=now.toLocaleDateString("en-IN",{

day:"2-digit",

month:"long",

year:"numeric"

});

const time=now.toLocaleTimeString("en-IN",{

hour:"2-digit",

minute:"2-digit",

second:"2-digit"

});

document.getElementById("currentDate").innerHTML="📅 "+date;

document.getElementById("currentTime").innerHTML="🕒 "+time;

}

updateDateTime();

setInterval(updateDateTime,1000);



// =====================================
// Logout
// =====================================

const logout=document.querySelector(".logout");

logout.addEventListener("click",()=>{

let confirmLogout=confirm("Do you really want to Logout?");

if(confirmLogout){

window.location.href="login.html";

}

});

// =====================================
// Greeting Change Automatically
// =====================================

// =====================================
// Small Animation
// =====================================

const cards=document.querySelectorAll(".quick-card");

cards.forEach((card,index)=>{

card.style.opacity="0";

card.style.transform="translateY(30px)";

setTimeout(()=>{

card.style.transition=".5s";

card.style.opacity="1";

card.style.transform="translateY(0px)";

},250*index);

});