from data.database_connection import get_database_connection
from GUI.login import Login
from GUI.register import Register
from repot.yatzyrepo import Loginrepo


class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login()

    def _handle_play(self):
        print("NOW IF EVERYTHING IS RIGHT GAME WILL START")

    def _handle_register(self, var_u, var_p):
        sqlite_con = get_database_connection()
        Loginrepo(sqlite_con).create_acc()
    
    def _handle_back(self):
        self._show_login()

    def _show_login(self):
        self._hide_current_view()
        self._current_view = Login(
            self._root,
            self._handle_play,
            self._show_register
        )

        self._current_view.pack()

    def _show_register(self):
        self._hide_current_view()
        self._current_view = Register(
            self._root,
            self._handle_back
        )
        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
