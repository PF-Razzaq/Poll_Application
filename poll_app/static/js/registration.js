// Function to display errors below input fields
function displayError(inputId, errorMessage) {
  let errorElement = document.getElementById(inputId + "-error");
  if (!errorElement) {
    errorElement = document.createElement("div");
    errorElement.id = inputId + "-error";
    errorElement.className = "text-danger";
    document.getElementById(inputId).parentNode.appendChild(errorElement);
  }
  errorElement.innerHTML = errorMessage;
}

// Function to validate email
function validateEmail(email) {
  let emailRegex = /^(?=.*[a-zA-Z0-9])(?=.*[!@#$%^&*]).{6,}$/;
  return emailRegex.test(email);
}

// Function to validate CNIC
function validateCNIC(cnic) {
  let cnicRegex = /^\d{5}-\d{7}-\d{1}$/;
  return cnicRegex.test(cnic);
}

// Function to validate mobile number
function validateMobileNumber(mobileNumber) {
  let mobileNumberRegex = /^\d{4}-\d{7}$/;
  return mobileNumberRegex.test(mobileNumber);
}

// Function to validate password
function validatePassword(password) {
  let passwordRegex = /^(?=.*[a-zA-Z])(?=.*[!@#$%^&*])(?=.*[0-9]).{8,}$/;
  return passwordRegex.test(password);
}

// Function to handle form submission
function validateForm() {
  let email = document.getElementById("id_email").value;
  let cnic = document.getElementById("id_cnic").value;
  let mobileNumber = document.getElementById("id_mobile_no").value;
  let password = document.getElementById("id_password").value;
  let confirmPassword = document.getElementById("id_confirm_password").value;

  let isValid = true;

  // Validate email
  if (!validateEmail(email)) {
    displayError(
      "id_email",
      "Email must be at least 6 characters and contain at least one special character or number."
    );
    isValid = false;
  } else {
    displayError("id_email", "");
  }

  // Validate CNIC
  if (!validateCNIC(cnic)) {
    displayError("id_cnic", "CNIC must be in the format XXXXX-XXXXXXX-X.");
    isValid = false;
  } else {
    displayError("id_cnic", "");
  }

  // Validate mobile number
  if (!validateMobileNumber(mobileNumber)) {
    displayError(
      "id_mobile_no",
      "Mobile number must be in the format XXXX-XXXXXXX."
    );
    isValid = false;
  } else {
    displayError("id_mobile_no", "");
  }

  // Validate password
  if (!validatePassword(password)) {
    displayError(
      "id_password",
      "Password must be at least 8 characters and contain at least one special symbol and one uppercase or lowercase character."
    );
    isValid = false;
  } else {
    displayError("id_password", "");
  }

  // Confirm password
  if (password !== confirmPassword) {
    displayError("id_confirm_password", "Passwords do not match.");
    isValid = false;
  } else {
    displayError("id_confirm_password", "");
  }

  return isValid;
}

function validateAge(input) {
  // Remove non-digit characters
  input.value = input.value.replace(/[^0-9]/g, "");

  // Parse the value as an integer
  let age = parseInt(input.value);

  // Check if it's within the desired range (18 to 120)
  if (isNaN(age) || age < 18) {
    input.setCustomValidity("Age must be at least 18.");
  } else if (age > 120) {
    input.setCustomValidity("Age must not exceed 120.");
  } else {
    input.setCustomValidity("");
  }
}
