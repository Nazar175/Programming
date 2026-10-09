# Звіт до роботи
## Тема: Тестування з бібліотекою pytest
### Мета роботи: Навчитися писати тести для програм на Python з використанням бібліотеки pytest.

---
## Виконання роботи:

Посилання на файл з виконаними матеріалами лекцій [тут](2_lab)
Скріншот виконання тестів з бібліотекою pytest по лекції: ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/60.png)

* Результати виконання завдання:
    1. Добавлено тести параметризації, неправильного типу та кожного неправильного значення довжини і запущено усі тести:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/61.png)
    2. Запущено тести лише з маркером "unit":![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/62.png)
    3. Зроблено навмисну помилку щоб зламати один тест і запустив pytest -x --tb=short у результаті тестування зупинилося після першого ж проваленого тесту:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/63.png)
    ---
    Сама програма з виконаними завданнями [тут](02_pytest)
    ---
1. Команда встановлення pytest
python -m pip install pytest
2. Результат запуску тестів

Команда запуску:

python -m pytest -v

Результат: усі тести пройшли успішно (passed).

3. Різниця між unittest.TestCase та pytest

У unittest тести створюються як методи класу, що успадковує unittest.TestCase, а для перевірок використовуються спеціальні методи, наприклад self.assertEqual(). У pytest можна використовувати звичайні функції з назвою test_ та оператор assert. Pytest також підтримує параметризацію і fixtures.

4. Приклад використання параметризації
```python
import pytest
from app import Figure

@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    assert Figure(figure_type, 1).type == figure_type
```
Цей тест перевіряє всі дозволені типи фігур за допомогою однієї функції.
---
### Висновок:
- Написав перші тести з бібліотекою pytest і перевірив їх роботу;
- Мета була досягнута;
- Отримані знання роботи з тестами з бібліотекою pytest будуть корисні для подальшого навчання та роботи;
- Так;
- Так;
- Складностей під час роботи не виникало;
- Формат подобається.
---