# number = int(input("Введіть число від 1 до 100: "))

# if 1 <= number <= 100:
#     print("Число правильне!")
# else:
#     print("Помилка: число має бути від 1 до 100.")

import unittest


def count_vowels(text: str) -> int:
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    return sum(1 for char in text if char in vowels)


class TestCountVowels(unittest.TestCase):

    def test_normal_text(self):
        self.assertEqual(3, count_vowels("Привіт"))

    def test_another_text(self):
        self.assertEqual(4, count_vowels("Україна"))

    def test_empty_string(self):
        self.assertEqual(0, count_vowels(""))

    def test_digits(self):
        self.assertEqual(0, count_vowels("123456789"))

    def test_ukrainian_letters(self):
        self.assertEqual(6, count_vowels("АЕЄИІЇ"))


if __name__ == "__main__":
    unittest.main()