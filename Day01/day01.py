from day01_data import EXAMPLE_INPUT, PUZZLE_INPUT

# read the data from EXAMPLE_INPUT and convert it a list of lists of integers. Blank lines in the input are separators.
def read_calorie_data(input):
    all_calories = []
    current_calories = []
    for line in input.splitlines():
        if line == "":
            all_calories.append(current_calories)
            current_calories = []
            continue
        current_calories.append(int(line))

    # add the last set of calories
    all_calories.append(current_calories)

    return all_calories


def get_index_of_elf_carrying_most_calories(input):
    calorie_data = read_calorie_data(input)
    max_calories = -1
    max_calories_index = -1
    for elf_index in range(len(calorie_data)):
        calories_for_this_elf = sum(calorie_data[elf_index])

        if calories_for_this_elf > max_calories:
            max_calories = calories_for_this_elf
            max_calories_index = elf_index

    return max_calories_index, max_calories

def part_one(input):
    elf_index, elf_calories = get_index_of_elf_carrying_most_calories(input)
    print("Elf {} carried {} calories".format(elf_index+1, elf_calories))


print("Part one - example data:")
part_one(EXAMPLE_INPUT)

print("\nPart one - puzzle data:")
part_one(PUZZLE_INPUT)

from typing import List


class Elf:
    def __init__(self, index: int, calories: int):
        self.index = index
        self.calories = calories

    def __repr__(self):
        return f"Elf {self.index} with {self.calories} calories"
    
    def __lt__(self, other):
        return self.calories < other.calories


def get_calorie_totals(input: List[str]) -> List[Elf]:
    calorie_data = read_calorie_data(input)
    calorie_totals = []
    for elf_index, elf_calories in enumerate(calorie_data):
        calories_for_this_elf = sum(elf_calories)
        calorie_totals.append(Elf(elf_index+1, calories_for_this_elf))

    # sort the list of elves by their calorie totals, descending
    calorie_totals.sort()
    calorie_totals.reverse()

    return calorie_totals


def part_two(input: List[str]):
    elf_calorie_totals = get_calorie_totals(input)

    for top_elf in elf_calorie_totals[:3]:
        print(top_elf)

    sum_of_top_three = sum([elf.calories for elf in elf_calorie_totals[:3]])
    print(f"Sum of top three elves calories: {sum_of_top_three}")


print("\nPart two - example data:")
part_two(EXAMPLE_INPUT)

print("\nPart two - puzzle data:")
part_two(PUZZLE_INPUT)