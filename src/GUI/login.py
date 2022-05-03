from tkinter import ttk, constants, messagebox
from src.GUI import main_gui

class Login:
    def __init__(self, root, handle_play, show_highscore):
        self._root = root
        self._handle_play = handle_play
        self._show_highscore = show_highscore
        self._frame = None
        self._username_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        main_label = ttk.Label(master=self._frame, text="Login or Highscores")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_play1)
        register_button = ttk.Button(
            master=self._frame, text="Highscores", command=self._show_highscore)

        main_label.grid(row=0, column=1)
        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)
        login_button.grid(row=3, column=1)
        register_button.grid(row=3, column=0)

    def _handle_play1(self):
        name_help = self._username_entry.get()
        print(name_help)
        if len(name_help) == 0:
            messagebox.showinfo("error", "Insert username first")
            return
        main_gui.GUI.handle_play(self, name_help)
        