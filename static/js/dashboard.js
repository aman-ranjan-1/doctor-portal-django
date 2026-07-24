document.addEventListener("DOMContentLoaded", function () {

    const editBtn = document.getElementById("editProfileBtn");
    const saveBtn = document.getElementById("saveProfileBtn");
    const cancelBtn = document.getElementById("cancelProfileBtn");

    const inputs = document.querySelectorAll(".patient-edit-field");

    const imageInput = document.getElementById("profileImage");
    const imagePreview = document.getElementById("imagePreview");

    // Store original values
    const originalValues = [];

    inputs.forEach(function (field) {

        originalValues.push(field.value);

    });

    // ==========================
    // Edit Profile
    // ==========================

    if (editBtn) {

        editBtn.addEventListener("click", function () {

            inputs.forEach(function (field) {

                if (field.tagName === "SELECT") {

                    field.disabled = false;

                }

                else {

                    field.removeAttribute("readonly");

                }

            });

            if (imageInput) {

                imageInput.disabled = false;

            }

            editBtn.style.display = "none";

            saveBtn.style.display = "inline-flex";

            cancelBtn.style.display = "inline-flex";

        });

    }

    // ==========================
    // Cancel
    // ==========================

    if (cancelBtn) {

        cancelBtn.addEventListener("click", function () {

            inputs.forEach(function (field, index) {

                field.value = originalValues[index];

                if (field.tagName === "SELECT") {

                    field.disabled = true;

                }

                else {

                    field.setAttribute("readonly", true);

                }

            });

            if (imageInput) {

                imageInput.disabled = true;

                imageInput.value = "";

            }

            editBtn.style.display = "inline-flex";

            saveBtn.style.display = "none";

            cancelBtn.style.display = "none";

        });

    }

    // ==========================
    // Image Preview
    // ==========================

    if (imageInput) {

        imageInput.addEventListener("change", function (e) {

            const file = e.target.files[0];

            if (!file) return;

            const reader = new FileReader();

            reader.onload = function (event) {

                imagePreview.src = event.target.result;

            };

            reader.readAsDataURL(file);

        });

    }

});