import pygame


class Clock:
    '''Class used to controll and get and set the clocks of game (fps)'''
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        self._clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()
