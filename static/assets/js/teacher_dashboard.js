// ==============================
// AttendX Teacher Dashboard
// ==============================

// Start Attendance Session

const startBtn = document.querySelector(".start-btn");

if(startBtn){

startBtn.addEventListener("click",function(){

const semester=document.querySelectorAll("select")[0].value;
const subject=document.querySelectorAll("select")[1].value;
const period=document.querySelectorAll("select")[2].value;

alert(
"✅ Attendance Session Started!\n\n"+
"Semester : "+semester+
"\nSubject : "+subject+
"\nPeriod : "+period
);

this.innerHTML="🟢 Session Running";
this.style.background="#16a34a";

});

}


// ==============================
// Sidebar Active Menu
// ==============================

const menuItems=document.querySelectorAll(".sidebar ul li");

menuItems.forEach(item=>{

item.addEventListener("click",()=>{

menuItems.forEach(i=>i.classList.remove("active"));

item.classList.add("active");

});

});


// ==============================
// Quick Action Buttons
// ==============================

const buttons=document.querySelectorAll(".action-card button");

if(buttons.length>=4){

buttons[0].onclick=()=>{window.location.href="/manage_students/"};

buttons[1].onclick=()=>{window.location.href="/teacher_marks/"};

buttons[2].onclick=()=>{window.location.href="/teacher_library/"};

buttons[3].onclick=()=>{window.location.href="/attendance_report/"};

}


// ==============================
// Logout
// ==============================

const logout = document.querySelector(".logout a");

if(logout){

logout.addEventListener("click",function(e){

if(!confirm("Are you sure you want to logout?")){

e.preventDefault();

}

});

}


// ==============================
// Sidebar Toggle (Mobile)
// ==============================

const menuBtn=document.querySelector(".menu-btn");
const sidebar=document.querySelector(".sidebar");

if(menuBtn && sidebar){

menuBtn.addEventListener("click",function(e){

e.stopPropagation();

sidebar.classList.toggle("active");

});

document.addEventListener("click",function(e){

if(
!sidebar.contains(e.target) &&
!menuBtn.contains(e.target)
){

sidebar.classList.remove("active");

}

});

}


// ==============================
// Welcome
// ==============================

window.onload=function(){

console.log("AttendX Teacher Dashboard Loaded Successfully.");

};