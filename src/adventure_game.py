from colors import FontColors, Styles

fc = FontColors
s = Styles


class Game():
    def play(self):
        header()
        while True:
            character = str(
                input(f"{fc.magenta}Enter your character's name: {s.end}"))
            print(f"{fc.cyan}Welcome to the New World {character}!{s.end}")
            self.decisions(character)
            play_again = str(input(
                f"{fc.green}{character} Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: {s.end}")).upper().strip()
            if play_again not in "YN":
                play_again = play_again_is_Y_or_N(play_again)
            if play_again == "N":
                break
        footer()

    def decisions(self, character):
        print("""Character characteristics:
        [1] Fearful
        [2] Courageous""")
        characteristics = int(input(f"{fc.yellow}What is {character}'s trait? {s.end}"))
        if characteristics == 1:
            print("""Actions:
            [1] Run
            [2] Warn""")
            actions = int(input(f"{fc.yellow}What do you want to do? {s.end}"))
            if actions == 1:
                print("""Run:
                [1] From the Humans
                [2] From the Monsters""")
                run = int(input(f"{fc.yellow}Who do you want to run from? {s.end}"))
                if run == 1:
                    print(f"{fc.red}You were killed by the Monsters!{s.end}")
                else:
                    print(f"{fc.blue}You were protected by Humans and you are alive{s.end}")
            else:
                print("""Warn:
                [1] Humans
                [2] Monsters""")
                warn = int(input(f"{fc.yellow}Who do you want to warn? {s.end}"))
                if warn == 1:
                    print(f"{fc.blue}You were protected by Humans and you are alive{s.end}")
                else:
                    print(f"{fc.red}You saved the Monsters and got killed!{s.end}")
        else:
            print("""Actions:
            [1] Fight alone
            [2] Fight in group""")
            actions = int(input(f"{fc.yellow}What do you want to do? {s.end}"))
            if actions == 1:
                print("""Mode:
                [1] Berseker
                [2] Clever""")
                mode = int(input(f"{fc.yellow}Which way do you choose to fight? {s.end}"))
                if mode == 1:
                    print(f"{fc.red}You fought bravely but died!{s.end}")
                else:
                    print(f"{fc.blue}You fought strategically and defeated all monsters!{s.end}")
            else:
                print("""Strategy:
                [1] Straight line
                [2] Surround""")
                strategy = int(
                    input(f"{fc.yellow}What strategy do you choose to lead the fight? {s.end}"))
                if strategy == 1:
                    print(f"{fc.red}You killed all your mates and died!{s.end}")
                else:
                    print(f"{fc.blue}You ambushed the monsters and slaughtered them!{s.end}")


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
    print(f"{fc.light_red}{title.center(80)}{s.end}")
    print("-=" * 40)


def footer():
    title = "END GAME"
    print("-=" * 40)
    print(f"{fc.white}{s.bold}{title.center(80)}{s.end}")
    print("-=" * 40)
