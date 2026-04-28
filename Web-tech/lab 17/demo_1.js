function toggleFAQ(id) {
    let content = document.getElementById(id);
    let all = document.querySelectorAll('.faq-content');
    all.forEach(item => {
        if (item.id !== id) {
            item.style.maxHeight = null;
            item.style.padding = "0 15px";
            localStorage.setItem(item.id, "closed");
        }
    });
    if (content.style.maxHeight) {
        content.style.maxHeight = null;
        content.style.padding = "0 15px";
        localStorage.setItem(id, "closed");
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
        content.style.padding = "15px";
        localStorage.setItem(id, "open");
    }
}
window.onload = function () {
    let blocks = document.querySelectorAll('.faq-content');

    blocks.forEach(block => {
        let state = localStorage.getItem(block.id);

        if (state === "open") {
            block.style.maxHeight = block.scrollHeight + "px";
            block.style.padding = "15px";
        }
    });
};