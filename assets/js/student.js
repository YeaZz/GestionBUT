const semesterChoice = document.getElementById("semesterSelection")
const viewChoice = document.getElementById("viewSelection")

// Select : change semester
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

// Select : change view
if (viewChoice != undefined) {
    const resources = document.getElementsByClassName("resource")
    const ues = document.getElementsByClassName("ue")

    displayView()

    viewChoice.addEventListener("click", () => {
        displayView()
    })

    function displayView() {
        const value = viewChoice.value
        Array.from(resources).forEach(resource => {
            resource.style.display = value == "resource" ? "block" : "none"
        })
        Array.from(ues).forEach(ue => {
            ue.style.display = value == "ue" ? "block" : "none"
        })
    }
}