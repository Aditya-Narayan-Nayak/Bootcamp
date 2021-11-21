function switchoff() {
    document.getElementById("bulbImage").src =
        "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/bulb-go-off-img.png";
    document.getElementById("catimage").src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/cat-eyes-img.png";
    document.getElementById("switchstatus").textContent = "switch off";
    document.getElementById("onSwitch").style.backgroundColor = "#22c55e";
  document.getElementById("offSwitch").style.backgroundColor = "#cbd2d9";
}

function switchon() {
    document.getElementById("bulbImage").src =
        "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/bulb-go-on-img.png";
    document.getElementById("catimage").src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/cat-img.png";
    document.getElementById("switchstatus").textContent = "switch on";
    document.getElementById("offSwitch").style.backgroundColor = "#e12d39";
  document.getElementById("onSwitch").style.backgroundColor = "#cbd2d9";
    
}
