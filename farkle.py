import random

WINNING_SCORE = 10000

def roll_dice(number_of_dice):
    return [random.randint(1, 6) for _ in range(number_of_dice)]


def calculate_remaining_dice(dice):
    remaining_dice = len(dice)
    ...
    return remaining_dice


def calculate_score(dice):
    score = 0
    ...
    return score


def initialize_game():
    global number_of_players
    number_of_players = int(input("Enter the number of players: "))
    if number_of_players < 2:
        print("Error: Minimum number of players is 2")
        exit()
    players = {"name":}


def player_turn(player):
    score_for_turn = 0
    remaining_dice = 6

    while True:
        dice = roll_dice(remaining_dice)
        print(f"Player {player + 1} rolled: {dice}")
        score = calculate_score(dice)
        if score == 0:
            return 0 # Farkle, end turn
        score_for_turn += score
        remaining_dice = calculate_remaining_dice(dice)


def play_game():
    initialize_game()
    player_scores = [0] * number_of_players
    current_player = 0

    while max(player_scores) < WINNING_SCORE:
        turn_score = player_turn(current_player)
        player_scores[current_player] += turn_score
        if player_scores[current_player] >= WINNING_SCORE:
            print(f"Player {current_player + 1} wins!")
            break
        current_player = (current_player + 1) % number_of_players
        if current_player == 0:
            print(f"Scores: {player_scores}")


play_game()    






