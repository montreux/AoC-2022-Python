from typing import List

move_values = {"X": 1, "Y": 2, "Z": 3}
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


def translate_move(move: str):
    return move_meaning[move]


def read_move_data(input: str) -> List[List[str]]:
    move_data = []
    for line in input.splitlines():
        move = line.strip().split()
        move_data.append(move)
    return move_data


# BUG: Forgot to add the score for the move
def score_round(round: List[str]):
    their_move = translate_move(round[0])
    your_move = translate_move(round[1])
    if their_move == your_move:
        return loss_draw_win["D"]
    if their_move == winning_moves[your_move]:
        return loss_draw_win["W"]
    return loss_draw_win["L"]


def score_match(input: str):
    move_data = read_move_data(input)
    total_score = 0
    for round in move_data:
        total_score += score_round(round)
    return total_score
