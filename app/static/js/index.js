const globe = document.getElementById("globe");
let globePosX = 50;
let globePosY = 0;

globe.style.backgroundPositionX = `${globePosX}px`;

globe.onclick = function() {
    console.log("fwuh fwuh fuwh")
    globePosX += 10;
    // globePosY += 10;
    globe.style.backgroundPosition = `${globePosX}px ${globePosY}px`;
};