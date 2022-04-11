import sys
import unittest
import GUI.mainGUI
from data.database_connection import get_database_connection
from data.intialize_database import initialize_database
from tkinter import Tk


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.teseri = GUI.mainGUI.GUI(Tk())

    def test_ui_toimii(self):
        self.assertEqual(self.teseri._current_view, None)
