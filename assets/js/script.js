const forms = document.getElementsByTagName("form")
const modals = document.getElementsByClassName("modal")

Array.from(forms).forEach(form => {
    form.addEventListener("click", () => {
        if (form.className.includes("auto"))
            form.submit()
    })
})

Array.from(modals).forEach(modal => {
    modal.addEventListener("click", (event) => {
        if (event.target == modal) {
            modal.style.display = "none"
            document.body.style.overflowY = "overlay"
        }
    })
})