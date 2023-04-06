const establishmentChoice = document.getElementById("establishmentSelection")
const semesterChoice = document.getElementById("semesterSelection")

const students = document.querySelectorAll(".students")
const groupChoices = document.querySelectorAll(".group")

const importInputs = document.querySelectorAll(".import_evaluation")

const studentInput = document.getElementById("student_search")
const studentContainer = document.querySelector(".grid-students")

// Select : change semester
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

// Select : change semester
if (semesterChoice != undefined) {
    displaySemester()

    semesterChoice.addEventListener("click", () => {
        displaySemester()
    })

    function displaySemester() {
        Array.from(semesterChoice.options).forEach(option => {
            let value = option.value
            let currentSemester = document.getElementsByClassName("grid-semester " + value)[0]
            if (currentSemester == undefined) return
            if (option.selected) currentSemester.style.display = "table"
            else currentSemester.style.display = "none"
            return
        })
    }
}

// Modal : Select : display students by choosen group
if (students.length > 0) {
    Array.from(groupChoices).forEach(select => {
        displayStudents(select)
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

// Card : add listener on add cards
function cardAddListener(card, modal) {
    if (card == undefined || modal == undefined) return
    card.addEventListener("click", () => {
        modal.style.display = "block"
        document.body.style.overflowY = "hidden"
    })
}

// Card : add listeners on cards
function addListeners(name) {
    const resources = document.querySelectorAll(".add_" + name)
    Array.from(resources).filter(resource => !resource.classList.contains('modal')).forEach(resource => {
        let value = resource.classList[1]
        let current = document.getElementsByClassName("modal add_" + name + " " + value)[0]
        cardAddListener(resource, current)
    })

    const cards = document.querySelectorAll("." + name)
    if (cards.length == 0) return
    Array.from(cards).forEach(card => {
        let value = card.classList[1]
        let current = document.getElementsByClassName("modal " + value)[0]
        cardAddListener(card, current)
    })
}

addListeners("evaluation")
addListeners("grid-evaluation")

// Modal : import a CSV files containing notes
if (importInputs != undefined) {

    Array.from(importInputs).forEach(importInput => {
        const students = importInput.parentNode.parentNode.getElementsByClassName("students")

        importInput.onchange = function() {
            let reader = new FileReader();
            reader.onload = function() {
                lines = reader.result.split('\r\n')
                lines.pop()
                lines.forEach(line => {
                    [id, note] = line.split(';')
                    note = note.replace(',', '.')
                    Array.from(students).forEach(student => {
                        Array.from(student.children).forEach(child => {
                            if (child.tagName == "INPUT" && child.name == ("note " + student.classList[1] + " " + id)) {
                                child.value = +note
                            }
                        })
                    })
                })
            }

            if (importInput.files.length > 0)
                reader.readAsText(importInput.files[0])
        }
    })
}

// Students page : filter by name
if (studentInput != undefined && studentContainer != undefined) {

    const studentList = Array.from(studentContainer.children)

    studentList.forEach((student) => {
        let studentId = student.classList[1]
        let card = document.getElementsByClassName("modal student " + studentId)[0]
        cardAddListener(student, card)
    })

    function filteredStudents() {
        let selection = []
        let input = studentInput.value.toLocaleLowerCase()
        Array.from(studentList).forEach((student) => {
            if (student.innerHTML.toLocaleLowerCase().includes(input))
                selection.push(student)
        })
        return selection
    }

    function render(students) {
        studentContainer.innerHTML = ""
        Array.from(students).forEach((student) => {
            studentContainer.appendChild(student)
        })
    }

    studentInput.addEventListener("input", () => {
        render(filteredStudents())
    })
}