from tkinter import messagebox
from src.data.database_connection import get_database_connection
from src.GUI.login import Login
from src.repot.yatzyrepo import Loginrepo

class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login()

    def handle_play(self, name, passw):
        connection = get_database_connection()
        helper_1 = Loginrepo(connection)
        helper_1.set_nonactive()
        helper_1.print_all()
        if helper_1.check_login(name, passw):
            helper_1.set_active(name)
            self._root.destroy()
        else:
            messagebox.showerror("error", "Invalid credentials")
            return


    def handle_register(self, name, passw):
        connection = get_database_connection()
        helper_1 = Loginrepo(connection)
        helper_1.find_user(name)
        if helper_1.find_user(name):
            helper_1.create_acc(name, passw)
            messagebox.showinfo("Account created", "Account was created!")
        else:
            messagebox.showerror("error", "Username taken")
            return


    def _handle_back(self):
        self._show_login()

    def _show_login(self):
        self._hide_current_view()
        self._current_view = Login(
            self._root,
            self.handle_play
        )
        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
