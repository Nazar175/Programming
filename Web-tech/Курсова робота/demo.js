(function () {
    "use strict";

    const triggerSelector = ".js-register-trigger";
    const popupName = "teklink_register_window";
    const popupFeatures = "width=520,height=620,left=220,top=120,resizable=yes,scrollbars=yes";

    function createPopupMarkup() {
        return `<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Реєстрація в TekLink</title>
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f5f7;
            color: #1f1f1f;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 18px;
        }
        .register-card {
            width: 100%;
            max-width: 420px;
            background: #ffffff;
            border-radius: 14px;
            border: 1px solid #d9d9d9;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            padding: 22px;
        }
        h1 {
            margin: 0 0 8px;
            font-size: 26px;
        }
        p {
            margin: 0 0 18px;
            color: #4f4f4f;
            line-height: 1.5;
            font-size: 15px;
        }
        .field {
            margin-bottom: 14px;
        }
        label {
            display: block;
            margin-bottom: 6px;
            font-size: 14px;
            font-weight: 600;
        }
        input {
            width: 100%;
            border: 1px solid #cfcfcf;
            border-radius: 10px;
            padding: 10px 12px;
            font-size: 15px;
            outline: none;
        }
        input:focus {
            border-color: #0fa6ff;
            box-shadow: 0 0 0 3px rgba(15, 166, 255, 0.15);
        }
        .error {
            min-height: 20px;
            color: #c43131;
            font-size: 13px;
            margin-bottom: 8px;
        }
        .submit-btn {
            width: 100%;
            border: none;
            border-radius: 10px;
            padding: 12px;
            background: #0fa6ff;
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
        }
        .submit-btn:hover {
            background: #008edc;
        }
    </style>
</head>
<body>
    <section class="register-card">
        <h1>Реєстрація</h1>
        <p>Заповніть форму, щоб створити обліковий запис TekLink.</p>

        <form id="registerForm" novalidate>
            <div class="field">
                <label for="regName">Ім'я</label>
                <input id="regName" name="name" type="text" placeholder="Введіть ваше ім'я" autocomplete="name" required>
            </div>

            <div class="field">
                <label for="regEmail">Email</label>
                <input id="regEmail" name="email" type="email" placeholder="name@example.com" autocomplete="email" required>
            </div>

            <div class="field">
                <label for="regPassword">Пароль</label>
                <input id="regPassword" name="password" type="password" placeholder="Мінімум 6 символів" minlength="6" autocomplete="new-password" required>
            </div>

            <div class="error" id="formError"></div>
            <button class="submit-btn" type="submit">Зареєструватися</button>
        </form>
    </section>
</body>
</html>`;
    }

    function attachPopupHandlers(regWindow) {
        const form = regWindow.document.getElementById("registerForm");
        const nameInput = regWindow.document.getElementById("regName");
        const emailInput = regWindow.document.getElementById("regEmail");
        const passwordInput = regWindow.document.getElementById("regPassword");
        const errorBox = regWindow.document.getElementById("formError");

        if (!form || !nameInput || !emailInput || !passwordInput || !errorBox) {
            return;
        }

        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const name = nameInput.value.trim();
            const email = emailInput.value.trim();
            const password = passwordInput.value;

            if (!name || !email || !password) {
                errorBox.textContent = "Будь ласка, заповніть усі поля.";
                return;
            }

            if (password.length < 6) {
                errorBox.textContent = "Пароль має містити щонайменше 6 символів.";
                return;
            }

            errorBox.textContent = "";
            regWindow.alert(`${name}, вітаємо! Ви успішно зареєстровані!`);
            form.reset();
            nameInput.focus();
        });

        nameInput.focus();
    }

    function openRegistrationWindow() {
        const regWindow = window.open("", popupName, popupFeatures);

        if (!regWindow) {
            alert("Браузер заблокував спливаюче вікно. Дозвольте pop-up для цього сайту.");
            return;
        }

        regWindow.document.open();
        regWindow.document.write(createPopupMarkup());
        regWindow.document.close();

        attachPopupHandlers(regWindow);
        regWindow.focus();
    }

    function initRegistrationTriggers() {
        const triggers = document.querySelectorAll(triggerSelector);

        triggers.forEach(function (trigger) {
            trigger.addEventListener("click", function (event) {
                event.preventDefault();
                openRegistrationWindow();
            });
        });
    }

    function createSeededShuffle(total, seed) {
        const indices = Array.from({ length: total }, function (_, index) {
            return index;
        });
        let state = seed >>> 0;

        function random() {
            state = (state * 1664525 + 1013904223) >>> 0;
            return state / 4294967296;
        }

        for (let i = indices.length - 1; i > 0; i -= 1) {
            const j = Math.floor(random() * (i + 1));
            const temp = indices[i];
            indices[i] = indices[j];
            indices[j] = temp;
        }

        return indices;
    }

    function areSameOrder(first, second) {
        if (!first || !second || first.length !== second.length) {
            return false;
        }

        return first.every(function (value, index) {
            return value === second[index];
        });
    }

    function initMainProductsSlider() {
        const grid = document.querySelector(".products-grid");
        const prevButton = document.querySelector(".products-prev");
        const nextButton = document.querySelector(".products-more");

        if (!grid || !prevButton || !nextButton) {
            return;
        }

        const cards = Array.from(grid.querySelectorAll(".product-card"));

        if (cards.length < 2) {
            nextButton.disabled = true;
            return;
        }

        const baseOrder = cards.map(function (_, index) {
            return index;
        });
        const shuffledOrderOne = createSeededShuffle(cards.length, 20260422);
        const shuffledOrderTwo = createSeededShuffle(cards.length, 7772026);

        if (areSameOrder(baseOrder, shuffledOrderOne)) {
            shuffledOrderOne.reverse();
        }

        if (areSameOrder(baseOrder, shuffledOrderTwo) || areSameOrder(shuffledOrderOne, shuffledOrderTwo)) {
            shuffledOrderTwo.push(shuffledOrderTwo.shift());
        }

        const slides = [baseOrder, shuffledOrderOne, shuffledOrderTwo];
        let currentSlideIndex = 0;

        function renderSlide(slideIndex, withAnimation) {
            if (withAnimation) {
                grid.classList.remove("products-grid--animating");
                void grid.offsetWidth;
                grid.classList.add("products-grid--animating");
            }

            const fragment = document.createDocumentFragment();

            slides[slideIndex].forEach(function (cardIndex) {
                fragment.appendChild(cards[cardIndex]);
            });

            grid.appendChild(fragment);
            nextButton.setAttribute(
                "aria-label",
                `Показати наступний набір товарів (${slideIndex + 1} з ${slides.length})`
            );
        }

        grid.addEventListener("animationend", function () {
            grid.classList.remove("products-grid--animating");
        });

        renderSlide(currentSlideIndex, false);

        prevButton.addEventListener("click", function () {
            currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
            renderSlide(currentSlideIndex, true);
        });

        nextButton.addEventListener("click", function () {
            currentSlideIndex = (currentSlideIndex + 1) % slides.length;
            renderSlide(currentSlideIndex, true);
        });
    }

    function initMobileBurgerMenu() {
        const burgerButton = document.querySelector(".burger-toggle");
        const mobileMenu = document.querySelector(".mobile-menu");

        if (!burgerButton || !mobileMenu) {
            return;
        }

        function closeMenu() {
            mobileMenu.classList.remove("mobile-menu--open");
            burgerButton.setAttribute("aria-expanded", "false");
        }

        burgerButton.addEventListener("click", function () {
            const isOpen = mobileMenu.classList.toggle("mobile-menu--open");
            burgerButton.setAttribute("aria-expanded", String(isOpen));
        });

        document.addEventListener("click", function (event) {
            if (!mobileMenu.contains(event.target) && !burgerButton.contains(event.target)) {
                closeMenu();
            }
        });

        mobileMenu.addEventListener("click", function (event) {
            if (event.target.closest("a")) {
                closeMenu();
            }
        });

        window.addEventListener("resize", function () {
            if (window.innerWidth > 768) {
                closeMenu();
            }
        });
    }

    function initPageFeatures() {
        initRegistrationTriggers();
        initMainProductsSlider();
        initMobileBurgerMenu();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initPageFeatures);
    } else {
        initPageFeatures();
    }
})();
