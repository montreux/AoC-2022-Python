import unittest

from day02_data import EXAMPLE_INPUT
from day02 import score_match


class TestElfRockPaperScissors(unittest.TestCase):
    def test_score_round_part_one_example_data(self):
        expected_output = 15
        self.assertEqual(score_match(EXAMPLE_INPUT), expected_output)


if __name__ == "__main__":
    unittest.main()
