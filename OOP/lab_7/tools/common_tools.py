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