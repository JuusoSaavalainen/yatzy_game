import pygame
from tkinter import Tk
from src import logik
from src.data.intialize_database import initialize_database1
from src import gameloop
from src.GUI import main_gui
from src.data import intialize_database
from src.gameloop import GameLoop
from src.clock import Clock
from src.renderer import Renderer
from src.eventqueue import EventQueue


def main():
    initialize_database1()
    window = Tk()
    window.title("YATZEEE")

    gui = main_gui.GUI(window)
    gui.start()

    window.mainloop()

    dp_height = 1000
    dp_widht = 1000
    pygame.font.init()
    dp = pygame.display.set_mode((dp_widht, dp_height))
    draw = logik.Draw(dp, gui.name)
    pygame.display.set_caption('Yatzyy!')
    event_queue = EventQueue()
    renderer = Renderer(dp, draw)
    clock = Clock()
    game_loop = GameLoop(draw, renderer, clock, event_queue,dp)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
 