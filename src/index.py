from GUI.mainGUI import *
from tkinter import Tk
import repot
import tests
import data
from data.intialize_database import initialize_database


def main():
    initialize_database()
    window = Tk()
    window.title("YATZEEE")

    gui = GUI(window)
    gui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
