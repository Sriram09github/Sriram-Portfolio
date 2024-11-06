function toggleMenu(){
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}

const typed = new Typed(".title",{
    strings:["Student","Fresher","Full-Stack Developer","Data Analyst"],
    typeSpeed:100,
    backSpeed:100,
    backDelay:750,
    loop:true,
});
 