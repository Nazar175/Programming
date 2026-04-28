function toggleDescription() {
    let description = document.getElementById("productDescription");
    if (description.style.display === "none") {
        description.style.display = "block";
        localStorage.setItem("descriptionState", "open");
        let pos = 0;
        let id = setInterval(function () {
            if (pos >= 200) {
                clearInterval(id);
            } else {
                pos++;
                description.style.marginLeft = pos + "px";
            }
        }, 5);
    } else {
        description.style.display = "none";
        description.style.marginLeft = "0px";
        localStorage.setItem("descriptionState", "closed");
    }
}
window.onload = function () {
    let description = document.getElementById("productDescription");
    let state = localStorage.getItem("descriptionState");

    if (state === "open") {
        description.style.display = "block";
    } else {
        description.style.display = "none";
    }
}