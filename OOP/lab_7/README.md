# Звіт до роботи
## Тема: AI Агенти з Google ADK
### Мета роботи: Навчитись створювати AI агентів з використанням Google ADK (Python) та Poetry для управління залежностями проекту

---
## Виконання роботи:

У звязку з тим що завдання з лекції були такіж як у завданні, я зробив їх один раз і для лекції і для лабараторної роботи.

* Результати виконання завдання:
    1. Актуальна версія Python і Poetry:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/33.png)
    2. Файл poetry.lock потрібен для відтворення точного отримання залежностей, бібліотек:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/34.png)
    3. Версія Google ADK:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/35.png)
    4. Основні команди в Google ADK:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/36.png)
    5. Agent клас - це базовий клас для створення AI агентів, який надає основні функції та структуру для розробки агентів з різними можливостями та поведінкою. Параметр tools потрібен для визначення інструментів, які агент може використовувати для виконання своїх завдань. Функція get_current_time використовується для отримання поточного часу, що може бути корисним для агентів, які потребують інформації про час для виконання своїх завдань або прийняття рішень.
    6. Результат діалогу з агентом де запитано поточний час:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/37.png)
    7. Поставлено ще більше питань про час агенту:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/38.png)
    8. Протестовані AI агента через веб інтерфейс:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/39.png)
    9. Протестовано агента задавши три питання на які він відповів вірно:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/40.png)
    10. Результат додавання ще одного математичного інструменту:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/41.png)
    11. Підтвердження роботи студенського агента через консоль:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/42.png)
    12. Дальше потрібно було створити агента який буде писати історії залежно від базових поставлених налаштувань, але у звязку з тим що версія ADK оновилася тепер ці параметри задавати неможна, тому я зупинився на створенні самого агента без привязки до налаштувань, але він все одно може писати історії:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/43.png)
    13. Результат роботи агента який запамятовує інформацію сказану користувачем:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/44.png)
    14. Настипним етапом було логування агента але чомусь я не зміг запустити дану функцію, через її відсутність у даному ADK:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/45.png)
    15. Структура папок та файлів проекту:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/46.png)
    16. Створено власного покращеного студенського агента використовуючи поради, я написав чіткі інструкції для агента щоб він відповідав прямо як є, додав якісні інструменти для базових розрахунків і добавив валідацію вводу: 
    ```bash
        from google.adk.agents.llm_agent import Agent
    def calculate_grade(score: float, max_score: float) -> dict:
        """
        Обчислює оцінку у відсотках.
        Args:
            score: отримані бали
            max_score: максимальна кількість балів
        Returns:
            dict: результат обчислення або помилка
        """
        if max_score <= 0:
            return {"status": "error", "error": "Максимальний бал має бути більше 0", "result": None}
        percentage = (score / max_score) * 100
        return {
            "status": "success",
            "score": score,
            "max_score": max_score,
            "percentage": round(percentage, 2)
        }
    def generate_quiz(topic: str, difficulty: str = "easy") -> dict:
        """
        Генерує простий тест по темі.
        Args:
            topic: тема тесту
            difficulty: складність (easy, medium, hard)
        Returns:
            dict: список питань
        """
        if difficulty not in ["easy", "medium", "hard"]:
            return {
                "status": "error",
                "error": "Невірний рівень складності",
                "questions": None
            }
        questions = [
            f"Що таке {topic}?",
            f"Навіщо використовується {topic}?",
            f"Наведіть приклад використання {topic}"
        ]
        return {
            "status": "success",
            "topic": topic,
            "difficulty": difficulty,
            "questions": questions
        }
    def validate_input(text: str) -> dict:
        """
        Перевіряє введений текст.
        Args:
            text: текст користувача
        Returns:
            dict: результат перевірки
        """
        if not text.strip():
            return {"status": "error", "error": "Порожній ввід"}
        if len(text) < 3:
            return {"status": "error", "error": "Занадто короткий текст"}
        return {"status": "success", "message": "Ввід коректний"}
    root_agent = Agent(
        model='gemini-3.1-flash-lite-preview',
        name='study_assistant',
        description="Агент для допомоги студентам у навчанні та підготовці до тестів.",
        instruction="""
        Ти інтелектуальний навчальний помічник.
        Твої завдання:
        - Допомагати студентам розуміти навчальні теми
        - Генерувати прості тести для самоперевірки
        - Обчислювати оцінки
        - Перевіряти введені дані
        - Давати чіткі та зрозумілі пояснення
        Правила:
        - Завжди відповідай українською мовою
        - Використовуй просту та зрозумілу мову
        - Якщо використовуєш інструмент — поясни результат
        - Якщо сталася помилка — поясни її користувачу
        - Форматуй відповідь у Markdown
        Формат відповіді:
        - Пояснення
        - (за потреби) результат інструменту
        """,
        tools=[calculate_grade, generate_quiz, validate_input],
    )
    ```
    17. Створено агента який запамятовує інформацію про користувача на різних сесіях:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/47.png) ![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/48.png)
    18. Результат створення SequentialAgent який виконує завдання послідовно:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/49.png)
    Sequential агенти важливі адже вони задають послідовність виконання завдань, що дозволяє краще організувати роботу агента та забезпечити логічний порядок виконання дій, що може бути критично для досягнення правильного результату.
    19. Результат створення Loop Agent який виконує завдання циклічно:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/50.png)
    Через велике навантаження вдалося лише тричі запустити даних агентів*
    Завершення циклу через exit_loop функцію дозволяє контролювати тривалість виконання циклу, що є важливим для запобігання нескінченних циклів та забезпечення ефективного використання ресурсів.
    20. Результат роботи Parallel Agent який виконує завдання паралельно:![Скріншот](https://raw.githubusercontent.com/Nazar175/Programming/refs/heads/main/picture/51.png)
    Паралельні агенти дозволяють виконувати кілька завдань одночасно, що може значно підвищити ефективність та швидкість виконання, особливо коли завдання не залежать одне від одного. Це швидше за три послідовні завдання, оскільки вони виконуються одночасно, а не по черзі.
    21. Створено Workflow агента, який складається з кількох під агентів, що виконують різні етапи роботи:
```bash
    from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent

    def fetch_from_wikipedia(topic: str) -> dict:
        if not topic.strip():
            return {"status": "error", "error": "Порожня тема"}

        return {
            "status": "success",
            "source": "wikipedia",
            "data": f"Основна інформація про {topic}"
        }


    def fetch_from_blog(topic: str) -> dict:
        return {
            "status": "success",
            "source": "blog",
            "data": f"Практичне використання {topic}"
        }


    def analyze_data(data: str) -> dict:
        """
        Аналізує зібрані дані.

        Args:
            data: текст з даними

        Returns:
            dict
        """
        if not data.strip():
            return {"status": "error", "error": "Немає даних"}

        return {
            "status": "success",
            "analysis": f"Аналіз: {data}"
        }


    def generate_report(analysis: str) -> dict:
        return {
            "status": "success",
            "report": f"Звіт:\n{analysis}"
        }


    def improve_report(report: str) -> dict:
        if len(report) < 50:
            return {
                "status": "retry",
                "report": report + "\n(додано більше деталей...)"
            }

        return {
            "status": "done",
            "report": report + "\n(звіт оптимізовано)"
        }

    parallel_agent = ParallelAgent(
        name="data_collection",
        sub_agents=[
            Agent(
                model="gemini-3.1-flash-lite",
                name="wiki_agent",
                instruction="Отримай інформацію про тему користувача",
                tools=[fetch_from_wikipedia],
            ),
            Agent(
                model="gemini-3.1-flash-lite",
                name="blog_agent",
                instruction="Отримай практичну інформацію про тему",
                tools=[fetch_from_blog],
            ),
        ]
    )

    sequential_agent = SequentialAgent(
        name="processing_pipeline",
        sub_agents=[
            Agent(
                model="gemini-3.1-flash-lite",
                name="analysis_agent",
                instruction="Проаналізуй отримані дані",
                tools=[analyze_data],
            ),
            Agent(
                model="gemini-3.1-flash-lite",
                name="report_agent",
                instruction="Створи звіт",
                tools=[generate_report],
            ),
        ]
    )

    loop_agent = LoopAgent(
        name="improvement_loop",
        sub_agents=[
            Agent(
                model="gemini-3.1-flash-lite",
                name="improver",
                instruction="""
                Покращуй звіт поки він не стане достатньо детальним.
                Якщо звіт хороший — завершуй.
                """,
                tools=[improve_report],
            )
        ],
        max_iterations=5
    )

    root_agent = SequentialAgent(
        name="full_workflow",
        sub_agents=[
            parallel_agent,
            sequential_agent,
            loop_agent
        ]
    )
```
Усі агенти є розділені папках у папці lab_7.
---
### Висновок:
- Вивчено процес створення AI агентів з використанням Google ADK та Poetry для управління залежностями проекту;
- Мета була досягнута;
- Отримані знання роботи з Google ADK та Poetry для створення AI агентів;
- Так;
- Так;
- Складностей під час роботи не виникало;
- Формат подобається.
---