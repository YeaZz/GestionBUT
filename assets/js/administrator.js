function cardAddListener(card, modal) {
    if (card == undefined || modal == undefined) return
    card.addEventListener("click", () => {
        modal.style.display = "block"
        document.body.style.overflowY = "hidden"
    })
}

function addListeners(name) {
    cardAddListener(document.getElementById("add_" + name), document.querySelector(".modal.add_" + name))
    const cards = document.querySelectorAll(".carousel-item." + name)
    if (cards.length == 0) return
    Array.from(cards).forEach(card => {
        let value = card.classList[1]
        let current = document.getElementsByClassName("modal " + value + " " + name)[0]
        cardAddListener(card, current)
    })
}

addListeners("establishment")
addListeners("department")
addListeners("competence")
addListeners("semester")
addListeners("group")