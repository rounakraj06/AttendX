//=========================================
// STUDENT PASSWORD SHOW / HIDE
//=========================================

const studentPassword = document.getElementById("studentPassword");
const studentEye = document.getElementById("studentEye");

if (studentPassword && studentEye) {

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

}