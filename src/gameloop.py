import pygame


class GameLoop:
    def __init__(self, draw, renderer, clock, event_queue,dp):
        self._draw = draw
        self._clock = clock
        self._renderer = renderer
        self._event_queue = event_queue
        self._dp = dp
        self._play_again = False

    def start(self):
        self._draw.first_roll()
        self._draw.print_rules()
        self._draw.print_scoreboard()
        
        while True:
            if self._traverse_event() is False:
                break
            self._render()
            self._clock.tick(60)

    def _traverse_event(self):
        for event in self._event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = event.pos[0], event.pos[1]

                if event.button == 1:
                    self._draw.roll_dice(mouse_x, mouse_y, ('a'))
                    self._draw.get_hand(mouse_x, mouse_y)
                    
            if event.type == pygame.KEYDOWN:
                
                self._draw.select_dice(event.key)
                self._draw.unlock(event.key)
                self._draw.roll_dice(1, 1, event.key)

            
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
