
import pytest

from app import Figure


@pytest.fixture
def square():
    return Figure("квадрат", 5)


@pytest.fixture
def figure_length_10():
    return Figure("квадрат", 10)


@pytest.fixture(scope="module")
def allowed_figures_module():
    return Figure.FIGURES


@pytest.mark.unit
def test_triangle_type():
    assert Figure("трикутник", 4).type == "трикутник"


@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    assert Figure(figure_type, 1).type == figure_type


@pytest.mark.unit
def test_square_length(square):
    assert square.get_figure_length == 5


def test_figure_length_10(figure_length_10):
    assert figure_length_10.length == 10
    assert figure_length_10.get_figure_length == 10
    assert figure_length_10.type == "квадрат"


@pytest.mark.parametrize(
    "figure_type",
    ["коло", "ромб", ""]
)
def test_invalid_figure(figure_type):
    with pytest.raises(AssertionError, match="Невідомий тип фігури"):
        Figure(figure_type, 1)


@pytest.mark.parametrize("length", [0, -1, -10])
def test_invalid_length(length):
    with pytest.raises(
        AssertionError,
        match="Довжина має бути більшою за 0!"
    ):
        Figure("квадрат", length)


def test_module_fixture_contains_square(allowed_figures_module):
    assert "квадрат" in allowed_figures_module


def test_module_fixture_contains_triangle(allowed_figures_module):
    assert "трикутник" in allowed_figures_module