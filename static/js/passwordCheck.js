function checkPassword() {
    // Get all check divs
    uppercase = document.querySelector(".has-uppercase")
    lowercase = document.querySelector(".has-lowercase")
    number = document.querySelector(".has-number")
    special_char = document.querySelector(".has-special-char")
    length = document.querySelector(".password-length")

    match = document.querySelector(".match")
    password = document.getElementsByName("password")[document.getElementsByName("password").length - 1].value
    password_repeat = document.getElementsByName("password-repeat")[document.getElementsByName("password-repeat").length - 1].value

    // Get submit button
    submit = document.getElementsByName("submit")[document.getElementsByName("submit").length - 1]

    console.log(password_repeat)

    checks = [
        uppercase, lowercase, number, special_char, length, match
    ]

    // Generate conditions
    conditions = [
        /[A-Z]/.test(password),
        /[a-z]/.test(password),
        /[0-9]/.test(password),
        /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/.test(password),
        password.length >= 8,
        password === password_repeat
    ]

    // For each condition, test if valid
    // If valid: put the color green (var(--secondary))
    // else: turn basic color
    for (check_index = 0; check_index < checks.length; check_index++) {
        checks[check_index].style.color = conditions[check_index] ? getComputedStyle(document.documentElement).getPropertyValue("--secondary") : getComputedStyle(document.documentElement).getPropertyValue("--light-gray")
    }

    // If all conditions are met: enable the button
    // Else: disable the button
    if (conditions.includes(false)) {
        submit.classList.add("disabled")
    } else {
        submit.classList.remove("disabled")
    }
    
    submit.disabled = conditions.includes(false) && checkUsername()

}