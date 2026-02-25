# Звіт до роботи
## Тема: Знайомство з ООП
### Мета роботи: Начитись використовувати основні принципи ООП, розглянути кострукції побудови класу та створення обєтів та навчитись працювати з ними.

---
### Виконання роботи
* Результати виконання завдання
    1. Що вивела програма в першому завданні: ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/15.png)

- Також було модифіковано код і додано ім'я, сама програма [тут](class.py)
- Результат пропрацьовування лекції [тут](note.ipynb) і [тут](game.py)
---
* Відповіді на питання
    1. Бо None означає “немає імені”, тому замість нього створюється об’єкт із ім’ям Anonymous.
    1. Текст змінюється у рядку print() або return всередині методу say_hello(), ось дописаний код:
    ```python
    class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Привіт, мене звати {self.name}!")  # ← ось тут можна змінити текст
    ```
    1. Потрібно додати метод:
    ```python
    def count_letters(self): return len(self.name)
    ```
    1. У списку (list) імена повторюються, а у множині (set) — дублікати автоматично видаляються, тому кількість менша.
    1. Додайте .capitalize() у конструкторі, щоб перша літера була великою:
    ```python
    class Person:
    def __init__(self, name):
        self.name = name.capitalize()
    ```
    1. Додайте параметр domain у метод create_email, і використайте його після @.
    ```python
    class Person:
    def __init__(self, name):
        self.name = name.capitalize()

    def create_email(self, domain="gmail.com"):
        return f"{self.name.lower()}@{domain}"
    ```
    1. Додай перевірку if not name.isalpha(): raise ValueError("...") у конструкторі:
    ```python
    class Person:
    def __init__(self, name):
        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        self.name = name.capitalize()
    ```
    1. Додай властивість @property full_name, яка повертає рядок f"User #{self.user_id}: {self.name} ({self.email})":
    ```python
    class Person:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name.capitalize()
        self.email = email

    @property
    def full_name(self):
        return f"User #{self.user_id}: {self.name} ({self.email})"
    ```
    1. У методі відкрий файл у режимі "a" і запиши self.full_name + "\n" у нього:
    ```python
    class Person:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name.capitalize()
        self.email = email

    @property
    def full_name(self):
        return f"User #{self.user_id}: {self.name} ({self.email})"

    def save_to_file(self, filename="users.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")
    ```
---
### Висновок:
- У роботі було освоєно знання про основи ООП і вміння правильно застосовувати основні принципи ООП;
- Мета була досягнута;
- Отримані знання про основи ООП;
- Так;
- Так; 
- Складностей під час роботи не виникало;
- Формат подобається.
---