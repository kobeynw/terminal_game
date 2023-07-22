import random
import time


#CLASS FOR PLAYERS
dice_list = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

def roll_dice(kept=None):
    die_1 = random.choice(dice_list)
    die_2 = random.choice(dice_list)
    die_3 = random.choice(dice_list)
    die_4 = random.choice(dice_list)
    die_5 = random.choice(dice_list)
    new_roll = ""
    if die_5 == die_4 and die_5 == die_3 and die_5 == die_2 and die_5 == die_1:
        print(die_5*5)
        return 'yahtzee'
    if kept is None:
        return die_1 + die_2 + die_3 + die_4 + die_5
    for num in kept:
        if num == '1':
            new_roll += '⚀'
        elif num == '2':
            new_roll += '⚁'
        elif num == '3':
            new_roll += '⚂'
        elif num == '4':
            new_roll += '⚃'
        elif num == '5':
            new_roll += '⚄'
        elif num == '6':
            new_roll += '⚅'
    while not len(new_roll) == 5:
        new_roll += random.choice(dice_list)
    if new_roll[0] == new_roll[1] and new_roll[0] == new_roll[2] and new_roll[0] == new_roll[3] and new_roll[0] == \
            new_roll[4]:
        print(new_roll)
        return 'yahtzee'
    return new_roll


class Player:
    layout = """
    -----------------------------------------------------
    |                    YAHTZEE!                       |
    |---------------------------------------------------|
    |  UPPER SECTION:   |  HOW TO SCORE:    |           |
    |                   |                   |           |
    |  ACES    ⚀ = 1    |  add aces only    |           |
    |  TWOS    ⚁ = 2    |  add twos only    |           |
    |  THREES  ⚂ = 3    |  add threes only  |           |
    |  FOURS   ⚃ = 4    |  add fours only   |           |
    |  FIVES   ⚄ = 5    |  add fives only   |           |
    |  SIXES   ⚅ = 6    |  add sixes only   |           |
    |---------------------------------------------------|
    |---------------------------------------------------|
    |  LOWER SECTION:   |                   |           |
    |                   |                   |           |
    |  3 OF A KIND      | add total of dice |           |
    |  4 OF A KIND      | add total of dice |           |
    |  FULL HOUSE       | score of 25       |           |
    |  SMALL STRAIGHT   | score of 30       |           |
    |  LARGE STRAIGHT   | score of 40       |           |
    |  YAHTZEE!         | score of 50       |           |
    |  CHANCE           | add total of dice |           |
    |  YAHTZEE BONUS    | score of 90       |           |
    |---------------------------------------------------|
    |  Total:           |       --->        |           |
    -----------------------------------------------------
    """

    def __init__(self, name):
        self.name = name
        self.layout = Player.layout
        self.score = 0
        self.options = ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes', '3 of a kind', '4 of a kind', 'full house',
                   'small straight', 'large straight', 'chance', 'yahtzee']

    def __repr__(self):
        return f"Player: {self.name}"

    def update_scorecard(self, score, location):
        if len(score) == 2:
            if location == 'aces':
                self.layout = self.layout[:340] + str(score) + self.layout[342:]
            elif location == 'twos':
                self.layout = self.layout[:398] + str(score) + self.layout[400:]
            elif location == 'threes':
                self.layout = self.layout[:456] + str(score) + self.layout[458:]
            elif location == 'fours':
                self.layout = self.layout[:514] + str(score) + self.layout[516:]
            elif location == 'fives':
                self.layout = self.layout[:572] + str(score) + self.layout[574:]
            elif location == 'sixes':
                self.layout = self.layout[:630] + str(score) + self.layout[632:]
            elif location == '3 of a kind':
                self.layout = self.layout[:920] + str(score) + self.layout[922:]
            elif location == '4 of a kind':
                self.layout = self.layout[:978] + str(score) + self.layout[980:]
            elif location == 'full house':
                self.layout = self.layout[:1036] + str(score) + self.layout[1038:]
            elif location == 'small straight':
                self.layout = self.layout[:1094] + str(score) + self.layout[1096:]
            elif location == 'large straight':
                self.layout = self.layout[:1152] + str(score) + self.layout[1154:]
            elif location == 'yahtzee':
                self.layout = self.layout[:1210] + str(score) + self.layout[1212:]
            elif location == 'chance':
                self.layout = self.layout[:1268] + str(score) + self.layout[1270:]
            elif location == 'yahtzee bonus':
                self.layout = self.layout[:1326] + str(score) + self.layout[1328:]
        else:
            if location == 'aces':
                self.layout = self.layout[:341] + str(score) + self.layout[342:]
            elif location == 'twos':
                self.layout = self.layout[:399] + str(score) + self.layout[400:]
            elif location == 'threes':
                self.layout = self.layout[:457] + str(score) + self.layout[458:]
            elif location == 'fours':
                self.layout = self.layout[:515] + str(score) + self.layout[516:]
            elif location == 'fives':
                self.layout = self.layout[:573] + str(score) + self.layout[574:]
            elif location == 'sixes':
                self.layout = self.layout[:631] + str(score) + self.layout[632:]
            elif location == '3 of a kind':
                self.layout = self.layout[:921] + str(score) + self.layout[922:]
            elif location == '4 of a kind':
                self.layout = self.layout[:979] + str(score) + self.layout[980:]
            elif location == 'full house':
                self.layout = self.layout[:1037] + str(score) + self.layout[1038:]
            elif location == 'small straight':
                self.layout = self.layout[:1095] + str(score) + self.layout[1096:]
            elif location == 'large straight':
                self.layout = self.layout[:1153] + str(score) + self.layout[1154:]
            elif location == 'yahtzee':
                self.layout = self.layout[:1211] + str(score) + self.layout[1212:]
            elif location == 'chance':
                self.layout = self.layout[:1269] + str(score) + self.layout[1270:]
            elif location == 'yahtzee bonus':
                self.layout = self.layout[:1327] + str(score) + self.layout[1328:]

    def select_roll_location(self):
        print("Here is your current scorecard:")
        time.sleep(2)
        print(self.layout)
        while True:
            print("Where would you like this roll to be scored? (Type one of these options)")
            print(f'Options: {self.options}')
            location = input(">>")
            print("What was your score for this location? (Type a 1 or 2 digit number for your score)")
            score = input(">>")
            if location.lower() in self.options and location.lower() == 'aces' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('aces')
                break
            elif location.lower() in self.options and location.lower() == 'twos' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('twos')
                break
            elif location.lower() in self.options and location.lower() == 'threes' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('threes')
                break
            elif location.lower() in self.options and location.lower() == 'fours' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('fours')
                break
            elif location.lower() in self.options and location.lower() == 'fives' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('fives')
                break
            elif location.lower() in self.options and location.lower() == 'sixes' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('sixes')
                break
            elif location.lower() in self.options and location.lower() == '3 of a kind' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('3 of a kind')
                break
            elif location.lower() in self.options and location.lower() == '4 of a kind' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('4 of a kind')
                break
            elif location.lower() in self.options and location.lower() == 'full house' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('full house')
                break
            elif location.lower() in self.options and location.lower() == 'small straight' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('small straight')
                break
            elif location.lower() in self.options and location.lower() == 'large straight' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('large straight')
                break
            elif location.lower() in self.options and location.lower() == 'chance' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('chance')
                break
            elif location.lower() in self.options and location.lower() == 'yahtzee' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('yahtzee')
                break
            elif location.lower() in self.options and location.lower() == 'yahtzee bonus' and score.isnumeric() \
                    and len(score) < 3:
                self.options.remove('yahtzee bonus')
                break
            else:
                print("Sorry, I didn't get that! Make sure your desired location is in the list of options.")
                time.sleep(1)
        self.update_scorecard(score, location)
        return int(score)

    def update_score(self, score):
        self.score += score
        if len(str(self.score)) == 1:
            self.layout = self.layout[:1442] + " " + str(self.score) + " " + self.layout[1445:]
        elif len(str(self.score)) == 2:
            self.layout = self.layout[:1442] + str(self.score) + " " + self.layout[1445:]
        elif len(str(self.score)) == 3:
            self.layout = self.layout[:1442] + str(self.score) + self.layout[1445:]


#######################################################################################################################

#INTRODUCTION INFORMATION - explain game, instructions, possible inputs
def intro():
    print("Great shakes, it's Yahtzee! Your favorite game of luck and strategy! "
          "If you need a refresher about the rules, type 'rules'. "
          "Otherwise, press enter and you're ready to get started!")
    start = input(">>")
    if start.lower() == "rules":
        print("Rules:")
        print("\n\tThe object of Yahtzee is for each player to roll dice and fill out their score card over the course "
              "of a series of rounds, trying to obtain the best rolls they can in 13 different combinations. The player"
              " with the highest score at the end of the game wins.")
        print("\tAt the start of a turn, the player rolls all 5 dice. They can then roll some or all of "
              "the dice up to two more times, setting aside any dice they’d like to keep and re-rolling the rest. The "
              "dice can be scored after any of the rolls, but scoring the dice ends the player’s turn.")
        print("\tTo score the dice, the player selects one of the categories on their score card and puts their score "
              "in it. Each category can be scored only once per game (except for the Yahtzee category). Categories "
              "can be filled in any order. A player must score the dice on their turn even if there "
              "are no good categories remaining to score in. Once a category is filled it may not be changed. A player "
              "may write a score of zero in any category if they have rolled no point-generating results or if they "
              "simply choose to do so.")
        print("\tOnce all players have taken 13 turns, the game ends.\n")


#PLAYER CREATION - how many players, initialize players
def player_creation():
    print("First things first, we need your name(s) for your scorecard. "
          "Are there one or two players? (type '1' or '2')")
    while True:
        num_players = input("Number of players: ")
        if num_players == '1':
            name1 = input("Name: ")
            player_1 = Player(name1)
            print("Perfect, you're all set! Let the game begin!")
            return [player_1]
        elif num_players == '2':
            name1 = input("Name of first player: ")
            name2 = input("Name of second player: ")
            player_1 = Player(name1)
            player_2 = Player(name2)
            print("Perfect, you're all set! Let the game begin!")
            return [player_1, player_2]
        else:
            print("Sorry, didn't catch that! Are there one or two players? (type '1' or '2')")


#GAMEPLAY AND ACTIONS - roll dice, pick section for score
def gameplay(players):
    rounds = 13
    time.sleep(2)
    print("\nEach turn you can:"
          "\n1) view your scorecard before your turn, by typing 'scorecard'"
          "\n2) roll the dice by typing 'roll'"
          "\n\tYou will be able to roll 1-3 times, and can end your turn by typing 'end'."
          "\n\tTo save dice from your roll, type 'keep', then type the values of the dice you want to keep. "
          "For example, if you want to keep the '⚁', '⚂', and '⚃', then type 234"
          "\n\tYou will then select the location where you want your role to go on the scorecard.")

    for i in range(rounds):
        for player in players:
            time.sleep(2)
            print(f"\n{player.name}, your turn is next! \n(view scorecard by typing 'scorecard' or roll by typing 'roll')")
            while True:
                selection = input(">>")
                if selection.lower() == 'scorecard':
                    print(player.layout)
                else:
                    kept = None
                    round_count = 0
                    for j in range(3):
                        round_count += 1
                        print("now rolling...")
                        time.sleep(2)
                        roll = roll_dice(kept)
                        if roll == 'yahtzee':
                            time.sleep(2)
                            print("YAHTZEE!!! What a roll!")
                            time.sleep(2)
                            if 'yahtzee bonus' not in player.options:
                                player.options.append('yahtzee bonus')
                            break
                        print(roll)
                        if round_count == 3:
                            time.sleep(2)
                            print("Your 3 rolls are up!")
                            time.sleep(3)
                            break
                        print("Type 'end', 'roll', or 'keep'")
                        end = input(">>")
                        if end == 'end':
                            break
                        elif end == 'keep':
                            while True:
                                kept = input("(type values of dice to be kept) >>")
                                if len(kept) <= 5 and kept.isnumeric():
                                    break
                                else:
                                    print("Type the values of the dice you want to keep. "
          "For example, if you want to keep the '⚁', '⚂', and '⚃', then type 234")
                    score = player.select_roll_location()
                    player.update_score(score)
                    break


#SCORING - total, congratulate winner
def scoring(players):
    time.sleep(3)
    print("\nGame complete!")
    for player in players:
        time.sleep(2)
        print(f"{player.name}'s score for this game: {player.score}")
        if len(players) == 1:
            time.sleep(2)
            print(f"Good game, {player.name}!")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    if len(players) > 1:
        if players[0].score > players[1].score:
            print(f"Congratulations, {players[0].name}, you win!")
        elif players[1].score > players[0].score:
            print(f"Congratulations, {players[1].name}, you win!")
        else:
            print("Wow, a tie! Congratulations to both of you!")


#######################################################################################################################

#MAIN OVERALL FUNCTION
def yahtzee():
    intro()
    players = player_creation()
    gameplay(players)
    scoring(players)


if __name__ == "__main__":
    yahtzee()
