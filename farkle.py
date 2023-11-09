import random

WINNING_SCORE = 10000
number_of_players = 0
players = []

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.farkles_in_a_row = 0

class Score:
    def __init__(self, name, points, number_of_dice):
        self.name = name
        self.points = points
        self.number_of_dice = number_of_dice

class Die:
    def __init__(self):
        self.value = None
        self.selected = False

    def roll(self):
        self.value = random.randint(1, 6)

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

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
            if not die.selected:
                die.roll()

    def select_die(self, index):
        self.dice[index].select()

    def deselect_die(self, index):
        self.dice[index].deselect()



# def roll_dice(number_of_dice):
#     roll = []
#     for _ in range(number_of_dice):
#         die = Die.roll()
#         roll.append(die.value)

#     return roll


def calculate_remaining_dice(dice):
    remaining_dice = len(dice)
    ...
    return remaining_dice


def calculate_score(dice):
    score = 0
    possible_scores = check_for_scores(dice)
    print(possible_scores)
    # if len(possible_scores) > 0:
    #     for i in possible_scores:

            
    


    
    return score


def check_for_scores(Roll):
    dice = [die.value for die in Roll.dice]
    possible_scores = []
    pairs = 0
    triplets = 0
    four_of_a_kinds = 0
    
    for i in range(1,7):
        # Check for pairs
        if dice.count(i) == 2:
            pairs += 1

        # Check for 3 of a kind
        if dice.count(i) == 3:
            if i == 1:
                possible_scores.append({"Three Ones": 1000})
            else:
                possible_scores.append({"Three-of-a-Kind": 100 * i})
            triplets += 1

        # Check for 4 of a kind
        elif dice.count(i) == 4:
            possible_scores.append({"Four-of-a-Kind": 1000})
            four_of_a_kinds += 1

        # Check for 5 of a kind
        elif dice.count(i) == 5:
            possible_scores.append({"Five-of-a-Kind": 2000})

        # Check for 6 of a kind
        elif dice.count(i) == 6:
            possible_scores.append({"Six-of-a-Kind": 3000})

    # Check for 1-6 straight
    if sorted(dice) == [1, 2, 3, 4, 5, 6]:
        possible_scores.append({"Straight": 1500})

    # Check for 3 pairs
    if pairs == 3:
        possible_scores.append({"Three Pairs": 1500})

    # Check for 4 of a kind plus a pair
    if four_of_a_kinds == 1 and pairs == 1:
        possible_scores.append({"Four-of-a-Kind + Pair": 1500})

    # Check for 2 triplets
    if triplets == 2:
        possible_scores.append({"Two Triplets": 2500})

    # Check for ones scores
    if 1 in dice:
        if dice.count(1) != 3:
            possible_scores.append({"Ones": dice.count(1) * 100})

    # Check for fives scores
    if 5 in dice:
        if dice.count(5) < 3:
            possible_scores.append({"Fives": dice.count(5) * 50})
            
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

    while True:
        roll = Roll(remaining_dice)
        roll.roll_all()
        dice = [die.value for die in roll.dice]
        print(f"{player.name} rolled:", dice)
        
        score = calculate_score(roll)
        if score == 0:
            return turn_score
        turn_score += score
        remaining_dice = calculate_remaining_dice(roll)
        
    return turn_score


def play_game():
    initialize_game()
    player_scores = [player.score for player in players]
    current_player = players[0]
    player_names = [player.name for player in players]
    print("Players: ", player_names)

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

        if len(players) == 1:
            print(f"{players[0].name} wins!")
            break

        current_player = players[(players.index(current_player) + 1) % len(players)]
        if current_player == players[0]:
            for player in players:
                print(f"{player.name}: {player.score}")
            
        


play_game()    
