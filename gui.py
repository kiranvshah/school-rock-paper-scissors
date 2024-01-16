import tkinter as tk
from tkinter import ttk
from main import Game, Hand


class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.game = Game()
        self.title('Rock Paper Scissors')
        self.resizable(False, False)

        self.frames = {
            'setup_frame': SetupFrame(self),
            'choose_frame': ChooseFrame(self),
        }
        self.show_frame('setup_frame')

    def show_frame(self, current_frame: str):
        widgets = self.winfo_children()
        for widget in widgets:
            if widget.winfo_class() == 'Frame':
                widget.pack_forget()
        frame_to_show = self.frames[current_frame]
        frame_to_show.pack(expand=True, fill=tk.BOTH)
        frame_to_show.set_up()


class SetupFrame(tk.Frame):
    def __init__(self, parent: GameApp):
        super().__init__()
        self.parent = parent

        # player one
        self.player_one_label = tk.Label(self, text='Player 1', font=('', 15))
        self.player_one_name_label = tk.Label(self, text='Name:')
        self.player_one_name_entry = tk.Entry(self)
        player_one_is_computer = tk.BooleanVar()
        self.player_one_human_radiobutton = ttk.Radiobutton(
            self, text='Human', variable=player_one_is_computer, value=False,
        )
        self.player_one_computer_radiobutton = ttk.Radiobutton(
            self, text='Computer', variable=player_one_is_computer, value=True,
        )

        # player two
        self.player_two_label = tk.Label(self, text='Player 2', font=('', 15))
        self.player_two_name_label = tk.Label(self, text='Name:')
        self.player_two_name_entry = tk.Entry(self)
        player_two_is_computer = tk.BooleanVar()
        self.player_two_human_radiobutton = ttk.Radiobutton(
            self, text='Human', variable=player_two_is_computer, value=False,
        )
        self.player_two_computer_radiobutton = ttk.Radiobutton(
            self, text='Computer', variable=player_two_is_computer, value=True,
        )

        # game
        self.game_label = tk.Label(self, text='Game', font=('', 15))
        self.max_rounds_label = tk.Label(self, text='Max rounds:')
        self.max_rounds_entry = tk.Entry(self)
        self.ruleset_label = tk.Label(self, text='Ruleset:')
        self.ruleset_combobox = ttk.Combobox(self, state='readonly', values=['normal', 'lizard spock'])
        self.ruleset_combobox.current(0)

        self.go_button = tk.Button(self, text='Go', font=('', 15), command=lambda: self.parent.show_frame('choose_frame'))

        self.place_widgets()

    def place_widgets(self):
        padding = {
            'padx': 5,
            'pady': 10,
        }
        self.player_one_label.grid(row=0, column=0, **padding)
        self.player_one_name_label.grid(row=1, column=0, sticky='e', **padding)
        self.player_one_name_entry.grid(row=1, column=1, sticky='w', **padding)
        self.player_one_human_radiobutton.grid(row=2, column=0, **padding)
        self.player_one_computer_radiobutton.grid(row=2, column=1, **padding)

        self.player_two_label.grid(row=3, column=0, **padding)
        self.player_two_name_label.grid(row=4, column=0, sticky='e', **padding)
        self.player_two_name_entry.grid(row=4, column=1, sticky='w', **padding)
        self.player_two_human_radiobutton.grid(row=5, column=0, **padding)
        self.player_two_computer_radiobutton.grid(row=5, column=1, **padding)

        self.game_label.grid(row=6, column=0, **padding)
        self.max_rounds_label.grid(row=7, column=0, sticky='e', **padding)
        self.max_rounds_entry.grid(row=7, column=1, sticky='w', **padding)
        self.ruleset_label.grid(row=8, column=0, sticky='e', **padding)
        self.ruleset_combobox.grid(row=8, column=1, sticky='w', **padding)

        self.go_button.grid(row=9, column=0, **padding)

    def set_up(self):
        pass
        # variables can go here


class ChooseFrame(tk.Frame):
    def __init__(self, parent: GameApp):
        super().__init__()
        self.parent = parent

        self.label = tk.Label(self, text=f'{"kiran"}, choose your hand: ')

        self.buttons = [tk.Button(self, text=option) for option in Hand.allowable_hands]

        self.place_widgets()

    def place_widgets(self):
        padding = {
            'padx': 5,
            'pady': 10,
        }
        self.label.grid(row=0, column=0, columnspan=3, **padding)
        for index, button in enumerate(self.buttons):
            button.grid(row=1, column=index, **padding)


class Results(tk.Frame):
    # this frame will be shown once user selects an option
    def __init__(self, parent: GameApp):
        super().__init__()
        self.parent = parent

        self.header = tk.Label(self, text=f'Round {self.parent.game.current_round}', font=('', 15))

        # insert results and score here once game is functional



if __name__ == '__main__':
    # root = tk.Tk()
    # root.title('Rock Paper Scissors')
    # f = ChooseFrame(root)
    # f.pack()
    # root.mainloop()

    app = GameApp()
    app.mainloop()

