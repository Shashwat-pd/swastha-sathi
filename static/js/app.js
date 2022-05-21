const h = document.querySelector(".hamburger");
const n = document.querySelector(".nav");
const l = document.querySelectorAll(".hamburger div");

h.addEventListener("click", () => {
    n.classList.toggle("open");
    l.forEach(div => {
        div.classList.toggle("change");
    });
})