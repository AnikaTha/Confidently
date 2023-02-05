var button = document.createElement("button");
button.innerHTML = "Check Email";
button.style.backgroundColor = "white";
button.style.width = "100px";
button.style.height = "50px";
button.style.boxShadow = "none";
button.style.marginRight = "75px";
button.style.borderRadius = "8px";
// button.style.color = "rgb(250, 0, 250)";
button.style.color = "rgb(250, 250, 250)";
button.style.backgroundColor = "rgb(250, 0, 250)";



var button2 = document.createElement("button");
button2.innerHTML = "Rewrite Email";
button2.style.backgroundColor = "white";
button2.style.width = "100px";
button2.style.height = "50px";
button2.style.boxShadow = "none";
button2.style.borderRadius = "8px";
// button2.style.color = "rgb(250, 0, 250)";
// button2.style.color = "rgb(250, 250, 250)";
button2.style.backgroundColor = "rgb(173,255,47)";







button.addEventListener("click", function() {
  alert("Button was clicked! D:");
});

document.body.appendChild(button);
document.body.appendChild(button2);

