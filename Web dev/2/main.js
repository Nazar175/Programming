const title = document.getElementById("title");
const button = document.getElementById("btn");

button.addEventListener("click", function() {
    title.textContent = "Кнопку натиснуто!";
});
