import pygame


class GameLoop:
    def __init__(self, draw, renderer, clock, event_queue):
        self._draw = draw
        self._clock = clock
        self._renderer = renderer
        self._event_queue = event_queue

    def start(self):
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
                    self._draw.roll_dice(mouse_x, mouse_y)

            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
