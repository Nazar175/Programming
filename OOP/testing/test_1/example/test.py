import unittest

from unittest.mock import patch

from app import Figure, get_number


class TestFigure(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = Figure("квадрат", 5)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    def test_square_angles(self):
        figure = Figure("квадрат", 5)
        self.assertEqual(4, figure.get_angles)

    def test_rectangle_angles(self):
        figure = Figure("прямокутник", 5)
        self.assertEqual(4, figure.get_angles)

    def test_triangle_angles(self):
        figure = Figure("трикутник", 5)
        self.assertEqual(3, figure.get_angles)

    def test_all_figure_types(self):
        figures = [
            ("квадрат", 4),
            ("прямокутник", 4),
            ("трикутник", 3)
        ]

        for figure_type, expected_angles in figures:
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 5)
                self.assertEqual(expected_angles, figure.get_angles)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_zero_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", -5)

    @patch("builtins.input", return_value="5")
    def test_input(self, mock_input):
        self.assertEqual("5", get_number())
        mock_input.assert_called_once_with("Введіть число: ")


if __name__ == "__main__":
    unittest.main(verbosity=2)