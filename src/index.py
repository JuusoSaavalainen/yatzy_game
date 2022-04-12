import logik
import pygame
import gameloop
from GUI.mainGUI import *
from tkinter import Tk
from data.intialize_database import initialize_database
from gameloop import GameLoop
from clock import Clock
from renderer import Renderer
from eventqueue import EventQueue


def main():
    '''    initialize_database()
    window = Tk()
    window.title("YATZEEE")

    gui = GUI(window)
    gui.start()

    window.mainloop()'''
    draw = logik.Draw(1000)
    dp_height = 1000
    dp_widht = 1000

    dp = pygame.display.set_mode((dp_widht, dp_height))

    pygame.display.set_caption('Yatzyy!')

    event_queue = EventQueue()
    renderer = Renderer(dp, draw)
    clock = Clock()
    game_loop = GameLoop(draw, renderer, clock, event_queue)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
 