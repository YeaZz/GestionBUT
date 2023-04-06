const forms = document.getElementsByTagName("form")
const modals = document.getElementsByClassName("modal")

// Automatic form : submit on click
Array.from(forms).forEach(form => {
    form.addEventListener("click", () => {
        if (form.className.includes("auto"))
            form.submit()
    })
})

// Modal : close a openned modal
Array.from(modals).forEach(modal => {
    modal.addEventListener("click", (event) => {
        if (event.target == modal) {
            modal.style.display = "none"
            document.body.style.overflowY = "overlay"
        }
    })
})