
import re
import sqlite3
from data import database_connection
from data import intialize_database
from GUI.login import Login
#from highscores import Highscores
from GUI.register import Register
from repot.yatzyrepo import Loginrepo

from tkinter import ttk, constants, Tk , Frame
import tkinter


class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login()
    
    def _handle_play(self):
        print("NOW IF EVERYTHING IS RIGHT GAME WILL START")
    
    def _handle_register(self,varU,varP):
        sqliteConnection = get_database_connection()
        A = Loginrepo(sqliteConnection)
        A.create_acc()


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
    

