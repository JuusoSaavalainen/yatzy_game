import pygame

class EventQueue:
    '''Helper for the traverse event'''
    def get(self):
        return pygame.event.get()
