from typing import List

move_values = {"Rock": 1, "Paper": 2, "Scissors": 3}
loss_draw_win = {"L": 0, "D": 3, "W": 6}
move_meaning = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
winning_moves = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}
move_meaning_part_two = {
    "X": "W",
    "Y": "D",
    "Z": "L",
}


def translate_moves(their_encrypted_move: str, your_encrypted_move: str, part: int):
    their_move = move_meaning[their_encrypted_move]
    if part == 2:
        desired_result = move_meaning_part_two[your_encrypted_move]
        if desired_result == "D":
            return [their_move, their_move]

        if desired_result == "W":
            return [their_move, winning_moves[their_move]]

        if desired_result == "L":
            return [their_move, winning_moves[winning_moves[their_move]]]

    # Default to part 1 logic
    your_move = move_meaning[your_encrypted_move]

    return [their_move, your_move]


def read_move_data(input: str) -> List[List[str]]:
    move_data: List[List[str]] = []
    for line in input.splitlines():
        move = line.strip().split()
        move_data.append(move)
    return move_data


def score_outcome(their_move: str, your_move: str):
    if their_move == your_move:
        return loss_draw_win["D"]
    if their_move == winning_moves[your_move]:
        return loss_draw_win["W"]
    return loss_draw_win["L"]


def score_round(round: List[str], part: int):
    [their_move, your_move] = translate_moves(round[0], round[1], part)
    outcome_score = score_outcome(their_move, your_move)
    total_score = outcome_score + move_values[your_move]
    return total_score


def score_match(input: str, part: int = 1):
    move_data = read_move_data(input)
    total_score = 0
    for round in move_data:
        total_score += score_round(round, part)
    return total_score
