// =========================================
// SHOW / HIDE PASSWORD
// =========================================

const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");

togglePassword.addEventListener("click", function () {

    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);

    this.classList.toggle("fa-eye");
    this.classList.toggle("fa-eye-slash");

});

// =========================================
// SHOW / HIDE CONFIRM PASSWORD
// =========================================

const toggleConfirm = document.getElementById("toggleConfirm");
const confirmPassword = document.getElementById("confirmPassword");

toggleConfirm.addEventListener("click", function () {

    const type = confirmPassword.getAttribute("type") === "password" ? "text" : "password";
    confirmPassword.setAttribute("type", type);

    this.classList.toggle("fa-eye");
    this.classList.toggle("fa-eye-slash");

});

// =========================================
// PASSWORD MATCH VALIDATION
// =========================================

const form = document.querySelector("form");

form.addEventListener("submit", function(e){

    if(password.value !== confirmPassword.value){

        e.preventDefault();

        alert("Password and Confirm Password do not match!");

        confirmPassword.focus();

        return;
    }

    // alert("Registration Successful!");

});


setTimeout(function () {
    const msg = document.getElementById("message-box");
    if (msg) {
        msg.style.display = "none";
    }
}, 4000);