//=========================================
// STUDENT / TEACHER TAB SWITCH
//=========================================

const studentForm = document.getElementById("studentForm");
const teacherForm = document.getElementById("teacherForm");

const tabButtons = document.querySelectorAll(".tab-btn");

function showStudent() {

    studentForm.style.display = "flex";
    teacherForm.style.display = "none";

    tabButtons[0].classList.add("active");
    tabButtons[1].classList.remove("active");

}

//=========================================
// STUDENT PASSWORD SHOW/HIDE
//=========================================

const studentPassword = document.getElementById("studentPassword");
const studentEye = document.getElementById("studentEye");

studentEye.addEventListener("click", () => {

    if (studentPassword.type === "password") {

        studentPassword.type = "text";
        studentEye.classList.remove("fa-eye");
        studentEye.classList.add("fa-eye-slash");

    } else {

        studentPassword.type = "password";
        studentEye.classList.remove("fa-eye-slash");
        studentEye.classList.add("fa-eye");

    }

});

