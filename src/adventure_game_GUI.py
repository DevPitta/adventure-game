import PySimpleGUI as sg

game_image = 'image/game_scale.png'
victory_image = 'image/victory.png'
defeat_image = 'image/defeat.png'


class Game:
    def play(self, character_name):
        while True:
            print(f"Welcome to the New World {character_name}!")
            self.decisions(character_name)
            play_again = sg.popup_yes_no(f"{character_name} Congratulations on finishing the story!\nDo you want to play again and discover the other outcomes?", font=14)
            if play_again == "No":
                break

    def decisions(self, character_name):
        characteristics = sg.Window('Characteristics', [[sg.T(f"{character_name}'s feature:\n[1] Fearful\n[2] Courageous")], [sg.Button('1', size=5), sg.Button('2', size=5)]], font=14, disable_close=True).read(close=True)
        if characteristics[0] == '1':
            print("Characteristic: Fearful")
            actions = sg.Window('Actions', [[sg.T("What do you want to do?\n[1] Run\n[2] Warn")], [sg.Button('1', size=5), sg.Button('2', size=5)]], font=14, disable_close=True).read(close=True)
            if actions[0] == '1':
                print("Action: Run")
                run = sg.Window('Run', [[sg.T("Who do you want to run from?\n[1] From the Humans\n[2] From the Monsters")], [sg.Button('1', size=5), sg.Button('2', size=5)]], font=14, disable_close=True).read(close=True)
                if run[0] == '1':
                    print("Run: From the Humans")
                    print("Final: You were killed by the Monsters!")
                    sg.Window("Final", [[sg.T("You were killed by the Monsters!")], [sg.Button(image_filename=defeat_image)]], font=14, disable_close=True).read(close=True)
                else:
                    print("Run: From the Monsters")
                    print("Final: You were protected by Humans and you are alive!")
                    sg.Window("Final", [[sg.T("You were protected by Humans and you are alive!")], [sg.Button(image_filename=victory_image)]], font=14, disable_close=True).read(close=True)
            else:
                print("Characteristic: Warn")
                warn = sg.Window('Warn', [[sg.T("Who do you want to warn?\n[1] Humans\n[2] Monsters")], [sg.Button('1', size=5), sg.Button('2', size=5)]], font=14, disable_close=True).read(close=True)
                if warn[0] == '1':
                    print("Warn: Humans")
                    print("Final: You were protected by Humans and you are alive!")
                    sg.Window("Final", [[sg.T("You were protected by Humans and you are alive!")], [sg.Button(image_filename=victory_image)]], font=14, disable_close=True).read(close=True)
                else:
                    print("Warn: Monsters")
                    print("Final: You saved the Monsters and got killed!")
                    sg.Window("Final", [[sg.T("You saved the Monsters and got killed!")], [sg.Button(image_filename=defeat_image)]], font=14, disable_close=True).read(close=True)
        else:
            print("Characteristic: Courageous")
            actions = sg.Window('Actions', [[sg.T("What do you want to do?\n[1] Fight alone\n[2] Fight in group")], [sg.Button('1', size=5), sg.Button('2', size=5)]], font=14, disable_close=True).read(close=True)
            if actions[0] == '1':
                print("Action: Fight alone")
                mode = sg.Window('Mode', [[sg.T("Which way do you choose to fight?\n[1] Berseker\n[2] Clever")], [sg.Button('1', size=5), sg.Button('2', size=5)]], font=14, disable_close=True).read(close=True)
                if mode[0] == '1':
                    print("Mode: Berseker")
                    print("Final: You fought bravely but died!")
                    sg.Window("Final", [[sg.T("You fought bravely but died!")], [sg.Button(image_filename=defeat_image)]], font=14, disable_close=True).read(close=True)
                else:
                    print("Mode: Clever")
                    print("Final: You fought strategically and defeated all monsters!")
                    sg.Window("Final", [[sg.T("You fought strategically and defeated all monsters!")], [sg.Button(image_filename=victory_image)]], font=14, disable_close=True).read(close=True)
            else:
                print("Action: Fight in group")
                strategy = sg.Window('Strategy', [[sg.T("What strategy do you choose to lead the fight?\n[1] Straight line\n[2] Surround")], [sg.Button('1', size=5), sg.Button('2', size=5)]], font=14, disable_close=True).read(close=True)
                if strategy[0] == 1:
                    print("Strategy: Straight line")
                    print("Final: You killed all your mates and died!")
                    sg.Window("Final", [[sg.T("You killed all your mates and died!")], [sg.Button(image_filename=defeat_image)]], font=14, disable_close=True).read(close=True)
                else:
                    print("Strategy: Surround")
                    print("Final: You ambushed the monsters and slaughtered them!")
                    sg.Window("Final", [[sg.T("You ambushed the monsters and slaughtered them!")], [sg.Button(image_filename=victory_image)]], font=14, disable_close=True).read(close=True)


class PythonScreen(Game):
    def __init__(self):
        # Change color layout
        sg.change_look_and_feel('Reddit')
        # Layout
        layout = [
            [sg.Image(filename=game_image)],
            [sg.Text("Enter your character's name:", font=14), sg.Input(font=14, size=(20, 0), key='name')],
            [sg.Output(font=14, size=(45, 15))],
            [sg.Button('Start', font=14, size=20, button_color='green'), sg.Button('Exit', font=14, size=20, button_color='red')],
        ]
        # Window
        self.window = sg.Window("Interactive Adventure Game").layout(layout)

    def Start(self):
        while True:
            # Extract screen data
            self.button, self.values = self.window.Read()
            character_name = str(self.values['name'])
            if self.button == 'Exit':
                break
            self.play(character_name)
            print('-' * 30)


screen = PythonScreen()
screen.Start()
