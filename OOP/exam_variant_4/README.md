# Варіант 4. Агент успішності студентів

## Завдання OOP
Реалізуйте систему обліку успішності:

### Абстрактний клас Person
- атрибути: `name`, `age`
- абстрактний метод: `get_role() -> str`

### Клас Student (успадковує Person)
- зберігає оцінки у приватному списку `__grades` (інкапсуляція)
- методи:
  - `add_grade(grade: float)`
  - `average() -> float`
  - `min_grade() -> float`
  - `max_grade() -> float`
  - `get_role()`

### Клас Teacher (успадковує Person)
- атрибут: `subject`
- методи:
  - `get_role()`
  - `evaluate(student: Student, grade: float)` — додає оцінку студенту через `student.add_grade()`

### AI-агент
- Інструмент (tool): функція `calculate_grade(name: str, scores: list) -> dict`
  - всередині функції створює об'єкт `Student(name, age=18)`
  - додає кожну оцінку зі списку через `add_grade()`
  - викликає `average()`, `min_grade()`, `max_grade()` для формування відповіді
  - `letter_grade` визначається за шкалою:
    - `90+ → A`
    - `75+ → B`
    - `60+ → C`
    - нижче → `F`
  - повертає:
    - `{"student": ..., "average": ..., "min": ..., "max": ..., "letter_grade": ...}`

- Промпт агента:
  - агент є освітнім асистентом
  - розраховує середній бал
  - визначає рейтинг
  - дає поради щодо покращення успішності
  - відповідає українською мовою

- Демонстрація:
  - поставте агенту 3 запитання з іменами студентів та різними наборами оцінок.

## Результат виконання завдання
Приклад запитання та відповіді агента:

![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/51.png)

![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/52.png)

![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/53.png)