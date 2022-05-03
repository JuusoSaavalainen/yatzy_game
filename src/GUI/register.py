from tkinter import ttk, constants
from src.data.database_connection import get_database_connection
from src.repot.yatzyrepo import Loginrepo

class Highscores:
    def __init__(self, root, handle_back):
        self._root = root
        self._handle_back = handle_back
        self._frame = None
        self._username = None
        self._password = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        connection = get_database_connection()
        helper_1 = Loginrepo(connection)
        helper_1 = helper_1.get_highscores()

        self._frame = ttk.Frame(master=self._root)
        main_label = ttk.Label(master=self._frame, text="HIGHSCORES")
        score_label = ttk.Label(master=self._frame, text='todo _ insert highscorelist')
        back_button = ttk.Button(master=self._frame, text='Back', command=self._handle_back)

        main_label.grid(row=0, column=0)
        score_label.grid(row=1, column=0)
        back_button.grid(row=2, column=0)
        