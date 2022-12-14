const forms = document.getElementsByTagName("form")

Array.from(forms).forEach(form => {
    form.addEventListener("click", () => {
        if (form.className.includes("auto"))
            form.submit()
    })
})
