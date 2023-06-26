import unittest

from day02_data import EXAMPLE_INPUT, PUZZLE_INPUT
from day02 import score_match


class TestElfRockPaperScissors(unittest.TestCase):
    def test_score_round_part_one_example_data(self):
        expected_output = 15
        self.assertEqual(score_match(EXAMPLE_INPUT), expected_output)

    def test_score_round_part_one_puzzle_data(self):
        expected_output = 11906
        self.assertEqual(score_match(PUZZLE_INPUT), expected_output)

    def test_score_round_part_two_example_data(self):
        expected_output = 12
        self.assertEqual(score_match(EXAMPLE_INPUT, part=2), expected_output)


if __name__ == "__main__":
    unittest.main()
