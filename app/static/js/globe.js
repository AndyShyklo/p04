// Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
// JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
// SoftDev
// p04
// 2025-03-28

const globe = document.getElementById("globe");
let globePosX = 50;
let globePosY = 0;
let globeZoom = 0.7;


globe.style.backgroundPositionX = `${globePosX}px`;

globe.addEventListener("wheel", (e) => {
    e.preventDefault();
    
    globeZoom += e.deltaY < 0 ? 0.05 : -0.05;
    globeZoom = Math.max(globeZoom, 1.8)
    globe.style.backgroundSize = `${800 * globeZoom}px`
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