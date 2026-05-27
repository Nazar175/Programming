from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from dotenv import load_dotenv
from google.adk import Agent

load_dotenv()


class Person(ABC):
    """Abstract base class for every person in the academic system."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name.strip()
        self.age = age

    @abstractmethod
    def get_role(self) -> str:
        """Return the academic role of the person."""


class Student(Person):
    """Stores and analyzes a student's grades."""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name=name, age=age)
        self.__grades: list[float] = []

    def add_grade(self, grade: float) -> None:
        numeric_grade = float(grade)
        if numeric_grade < 0 or numeric_grade > 100:
            raise ValueError("Оцінка має бути в межах від 0 до 100.")
        self.__grades.append(numeric_grade)

    def average(self) -> float:
        if not self.__grades:
            return 0.0
        return round(sum(self.__grades) / len(self.__grades), 2)

    def min_grade(self) -> float:
        if not self.__grades:
            return 0.0
        return min(self.__grades)

    def max_grade(self) -> float:
        if not self.__grades:
            return 0.0
        return max(self.__grades)

    def get_role(self) -> str:
        return "Студент"

    @property
    def grades(self) -> tuple[float, ...]:
        """Read-only snapshot of grades for safe external access."""
        return tuple(self.__grades)


class Teacher(Person):
    """Represents a teacher who can evaluate students."""

    def __init__(self, name: str, age: int, subject: str) -> None:
        super().__init__(name=name, age=age)
        self.subject = subject.strip()

    def get_role(self) -> str:
        return f"Викладач предмета {self.subject}"

    def evaluate(self, student: Student, grade: float) -> None:
        student.add_grade(grade)


def describe_person(person: Person) -> str:
    """Demonstrates polymorphism by working with any Person subclass."""
    return f"{person.name}, {person.age} років, роль: {person.get_role()}"


def determine_letter_grade(average_score: float) -> str:
    if average_score >= 90:
        return "A"
    if average_score >= 75:
        return "B"
    if average_score >= 60:
        return "C"
    return "F"


def calculate_grade(name: str, scores: list[float]) -> dict[str, Any]:
    """
    Calculate a student's academic performance summary.

    Args:
        name: Student name.
        scores: List of numeric grades.

    Returns:
        A dictionary with student statistics and a letter grade.
    """
    cleaned_name = name.strip()
    if not cleaned_name:
        return {
            "student": "",
            "average": 0.0,
            "min": 0.0,
            "max": 0.0,
            "letter_grade": "F",
        }

    if not scores:
        return {
            "student": cleaned_name,
            "average": 0.0,
            "min": 0.0,
            "max": 0.0,
            "letter_grade": "F",
        }

    student = Student(name=cleaned_name, age=18)

    # Demonstrates polymorphism and inheritance in a simple academic context.
    mentor = Teacher(name="Пані Коваленко", age=40, subject="успішність студентів")
    describe_person(student)
    describe_person(mentor)

    for score in scores:
        student.add_grade(score)

    average_score = student.average()
    return {
        "student": student.name,
        "average": average_score,
        "min": student.min_grade(),
        "max": student.max_grade(),
        "letter_grade": determine_letter_grade(average_score),
    }


root_agent = Agent(
    name="student_success_agent",
    model="gemini-2.5-flash",
    description="Освітній асистент для аналізу успішності студентів.",
    instruction="""
Ти освітній асистент, який допомагає аналізувати успішність студентів.

Правила роботи:
- Завжди відповідай українською мовою.
- Якщо користувач просить порахувати успішність, середній бал, мінімальну або максимальну оцінку, обов'язково використай інструмент calculate_grade.
- Після використання інструмента коротко поясни результат людською мовою.
- Обов'язково вкажи середній бал, мінімальну оцінку, максимальну оцінку та літерний рейтинг.
- Дай 2-3 короткі поради щодо покращення успішності.
- Якщо середній бал 90 і вище, похвали студента і порадь підтримувати рівень.
- Якщо середній бал від 75 до 89.99, порадь зміцнити стабільність результатів.
- Якщо середній бал від 60 до 74.99, порадь повторити теми, де є прогалини.
- Якщо середній бал нижче 60, порадь почати з базового повторення і звернутися по допомогу до викладача.
- Якщо в запиті бракує імені або списку оцінок, попроси користувача уточнити дані.
- Не вигадуй оцінки, яких користувач не надав.
""",
    tools=[calculate_grade],
)
