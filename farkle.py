import random
import os

WINNING_SCORE = 10000
number_of_players = 0
players = []

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.farkles_in_a_row = 0

class Score:
    def __init__(self, name, points, dice_banked):
        self.name = name
        self.points = points
        self.dice_banked = dice_banked
           

class Die:
    def __init__(self):
        self.value = None
        self.selected = False

    def roll(self):
        self.value = random.randint(1, 6)


class Roll:
    def __init__(self, number_of_dice):
        if 1 <= number_of_dice <= 6:
            self.dice = [Die() for _ in range(number_of_dice)]
        else:
            raise ValueError("Number of dice must be between 1 and 6")
        
        
    def dice(self):
        return [die.value for die in self.dice]
    
    def roll_all(self):
        for die in self.dice:
            die.roll()
        

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def calculate_remaining_dice(dice, scores):
    remaining_dice = len(dice)
    ...
    return remaining_dice


def calculate_score(dice):
    roll_score = 0
    dice_banked = 0
    possible_scores = check_for_scores(dice)
    possible_scores.sort(key=lambda x: x.points, reverse=True)
    
    if len(possible_scores) == 0:
        print("No scoring dice, Farkle!")
        return roll_score, dice_banked
    
    print("------Scores------")
    for score in possible_scores:
        print("|", score.name, "-", score.points)
        roll_score += score.points
        dice_banked += score.dice_banked
    print("------------------")
    
    return roll_score, dice_banked


def check_for_scores(Roll):
    # create score objects
    
    three_of_a_kind = Score("Three-of-a-Kind", 100, 3)
    four_of_a_kind = Score("Four-of-a-Kind", 1000, 4)

    dice = [die.value for die in Roll.dice]
    possible_scores = []
    pairs = 0
    triplets = 0
    four_of_a_kinds = 0
    
    for i in range(1,7):
        # Check for pairs
        if dice.count(i) == 2 and i != 1:
            pairs += 1

        # Check for 3 of a kind
        if dice.count(i) == 3:
            if i == 1:
                possible_scores.append(Score("Three Ones", 1000, 3))
            else:
                possible_scores.append(Score("Three-of-a-Kind", 100 * i, 3))
            triplets += 1

        # Check for 4 of a kind
        elif dice.count(i) == 4:
            possible_scores.append(Score("Four-of-a-Kind", 1000, 4))
            four_of_a_kinds += 1

        # Check for 5 of a kind
        elif dice.count(i) == 5:
            possible_scores.append(Score("Five-of-a-Kind", 2000, 5))

        # Check for 6 of a kind
        elif dice.count(i) == 6:
            possible_scores.append(Score("Six-of-a-Kind", 3000, 6))
            return possible_scores

    # Check for 1-6 straight
    if sorted(dice) == [1, 2, 3, 4, 5, 6]:
        possible_scores.append(Score("Straight", 1500, 6))
        return possible_scores

    # Check for 3 pairs
    if pairs == 3:
        possible_scores.append(Score("Three Pairs", 1500, 6))
        return possible_scores

    # Check for 4 of a kind plus a pair
    if four_of_a_kinds == 1 and pairs == 1:
        possible_scores.append(Score("Four-of-a-Kind + Pair", 1500, 6))

    # Check for 2 triplets
    if triplets == 2:
        possible_scores.append(Score("Two Triplets", 2500, 6))

    # Check for ones scores
    if 1 in dice and triplets != 2 and pairs != 3:
        if dice.count(1) < 3:
            ones_banked = 0
            if dice.count(1) > 1 and len(possible_scores) == 0:
                try:
                    ones_banked = int(input(f"How many ones would you like to bank?  0-{dice.count(1)}: "))
                except ValueError:
                    print("Error: Invalid input")
            if dice.count(1) == 1:
                ones_banked = 1
            if ones_banked and 0 < ones_banked <= dice.count(1):
                possible_scores.append(Score("Ones", ones_banked * 100, ones_banked))
                

    # Check for fives scores
    if 5 in dice and triplets != 2 and pairs != 3:
        if dice.count(5) < 3:
            fives_banked = 0
            if len(possible_scores) > 0 or dice.count(5) > 1:
                try:
                    fives_banked = int(input(f"How many fives would you like to bank?  0-{dice.count(5)}: "))
                except ValueError:
                    print("Error: Invalid input")
            elif dice.count(5) == 1 and len(possible_scores) == 0:
                fives_banked = 1

            if fives_banked and 0 < fives_banked <= dice.count(5):
                possible_scores.append(Score("Fives", 50 * fives_banked, fives_banked))
            
    return possible_scores


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
    roll_number = 1

    print("\n----------------------------------------\n")
    while True:
        roll = Roll(remaining_dice)
        roll.roll_all()
        dice = [die.value for die in roll.dice]
        print(f"Roll {roll_number}: {player.name} rolled:", sorted(dice))     
        print()   
        score, dice_banked = calculate_score(roll)
        if score == 0 and dice_banked == 0:
            return 0
        turn_score += score
        remaining_dice -= dice_banked

        if remaining_dice == 0 and turn_score != 0:
            remaining_dice = 6

        print(f"Turn score: {turn_score} | Remaining dice: {remaining_dice}\n")
        roll_again = ""
        while True:
            if remaining_dice < 3 and player.score == 0:
                print("Remember you need 500 points to get on the board.")
            roll_again = input("Roll again? (y/n): ")
            if roll_again.lower() != "y" and roll_again.lower() != "n":
                print("Invalid input. Please enter 'y' or 'n'.")
            else:
                break
        if roll_again.lower() == "n":
                print()
                break
        elif roll_again.lower() == "y":
            roll_number += 1
            print()
            continue
        
    return turn_score


def play_game():
    initialize_game()
    player_scores = [player.score for player in players]
    current_player = players[0]
    player_names = [player.name for player in players]
    res = str(player_names)[1:-1]
    print("Players: " + res)
    round = 1

    while max(player_scores) < WINNING_SCORE:
        print(f"\n {current_player.name} || Round {round} ||")
        turn_score = player_turn(current_player)

        if turn_score > 0:
            current_player.farkles_in_a_row = 0
        else:
            current_player.farkles_in_a_row += 1
            if current_player.farkles_in_a_row == 3:
                print(f"{current_player.name} is out!")
                players.remove(current_player)

        if current_player.score == 0:
            if 0 < turn_score < 500:
                print("First score must be at least 500.")
                turn_score = 0
            elif turn_score >= 500:
                print("You scored at least 500 points, you are on the board!")

        current_player.score += turn_score

        if current_player.score >= WINNING_SCORE:
            print(f"{current_player.name} wins!")
            break

        if len(players) == 1:
            print(f"{players[0].name} wins!")
            break
        
        current_player = players[(players.index(current_player) + 1) % len(players)]
        if current_player == players[0]:
            print("\n----------------------------------------")
            print("|| Current Scores ||\n")
            sorted_players = sorted(players, key=lambda x: x.score, reverse=True)
            for player in sorted_players:
                print(f"{player.name}: {player.score}")
            print("----------------------------------------\n")
            round += 1
            
        


play_game()    
