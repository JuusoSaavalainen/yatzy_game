import pygame
from tkinter import Tk
from src import logik
from src.GUI import main_gui
from src.Gameloops.clock import Clock
from src.Gameloops.renderer import Renderer
from src.Gameloops.eventqueue import EventQueue
from src.data.database_connection import get_database_connection
from src.repot.yatzyrepo import Loginrepo

'''Class to handle the main looping of the game and handling the events

Attributes
    draw = object connected to logik
    clock = tool to set fps ets clockking
    renderer = rending tool
    dp = display
'''
class GameLoop:
    def __init__(self, draw, renderer, clock, event_queue ,dp):
        self._draw = draw
        self._clock = clock
        self._renderer = renderer
        self._event_queue = event_queue
        self._dp = dp

    def start(self):
        ''' First thing to call when starting the game
        opens only if some user is set to active and handles the setup
        for the new game'''

        connection = get_database_connection()
        helpinghand_1 = Loginrepo(connection)
        if helpinghand_1.check_activity() == False:
            return

        self._draw.print_rules()
        self._draw.print_scoreboard()
        self._draw.first_roll()
        
        while True:
            if self._traverse_event() is False:
                break
            self._render()
            self._clock.tick(60)

    def _traverse_event(self):
        ''' main method to keep up with the events in the pygame.
        handles clicks and key presses accordingly'''
        for event in self._event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = event.pos[0], event.pos[1]

                if event.button == 1:
                    self._draw.roll_dice(mouse_x, mouse_y, ('a'))
                    self._draw.get_hand(mouse_x, mouse_y)
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    pygame.quit()
                    pygame.font.init()
                    dp = pygame.display.set_mode((1000, 1000))
                    draw = logik.Draw(dp)
                    pygame.display.set_caption('Yatzyy!')
                    event_queue = EventQueue()
                    renderer = Renderer(dp, draw)
                    clock = Clock()
                    game_loop = GameLoop(draw, renderer, clock, event_queue,dp)                        
                    pygame.init()
                    game_loop.start()
                if event.key == pygame.K_k:
                    window = Tk()
                    window.title("YATZEEE")
                    gui = main_gui.GUI(window)
                    gui.start()

                self._draw.select_dice(event.key)
                self._draw.unlock(event.key)
                self._draw.roll_dice(1, 1, event.key)


            
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
