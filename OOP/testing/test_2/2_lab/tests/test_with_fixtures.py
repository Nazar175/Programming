import pytest
from game import CardGame

@pytest.fixture
def card_game():
    """Фікстура для створення об'єкта CardGame"""
    return CardGame()

def test_incorrect_interraction_with_fixture(card_game):
    """Тестуємо функцію incorrect_interraction на об'єкті класу CardGame з використанням фікстури"""

    for i in [0, 1, 5, 10]:
        assert card_game.incorrect_interraction(i) == i * 2, f"Очікуваний результат: {i * 2}, отриманий результат: {card_game.incorrect_interraction(i)}"

    for i in [-1, -5, -10]:
        with pytest.raises(ValueError):
            card_game.incorrect_interraction(i)

    for i in ["string", 3.14, None, [], {}]:
        with pytest.raises(TypeError):
            card_game.incorrect_interraction(i)