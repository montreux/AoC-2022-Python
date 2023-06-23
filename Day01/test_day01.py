import unittest

from day01_data import EXAMPLE_INPUT

# Assume that the required code is in a file called 'elf_calories.py'
from day01 import read_calorie_data, get_index_of_elf_carrying_most_calories, part_one, get_calorie_totals, part_two, Elf

class TestElfCalories(unittest.TestCase):

    def test_read_calorie_data(self):
        expected_output = [[1000,2000,3000],[4000], [5000,6000], [7000,8000,9000], [10000]]
        self.assertEqual(read_calorie_data(EXAMPLE_INPUT), expected_output)

    def test_get_index_of_elf_carrying_most_calories(self):
        input_data = EXAMPLE_INPUT
        expected_output = (3, 24000)
        self.assertEqual(get_index_of_elf_carrying_most_calories(input_data), expected_output)

    def test_get_calorie_totals(self):
        input_data = "\n".join(["100", "200", "", "150", "250"])
        expected_output = [Elf(2, 400), Elf(1, 300)]
        self.assertEqual(get_calorie_totals(input_data), expected_output)

    def test_part_one(self):
        expected_output = "Elf 4 carried 24000 calories"
        self.assertEqual(part_one(EXAMPLE_INPUT), expected_output)

    def test_part_two(self):
        expected_output = "Sum of top three elves calories: 45000"
        self.assertEqual(part_two(EXAMPLE_INPUT), expected_output)

if __name__ == "__main__":
    unittest.main()
