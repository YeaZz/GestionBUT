const establishmentChoise = document.getElementById("establishment")

displayDepartment()

function displayDepartment() {
    Array.from(departmentChoice.options).forEach(option => {
        let value = option.value
        const currentDepartment = document.getElementsByClassName(value)[0]
        if (currentDepartment == undefined)
            return
        if (option.selected)
            currentDepartment.style.display = "flex"
        else
            currentDepartment.style.display = "none"
        return
    })
}