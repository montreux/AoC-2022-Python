from enum import Enum
from typing import List


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


move_meaning = {
    "A": Move.ROCK,
    "B": Move.PAPER,
    "C": Move.SCISSORS,
    "X": Move.ROCK,
    "Y": Move.PAPER,
    "Z": Move.SCISSORS,
}

winning_moves = {
    Move.ROCK: Move.SCISSORS,
    Move.PAPER: Move.ROCK,
    Move.SCISSORS: Move.PAPER,
}

move_meaning_part_two = {
    "X": Result.WIN,
    "Y": Result.DRAW,
    "Z": Result.LOSS,
}


def translate_moves(
    opponent_encrypted_move: str, player_encrypted_move: str, part: int
):
    opponent_move = move_meaning[opponent_encrypted_move]
    if part == 2:
        desired_result = move_meaning_part_two[player_encrypted_move]
        if desired_result == Result.DRAW:
            return (opponent_move, opponent_move)

        if desired_result == Result.WIN:
            return (opponent_move, winning_moves[opponent_move])

        if desired_result == Result.LOSS:
            return (opponent_move, winning_moves[winning_moves[opponent_move]])

    # Default to part 1 logic
    player_move = move_meaning[player_encrypted_move]

    return (opponent_move, player_move)


def read_move_data(input: str) -> List[List[str]]:
    move_data: List[List[str]] = []
    for line in input.splitlines():
        move = line.strip().split()
        move_data.append(move)
    return move_data


def score_outcome(opponent_move: Move, player_move: Move) -> int:
    if opponent_move == player_move:
        return Result.DRAW.value
    if opponent_move == winning_moves[player_move]:
        return Result.WIN.value
    return Result.LOSS.value


def score_round(round: List[str], part: int):
    opponent_encrypted_move, player_encrypted_move = round
    [opponent_move, player_move] = translate_moves(
        opponent_encrypted_move, player_encrypted_move, part
    )
    outcome_score = score_outcome(opponent_move, player_move)
    total_score = outcome_score + player_move.value
    return total_score


def score_match(input: str, part: int = 1):
    move_data = read_move_data(input)
    total_score = 0
    for round in move_data:
        total_score += score_round(round, part)
    return total_score
