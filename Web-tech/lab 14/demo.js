function showMessage() {
    alert("Це спливаюче вікно.");
}

function openNewWindow() {
    window.open("https://www.google.com", "_blank", "width=400,height=300");
}

function confirmMessage() {
    let result = confirm("Ви впевнені?");
    
    if (result) {
        alert("OK.");
    } else {
        alert("Cancel.");
    }
}

function promptMessage() {
    let name = prompt("Як вас звати?");
    alert("Вітаю, " + name + "!");
}
function greetUser() {
    let name = document.getElementById("userName").value;
    alert("Вітаю, " + name + "!");
}

function showInput() {
    let text = document.getElementById("inputField").value;
    console.log("Ви ввели: " + text);
}

function handleSubmit(event) {
    event.preventDefault();
    let value = document.getElementById("dataInput").value;
    alert("Введено: " + value);
}