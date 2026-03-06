# Звіт до роботи
## Тема: Віртуальні середовища
### Мета роботи: Навчитися створювати різні віртуальні середовища та встановлювати в них пакети.

---
## Виконання роботи:

Посилання на файл з виконаними матеріалами лекцій [venv](1_venv), [pipenv](2_pipenv) і [poetry](3_poetry).

* Результати виконання завдання:
    1. Скріншот усіх встановлених бібліотек і список усіх дій які можна робити за допомогою pip:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/20.png) ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/21.png)
    ---
    2. Результат виконання команд в REPL на прикладі встановлення бібліотеки requests і інших методів:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/22.png) ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/23.png)
    ---
    3. Інстальовано бібліотеку requests як загальньодоступну і після чого видалено її і виконана перевірка версій:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/24.png)
    ---
    4. Було запущено код про Аніме з виведенням сезонів і оцінки:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/25.png)
    Програма з виконаним завданням [тут](anime.py)
    ---
    5. До anime.py було дописано можливість перегляду поточного сезону аніме і їхніх оцінок:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/26.png)
    Програма з виконаним завданням [тут](season.py)
    ---
    6. Створено venv середовище.
    Остання команда показала глобальну версію requests тому що середовище було деактивовано. Потрібно ігнорувати папку my_env/ коли закидаєш на Github.
    ---
    7. Створено віртуальне середовище для запуску попереднього завдання.
    Було додано в поточне віртуальне середовище venv можливість запускати код anime.py і season.py, тому вивело воно те саме що і минулого разу.
    ---
    8. Pipenv може виконувати наступні команди:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/27.png) 
    ---
    9. Було створено віртуальне середовище за допомогою pipenv. Також створилися файли Pipfile (тут знаходиться список залежностей) і Pipfile.lock (тут знаходиться точні версії залежностей).
    ---
    10. Було написано тестову програмку [тут](pipenv_lab/test.py) і запущено двома способами:
    За допомогою командної стрічки: ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/28.png)
    За допомогою віртуального середовища те саме.
    ---
    11. Було вибрано інструмент для перевірки стилю коду після інсталяції і перевірки коду було виправлено помилку .\test.py:5:16: W292 no newline at end of file, а також .\test.py:6:1: W293 blank line contains whitespace:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/29.png)
    ---
    12. Було замінено інтерпретатор і запущено через кнопку Run: ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/30.png)
    ---
    13. Було проведено перевірку вразливостей: ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/31.png)
    ---
    14. Що буде якщо виконати скрипт без активації віртуального середовища? Буде помилка KeyError, бо змінна не підгрузиться.
    ---
    15. Результат виконаних команд:
```bash
PS C:\Users\User\Documents\Project\Programming\oop\lab_6\poetry_lab> poetry new myproject
Created package myproject in myproject

PS C:\Users\User\Documents\Project\Programming\oop\lab_6\poetry_lab> cd myproject
PS C:\Users\User\Documents\Project\Programming\oop\lab_6\poetry_lab\myproject> poetry add requests
Creating virtualenv myproject-py3.13 in C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\venv
Using version ^2.32.5 for requests

Updating dependencies
Resolving dependencies... 

Package operations: 5 installs, 0 updates, 0 removals

  • Installing certifi (2025.10.5)
  • Installing charset-normalizer (3.4.4)
  • Installing idna (3.11)
  • Installing urllib3 (2.6.3)
  • Installing requests (2.32.5)

Writing lock file

PS C:\Users\User\Documents\Project\Programming\oop\lab_6\poetry_lab\myproject> poetry show
certifi            2025.10.5   Python package for providing Mozillas CA Bundle.
charset-normalizer 3.4.4       Encoding detection library.
idna               3.11        Internationalized Domain Names in Applications.
requests           2.32.5      Python HTTP for Humans.
urllib3            2.6.3       HTTP library with thread-safe connection pooling.

PS C:\Users\User\Documents\Project\Programming\oop\lab_6\poetry_lab\myproject> poetry show --tree
requests 2.32.5 Python HTTP for Humans
├── certifi >=2017.4.17
├── charset-normalizer >=2.0.0,<4.0.0
├── idna >=2.5,<4
└── urllib3 >=1.26.0,<3

PS C:\Users\User\Documents\Project\Programming\oop\lab_6\poetry_lab\myproject> poetry remove requests
Removing requests (2.32.5)
Updating dependencies
Resolving dependencies... 

Package operations: 0 installs, 0 updates, 1 removal

  • Removing requests

Updating virtual environment

PS C:\Users\User\Documents\Project\Programming\oop\lab_6\poetry_lab\myproject> poetry update
Updating dependencies
Resolving dependencies... 
All dependencies are up to date. No packages to install, update or remove.
 ```
---
16. За допомогою ШІ було написане останнє завдання з створення flask сайту [тут](app.py) і запущено його: ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/32.png)
---
### Висновок:
- Вивчено, як створювати різні віртуальні середовища та встановлювати в них пакети;
- Мета була досягнута;
- Отримані знання створення і керування віртуальними середовищами;
- Так;
- Так;
- Складностей під час роботи не виникало;
- Формат подобається.
---