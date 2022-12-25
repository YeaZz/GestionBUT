const bodyElement = document.getElementById("body")
const addEstablishment = document.getElementById("add_establishment")

const modals = document.getElementsByClassName("modal")

if (addEstablishment != undefined) {
    const addModal = document.getElementsByClassName("modal add")[0]
    if (addModal != undefined) {
        addEstablishment.addEventListener("click", () => {
            addModal.style.display = "block"
            bodyElement.style.overflow = "hidden"
        })
    }
}

Array.from(modals).forEach(modal => {
    modal.addEventListener("click", (event) => {
        if (event.target == modal) {
            modal.style.display = "none"
            bodyElement.style.overflow = "auto"
        }
    })
})