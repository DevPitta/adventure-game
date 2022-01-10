while True:
    character = str(input("Enter your character's name: "))
    print("START")
    print("""Character characteristics:
    [1] Fearful
    [2] Courageous""")
    decision_1 = int(input("What is your character's trait? "))
    if decision_1 == 1:
        print("""Actions:
        [1] Run
        [2] Warn""")
        decision_2 = int(input("Whats do you want to do? "))
        if decision_2 == 1:
            print("""Run:
            [1] From the Humans
            [2] From the Monsters""")
            decision_3 = int(input("Who do you want to run from? "))
            if decision_3 == 1:
                print("You were killed by the Monsters!")
                play_again = str(input(
                    "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
                while play_again not in "YN":
                    play_again = str(
                        input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
                    if play_again in "YN":
                        break
                if play_again == "N":
                    break
            else:
                print("You were protected by Humans and you are alive")
                play_again = str(input(
                    "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
                while play_again not in "YN":
                    play_again = str(
                        input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
                    if play_again in "YN":
                        break
                if play_again == "N":
                    break
        else:
            print("""Warn:
            [1] Humans
            [2] Monsters""")
            decision_3 = int(input("Who do you want to warn? "))
            if decision_3 == 1:
                print("You saved the Humans and you are alive!")
                play_again = str(input(
                    "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
                while play_again not in "YN":
                    play_again = str(
                        input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
                    if play_again in "YN":
                        break
                if play_again == "N":
                    break
            else:
                print("You saved the Monsters and got killed!")
                play_again = str(input(
                    "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
                while play_again not in "YN":
                    play_again = str(
                        input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
                    if play_again in "YN":
                        break
                if play_again == "N":
                    break
    else:
        print("""Actions:
        [1] Fight alone
        [2] Fight in group""")
        decision_2 = int(input("Whats do you want to do? "))
        if decision_2 == 1:
            print("""Mode:
            [1] Berseker
            [2] Clever""")
            decision_3 = int(input("Which way do you choose to fight? "))
            if decision_3 == 1:
                print("You fought bravely but died!")
                play_again = str(input(
                    "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
                while play_again not in "YN":
                    play_again = str(
                        input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
                    if play_again in "YN":
                        break
                if play_again == "N":
                    break
            else:
                print("You fought strategically and defeated all monsters!")
                play_again = str(input(
                    "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
                while play_again not in "YN":
                    play_again = str(
                        input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
                    if play_again in "YN":
                        break
                if play_again == "N":
                    break
        else:
            print("""Strategy:
            [1] Straight line
            [2] Surround""")
            decision_3 = int(
                input("What strategy do you choose to lead the fight? "))
            if decision_3 == 1:
                print("You killed all your mates and died!")
                play_again = str(input(
                    "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
                while play_again not in "YN":
                    play_again = str(
                        input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
                    if play_again in "YN":
                        break
                if play_again == "N":
                    break
            else:
                print("You ambushed the monsters and slaughtered them!")
                play_again = str(input(
                    "Congratulations on finishing the story! Type 'Y' to know the other outcomes or 'N' to exit: ")).upper().strip()
                while play_again not in "YN":
                    play_again = str(
                        input("Invalid input! Type only 'Y' or 'N': ")).upper().strip()
                    if play_again in "YN":
                        break
                if play_again == "N":
                    break
