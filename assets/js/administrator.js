const addEstablishment = document.getElementById("add_establishment")
const addDepartment = document.getElementById("add_department")
const addCompetence = document.getElementById("add_competence")
const addSemester = document.getElementById("add_semester")
const addGroup = document.getElementById("add_group")

function modalAddListener(add, modal) {
    if (add == undefined || modal == undefined) return
    add.addEventListener("click", () => {
        modal.style.display = "block"
        document.body.style.overflow = "hidden"
    })
}

modalAddListener(addEstablishment, document.querySelector(".modal.add_establishment"))
modalAddListener(addDepartment, document.querySelector(".modal.add_department"))
modalAddListener(addCompetence, document.querySelector(".modal.add_competence"))
modalAddListener(addSemester, document.querySelector(".modal.add_semester"))
modalAddListener(addGroup, document.querySelector(".modal.add_group"))
