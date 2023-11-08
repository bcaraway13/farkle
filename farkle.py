import random

WINNING_SCORE = 10000
number_of_players = 0
players = []

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.farkles_in_a_row = 0

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
    number_of_players = int(input("Enter the number of players: "))

    if number_of_players < 2:
        print("Error: Minimum number of players is 2")
        exit()
        
    for player in range(number_of_players):
        player_name = get_player_names(player)
        players.append(Player(player_name))


def get_player_names(player_number):
    return input(f"Enter player {player_number + 1}'s name: ").title()



def player_turn(player):
    turn_score = 0
    remaining_dice = 6

    while True:
        dice = sorted(roll_dice(remaining_dice))
        print(f"{player.name} rolled: {dice}")
        score = calculate_score(dice)
        if score == 0:
            return 0
        turn_score += score
        remaining_dice = calculate_remaining_dice(dice)
        
    return turn_score


def play_game():
    initialize_game()
    player_scores = [player.score for player in players]
    current_player = players[0]
    print(players)

    while max(player_scores) < WINNING_SCORE:
        turn_score = player_turn(current_player)
        current_player.score += turn_score

        if turn_score > 0:
            current_player.farkles_in_a_row = 0
        else:
            current_player.farkles_in_a_row += 1
            if current_player.farkles_in_a_row == 3:
                print(f"{current_player.name} is out!")
                players.remove(current_player)


        if current_player.score >= WINNING_SCORE:
            print(f"{current_player.name} wins!")
            break
        current_player = players[(players.index(current_player) + 1) % len(players)]
        if current_player == players[0]:
            for player in players:
                print(f"{player.name}: {player.score}")
            
        


play_game()    
