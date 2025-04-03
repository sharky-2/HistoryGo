// Accordion script
let accordion_list = document.querySelectorAll("#accordion-list .item")
accordion_list.forEach(item => {
    item.addEventListener("click", function() {
        if (item.classList.contains("active")) {
            item.classList.remove("active")
        } else {
            accordion_list.forEach(el => el.classList.remove("active"))
            item.classList.add("active")
        } 
    })
})