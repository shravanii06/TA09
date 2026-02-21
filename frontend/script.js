// HEATMAP DATA
const zones = [
    {name:"North", risk:"high"},
    {name:"South", risk:"high"},
    {name:"East", risk:"high"},
    {name:"West", risk:"high"},
    {name:"Central", risk:"mid"},
    {name:"North-East", risk:"high"},
    {name:"South-East", risk:"high"},
    {name:"North-West", risk:"high"},
    {name:"South-West", risk:"mid"}
];

const map = document.getElementById("heatmap");

zones.forEach(z=>{
    const d=document.createElement("div");
    d.className="zone "+(z.risk==="high"?"high":z.risk==="mid"?"mid":"low");
    d.innerText=z.name+" Risk";
    map.appendChild(d);
});

// ALERTS
const alerts=[
    "Heatwave detected",
    "Dengue risk increasing",
    "Medicine stock required"
];

const alertBox=document.getElementById("alerts");
alerts.forEach(a=>{
    const div=document.createElement("div");
    div.innerHTML="⚠ "+a;
    div.style.marginBottom="8px";
    alertBox.appendChild(div);
});

// FORM
document.getElementById("form").onsubmit=e=>{
    e.preventDefault();
    alert("Symptoms submitted ✔");
}