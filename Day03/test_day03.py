from typing import List
import unittest

from day03_data import EXAMPLE_INPUT, PUZZLE_INPUT
from day03 import RucksackData


class TestRucksackData(unittest.TestCase):
    def test_from_string(self):
        all_rucksack_data = RucksackData.from_string(EXAMPLE_INPUT)
        self.assertEqual(len(all_rucksack_data), 6)
        self.assertEqual(all_rucksack_data[0].first_half, "vJrwpWtwJgWr")
        self.assertEqual(all_rucksack_data[0].second_half, "hcsFMMfFFhFp")
        self.assertEqual(all_rucksack_data[-1].first_half, "CrZsJsPPZsGz")
        self.assertEqual(all_rucksack_data[-1].second_half, "wwsLwLmpwMDw")

    def test_find_duplicate_item(self):
        rucksack_data = RucksackData("vJrwpWtwJgWr", "hcsFMMfFFhFp")
        expected_output = "p"
        self.assertEqual(rucksack_data.find_duplicate_item(), expected_output)

    def test_find_duplicate_item_no_duplicates(self):
        rucksack_data = RucksackData("vJrwpWtwJgWr", "CRZsjsPPZsGz")
        expected_output = ""
        self.assertEqual(rucksack_data.find_duplicate_item(), expected_output)

    def test_score_duplicate(self):
        all_rucksack_data = RucksackData.from_string(EXAMPLE_INPUT)

        all_scores: List[int] = []
        for rucksack_data in all_rucksack_data:
            all_scores.append(rucksack_data.score_duplicate())

        self.assertEqual(all_scores, [16, 38, 42, 22, 20, 19])
        self.assertEqual(sum(all_scores), 157)

    def test_puzzle_data_score_duplicate(self):
        all_rucksack_data = RucksackData.from_string(PUZZLE_INPUT)

        all_scores: List[int] = []
        for rucksack_data in all_rucksack_data:
            all_scores.append(rucksack_data.score_duplicate())

        self.assertEqual(sum(all_scores), 8401)

    def test_score_badges(self):
        all_rucksack_data = RucksackData.from_string(EXAMPLE_INPUT)
        total_badge_scores = RucksackData.score_badges(all_rucksack_data)
        self.assertEqual(total_badge_scores, 70)

    def test_puzzle_data_score_badges(self):
        all_rucksack_data = RucksackData.from_string(PUZZLE_INPUT)
        total_badge_scores = RucksackData.score_badges(all_rucksack_data)
        self.assertEqual(total_badge_scores, 2641)


if __name__ == "__main__":
    unittest.main()
