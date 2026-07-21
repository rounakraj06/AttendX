// ===============================
// Dark Mode
// ===============================

const darkMode = document.getElementById("darkMode");

darkMode.addEventListener("change", function () {

    if (this.checked) {

        document.body.style.background = "#0f172a";
        document.body.style.color = "#ffffff";

        document.querySelectorAll(".setting-card").forEach(card => {

            card.style.background = "#1e293b";
            card.style.color = "#ffffff";

        });

    } else {

        document.body.style.background = "#f4f7fb";
        document.body.style.color = "#1e293b";

        document.querySelectorAll(".setting-card").forEach(card => {

            card.style.background = "#ffffff";
            card.style.color = "#1e293b";

        });

    }

});

// ===============================
// Change Password
// ===============================

const changeBtn = document.querySelector(".setting-card button");

changeBtn.addEventListener("click", () => {

    let oldPass = prompt("Enter Current Password");

    if(oldPass == null) return;

    let newPass = prompt("Enter New Password");

    if(newPass == null) return;

    alert("✅ Password Changed Successfully.");

});

// ===============================
// Notification Switch
// ===============================

const notification = document.querySelectorAll("input")[0];

notification.addEventListener("change",function(){

    if(this.checked){

        alert("🔔 Notifications Enabled");

    }

    else{

        alert("🔕 Notifications Disabled");

    }

});

// ===============================
// Language
// ===============================

const language = document.querySelector("select");

language.addEventListener("change",()=>{

    alert("Language changed to : " + language.value);

});

// ===============================
// Contact Support
// ===============================

const supportBtn = document.querySelectorAll(".setting-card button")[1];

supportBtn.addEventListener("click",()=>{

    alert("📧 Email : support@attendx.com\n📞 Phone : +91 XXXXX XXXXX");

});

// ===============================
// Logout
// ===============================

const logoutBtn = document.getElementById("logoutBtn");

logoutBtn.addEventListener("click",()=>{

    let logout = confirm("Are you sure you want to Logout?");

    if(logout){

        window.location.href="login.html";

    }

});

// ===============================
// Page Animation
// ===============================

const cards = document.querySelectorAll(".setting-card");

cards.forEach((card,index)=>{

    card.style.opacity="0";
    card.style.transform="translateY(25px)";

    setTimeout(()=>{

        card.style.transition=".5s";
        card.style.opacity="1";
        card.style.transform="translateY(0px)";

    },150*index);

});