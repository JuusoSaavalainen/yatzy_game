from tkinter import messagebox
from src.data.database_connection import get_database_connection
from src.GUI.login import Login
from src.GUI.register import Highscores
from src.repot.yatzyrepo import Loginrepo

class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self.name = None

    def start(self):
        self._show_login()

    def handle_play(self, name):
        self.name = name
        self._root.destroy()

    def _handle_register(self, variable_username):
        sqlite_con = get_database_connection()
        helper_1 = Loginrepo(sqlite_con)
        helper_2 = helper_1.create_acc(variable_username)
        messagebox.showinfo("ACCOUNT INFO", helper_2)

    def _handle_back(self):
        self._show_login()

    def _show_login(self):
        self._hide_current_view()
        self._current_view = Login(
            self._root,
            self.handle_play,
            self._show_highscore
        )
        self._current_view.pack()

    def _show_highscore(self):
        self._hide_current_view()
        self._current_view = Highscores(
            self._root,
            self._handle_back
        )
        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
