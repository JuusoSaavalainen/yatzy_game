import pygame

class Renderer:
    def __init__(self, disp, draw):
        self._display = disp
        self._draw = draw

    def render(self):
        self._draw.all_sprites.draw(self._display)

        pygame.display.update()
