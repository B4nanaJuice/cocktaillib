function search(text) {
    // Get all divs 
    document.querySelectorAll(".cocktail").forEach((div) => {
        // Set all to invisible (display: none)
        div.style.display = 'none'
        // Test if value in name or ingredient
        // If found, show the div
        if (div.querySelector(".title").textContent.toLowerCase().includes(text.toLowerCase())) {
            div.style.display = 'block'
        }

        div.querySelectorAll(".ingredient").forEach((ingredient) => {
            if (ingredient.textContent.toLowerCase().includes(text.toLowerCase())) {
                div.style.display = 'block'
            }
        })
    })
}