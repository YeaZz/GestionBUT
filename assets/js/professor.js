const establishmentChoice = document.getElementById("establishmentSelection")
const semesterChoice = document.getElementById("semesterSelection")

const students = document.querySelectorAll(".students")
const groupChoices = document.querySelectorAll(".group")
const resourceButtons = document.querySelectorAll(".resource-button")
const departmentForms = document.querySelectorAll(".department-form")

const resourceModals = document.querySelectorAll(".modal")

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
            let currentSemester = document.getElementsByClassName("semester " + value)[0]
            if (currentSemester == undefined) return
            if (option.selected) currentSemester.style.display = "flex"
            else currentSemester.style.display = "none"
            return
        })
    }
}

if (students.length > 0) {

    Array.from(groupChoices).forEach(select => {
        select.addEventListener("click", () => {
            displayStudents(select)
        })
    })

    function displayStudents(select) {
        Array.from(select.options).forEach(option => {
            let value = option.value
            let currentStudents = select.parentNode.parentNode.getElementsByClassName("students " + value)[0]
            if (currentStudents == undefined) return
            if (option.selected) currentStudents.style.display = "grid"
            else currentStudents.style.display = "none"
            return
        })
    }
}

Array.from(resourceButtons).forEach(button => {
    button.addEventListener("click", () => {
        const form = button.closest("form")
        if (form != undefined && button.classList[1] != undefined) {
            const action = button.closest("form").action.split("?")[0]
            button.closest("form").action = action + "?resource=" + button.classList[1]
        }
        showModal(button.classList[1])
    })
})

function showModal(resource) {
    Array.from(resourceModals).forEach(modal => {
        if (modal.classList[1] == resource) {
            modal.style.display = "block"
            document.body.style.overflow = "hidden"
        }
    })
}

const queryString = window.location.search;
if (queryString != "") {
    const urlParams = new URLSearchParams(queryString);
    if (urlParams.has("resource")) {
        const resource = urlParams.get("resource")
        showModal(resource)
    }
}


