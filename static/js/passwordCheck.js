function check() {
    // Get all check divs
    uppercase = document.querySelector(".has-uppercase")
    lowercase = document.querySelector(".has-lowercase")
    number = document.querySelector(".has-number")
    special_char = document.querySelector(".has-special-char")
    length = document.querySelector(".length")

    match = document.querySelector(".match")
    password = document.getElementsByName("password")[0].value
    password_repeat = document.getElementsByName("password-repeat")[0].value

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
}