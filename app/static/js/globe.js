// Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
// JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
// SoftDev
// p04
// 2025-03-28

const globe = document.getElementById("globe");
let globePosX = 50;
let globePosY = 0;
let scrollSens = 0.7;


globe.style.backgroundPositionX = `${globePosX}px`;

globe.addEventListener("wheel", (e) => {
    e.preventDefault();

    globePosX -= e.deltaX * scrollSens;
    globePosY -= e.deltaY * scrollSens;

    globe.style.backgroundPosition = `${globePosX}px ${globePosY}px`;
});

function rotate(event) {
    const moveStep = 50;

    switch (event.key) {
        case "ArrowUp":
            globePosY += moveStep;
            break;
        case "ArrowDown":
            globePosY -= moveStep;
            break;
        case "ArrowLeft":
            globePosX += moveStep;
            break;
        case "ArrowRight":
            globePosX -= moveStep;
            break;
        default:
            return;
    }

    globe.style.backgroundPosition = `${globePosX}px ${globePosY}px`;
}

globe.addEventListener("mouseenter", () => {
    document.addEventListener("keydown", rotate);
});

globe.addEventListener("mouseleave", () => {
    document.removeEventListener("keydown", rotate);
});

function grow(){
    globe.style.transform = "scale(6)";
    globe.style.backgroundPosition = `${globePosX + 1000}px ${globePosY + 50}px`;
    globe.style.transition = "1s";
    setTimeout(function() { window.location.href = "map" }, 900);
}
