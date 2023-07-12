from __future__ import annotations
from typing import List


class RucksackData:
    def __init__(self, first_half: str, second_half: str):
        self.first_half = first_half
        self.second_half = second_half

    def find_duplicate_item(self):
        unique_items_in_first_half = set(self.first_half)

        for item in self.second_half:
            if item in unique_items_in_first_half:
                return item

        return ""

    @classmethod
    def convert_char_to_number(cls, c: str):
        if len(c) == 0:
            return 0
        elif len(c) > 1:
            raise ValueError("Input character must be a single character.")

        if "a" <= c <= "z":
            return ord(c) - ord("a") + 1
        elif "A" <= c <= "Z":
            return ord(c) - ord("A") + 27
        else:
            raise ValueError("Input character must be an English letter.")

    def score_duplicate(self):
        duplicate_item = self.find_duplicate_item()
        return self.convert_char_to_number(duplicate_item)

    def find_badge(self, other_a: RucksackData, other_b: RucksackData):
        my_unique_items = set(self.first_half + self.second_half)

        for item in my_unique_items:
            is_in_other_a = item in other_a.first_half + other_a.second_half
            is_in_other_b = item in other_b.first_half + other_b.second_half

            if is_in_other_a and is_in_other_b:
                return item

        return ""

    @classmethod
    def score_badges(cls, all_rucksack_data: List[RucksackData]):
        # split the list into groups of 3
        groups = [
            all_rucksack_data[i : i + 3] for i in range(0, len(all_rucksack_data), 3)
        ]

        group_badges: List[str] = []
        for group in groups:
            group_badges.append(cls.find_badge(group[0], group[1], group[2]))

        group_badge_scores = [
            cls.convert_char_to_number(badge) for badge in group_badges
        ]

        return sum(group_badge_scores)

    @classmethod
    def from_string(cls, input: str):
        all_rucksack_data: List[RucksackData] = []

        for line in input.splitlines():
            clean_line = line.strip()

            # split the string into two halves
            half = len(line) // 2
            first_half = clean_line[:half]
            second_half = clean_line[half:]

            all_rucksack_data.append(cls(first_half, second_half))

        return all_rucksack_data
