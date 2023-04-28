function addIngredient(first = 0) {
    parent = document.querySelector(".ingredients")
    button = document.querySelector(".addIngredient")

    // Create the div
    div = document.createElement("div")
    div.classList.add("ingredient")

    // Create the ingredient name input
    ingredientName = document.createElement("input")
    ingredientName.type = "text"
    ingredientName.placeholder = "Nom de l'ingrédient"
    ingredientName.name = "ingredientName"

    // Create the ingredient quantity input
    ingredientQuantity = document.createElement("input")
    ingredientQuantity.type = "number"
    ingredientQuantity.placeholder = "Quantité"
    ingredientQuantity.name = "ingredientQuantity"
    ingredientQuantity.step = 0.5

    // Create the label for the quantity input
    label = document.createElement("label")
    label.innerText = "cl"
    label.htmlFor = "ingredientQuantity"

    if (first == 0) {
        // Create a button to remove an ingredient
        removeButton = document.createElement("button")
        removeButton.innerText = "-"
        removeButton.type = "button"

        // Set button action
        removeButton.setAttribute('onclick', 'removeIngredient(this)')
    }

    // Add the inputs in the div
    div.appendChild(ingredientName)
    div.appendChild(ingredientQuantity)
    div.appendChild(label)

    if (first == 0) {
        div.appendChild(removeButton)
    }

    // Put the div in the form
    parent.insertBefore(div, button)
}

addIngredient(first = 1)