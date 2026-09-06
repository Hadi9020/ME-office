//================================
//values
//================================
const pingUrl = document.body.dataset.pingUrl;
const profile = document.getElementById('profilePart');
const profileKey = document.getElementById('pro');

//================================
//Box Drag
//================================

$("#box").draggable({
    scroll: true,
    containment: "#main",
    cursor: "grabbing",

    start: function() {
        this.style.opacity = "0.5";
    },

    drag: function() {
        this.style.opacity = "1";
        this.style.backgroundColor = "rgba(10, 10, 225, 0.5)";
    },

    stop: function() {
        this.style.opacity = "0.5";

        setTimeout(function() {
            this.style.opacity = "1";
        }.bind(this), 1000);
    }
});

// ===============================
// Internet Status
// ===============================

const internetColors = {
    offline: "#202020",
    terrible: "#8B0000",
    bad: "#B85C00",
    normal: "#C9A227",
    good: "#2E8B57",
    excellent: "#00C853"
};


async function checkInternet(){

    if(!navigator.onLine){
        return "offline";
    }

    const start = performance.now();

    try{

            await fetch(pingUrl + "?ping=" + Date.now(), {
                cache: "no-store"
            });


        const ping = performance.now() - start;


        if(ping < 40) return "excellent";
        if(ping < 100) return "good";
        if(ping < 180) return "normal";
        if(ping < 350) return "bad";

        return "terrible";


    }
    catch(error){

        console.error("Internet check error:", error);
        return "offline";

    }

}


async function updateInternetStatus(){

    const status = await checkInternet();

    const target = document.getElementById("internet-check");


    target.textContent = status;
    target.style.backgroundColor = internetColors[status];

}


// ===============================
// Menu Control
// ===============================

function openMenu(){

    const menu = document.getElementById("menu");
    const glass = document.getElementById("glass-model");


    menu.style.zIndex = "6";
    glass.style.zIndex = "5";

    menu.style.left = "80vw";

    glass.style.display = "block";
    glass.style.opacity = "0.5";

}



function closeMenu(){

    const menu = document.getElementById("menu");
    const glass = document.getElementById("glass-model");


    menu.style.zIndex = "0";
    glass.style.zIndex = "-2";

    menu.style.left = "100vw";

    glass.style.opacity = "0";
    glass.style.display = "none";

}


// ===============================
// SSS Control
// ===============================

function openSpacialSiteScape(){
    alert("the spacial site scape (S.S.S.) is not redy now... .It's coming soon... .")
}


// ===============================
// Profile Control
// ===============================

function openProfile(){
    const p = profile.style

    p.display = "block";
    p.zIndex = "4";
    p.opacity = "1";
}

function closeProfile(){
    const p = profile.style

    p.display = "hidden";
    p.zIndex = "-5";
    p.opacity = "0";
}


// ===============================
// Clock
// ===============================

function updateClock(){

    const now = new Date();


    const hour = String(now.getHours())
        .padStart(2, "0");


    const minute = String(now.getMinutes())
        .padStart(2, "0");


    const clock = document.getElementById("clock");


    clock.textContent = `<${hour}:${minute}>`;

}



// ===============================
// Start
// ===============================

closeProfile();

profileKey.addEventListener("click", openProfile);

document.getElementById('backProfile').addEventListener("click", closeProfile);

const topIcon = document.querySelector("#topIcon");
topIcon.addEventListener("click", openMenu);

const bottomIcon = document.querySelector("#bottomIcon");
bottomIcon.addEventListener("click", openSpacialSiteScape);

const menuCloseButton = document.querySelector("#mcb");
menuCloseButton.addEventListener("click", closeMenu);


updateClock();
updateInternetStatus();


setInterval(updateClock, 60000);
setInterval(updateInternetStatus,15000);

let a = document.getElementById('box'); a = a.style;
a.top = '80%';
a.left = '90%';

el.addEventListener("pointerdown", startDrag);