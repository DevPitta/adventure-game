from colors import FontColors, Styles

fc = FontColors
s = Styles


class Game():
    def play(self):
        header()
        while True:
            character = str(input("Enter your character's name: "))
            print(f"Welcome to the New World {character}!")
            self.decisions()
            play_again = str(input(
                "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
            if play_again not in "YN":
                play_again = play_again_is_Y_or_N(play_again)
            if play_again == "N":
                break

    def decisions(self):
        print("""Character characteristics:
        [1] Fearful
        [2] Courageous""")
        characteristics = int(input("What is your character's trait? "))
        if characteristics == 1:
            print("""Actions:
            [1] Run
            [2] Warn""")
            actions = int(input("What do you want to do? "))
            if actions == 1:
                print("""Run:
                [1] From the Humans
                [2] From the Monsters""")
                run = int(input("Who do you want to run from? "))
                if run == 1:
                    print("You were killed by the Monsters!")
                else:
                    print("You were protected by Humans and you are alive")
            else:
                print("""Warn:
                [1] Humans
                [2] Monsters""")
                warn = int(input("Who do you want to warn? "))
                if warn == 1:
                    print("You were protected by Humans and you are alive")
                else:
                    print("You saved the Monsters and got killed!")
        else:
            print("""Actions:
            [1] Fight alone
            [2] Fight in group""")
            actions = int(input("What do you want to do? "))
            if actions == 1:
                print("""Mode:
                [1] Berseker
                [2] Clever""")
                mode = int(input("Which way do you choose to fight? "))
                if mode == 1:
                    print("You fought bravely but died!")
                else:
                    print("You fought strategically and defeated all monsters!")
            else:
                print("""Strategy:
                [1] Straight line
                [2] Surround""")
                strategy = int(
                    input("What strategy do you choose to lead the fight? "))
                if strategy == 1:
                    print("You killed all your mates and died!")
                else:
                    print("You ambushed the monsters and slaughtered them!")


def play_again_is_Y_or_N(play_again):
    while play_again not in "YN":
        play_again = str(
            input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
        if play_again in "YN":
            break
    return play_again


def header():
    title = "INTERACTIVE ADVENTURE GAME"
    print("-=" * 40)
    print(f"{title.center(80)}")
    print("-=" * 40)
