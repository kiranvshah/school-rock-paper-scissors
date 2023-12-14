import tkinter as tk
from tkinter import ttk


class SetupFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

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
        self.max_rounds_label.grid(row=7, column=0, **padding)
        self.max_rounds_entry.grid(row=7, column=1, **padding)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Rock Paper Scissors')
    f = SetupFrame(root)
    f.pack()
    root.mainloop()
