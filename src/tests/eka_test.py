'''import unittest
from ..GUI import mainGUI
from tkinter import Tk

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.teseri = mainGUI.GUI(Tk())

    def test_ui_toimii(self):
        self.assertEqual(self.teseri._current_view, None)
'''