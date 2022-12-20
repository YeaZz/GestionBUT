const establishmentChoice = document.getElementById("selection")
const semesterChoice = document.getElementById("selection")
const semesterButtons = document.getElementsByClassName("department-button")
const departmentForms = document.getElementsByClassName("department-form")

if (establishmentChoice != undefined) {
    displayEstablishment()

    establishmentChoice.addEventListener("click", () => {
        displayEstablishment()
    })
    
    function displayEstablishment() {
        Array.from(establishmentChoice.options).forEach(option => {
            let value = option.value
            const currentEstablishment = document.getElementsByClassName("establishment " + value)[0]
            if (currentEstablishment == undefined) return
            if (option.selected) currentEstablishment.style.display = "flex"
            else currentEstablishment.style.display = "none"
            return
        })
    }
}

if (semesterChoice != undefined) {
    displaySemester()

    semesterChoice.addEventListener("click", () => {
        displaySemester()
    })

    function displaySemester() {
        Array.from(semesterChoice.options).forEach(option => {
            let value = option.value
            const currentSemester = document.getElementsByClassName(value)[0]
            if (currentSemester == undefined) return
            if (option.selected) currentSemester.style.display = "flex"
            else currentSemester.style.display = "none"
            return
        })
    }
}

Array.from(semesterButtons).forEach(button => {
    button.addEventListener("click", () => {
        changeLocationOnClick(button)
    })
})

function changeLocationOnClick(button) {
    const action = button.closest("form").action.split("?")[0]
    button.closest("form").action = action + "?semester=" + button.classList[1]
}

const queryString = window.location.search;
if (queryString != "") {
    const urlParams = new URLSearchParams(queryString);
    if (urlParams.has("semester")) {
        const semester = urlParams.get("semester")

        // Get the modal then show it ...
    }
}

