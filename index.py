import pygame
from tkinter import Tk
from src import logik
from src.GUI import main_gui
from src.Gameloops.gameloop import GameLoop
from src.Gameloops.clock import Clock
from src.Gameloops.renderer import Renderer
from src.Gameloops.eventqueue import EventQueue
from src.data.database_connection import get_database_connection
from src.repot.yatzyrepo import Loginrepo


def main():
    '''the first function to call to start the whole thing
    is used to setup the game and call the ui for the login first 
    also checks if the activity is accordingly set before starting the
    pygame'''

    connection = get_database_connection()
    helper_1 = Loginrepo(connection)
    helper_1.set_nonactive()
    window = Tk()
    window.title("YATZYY")

    gui = main_gui.GUI(window)
    gui.start()
    
    window.mainloop()

    dp_height = 1000
    dp_widht = 1000
    pygame.font.init()

    dp = pygame.display.set_mode((dp_widht, dp_height))
    draw = logik.Draw(dp)
    pygame.display.set_caption('Yatzyy!')
    event_queue = EventQueue()
    renderer = Renderer(dp, draw)
    clock = Clock()
    game_loop = GameLoop(draw, renderer, clock, event_queue, dp)

    
    pygame.init()
    game_loop.start()



if __name__ == "__main__":
    main()