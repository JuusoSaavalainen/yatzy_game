import pygame
import os
from src.load_image import load_image
# path to file
direc_name = os.path.dirname(__file__)

# Class for roll sprite
class Roll(pygame.sprite.Sprite):
    '''Class that could be replaced but
    it is used to store and call the rolling button'''
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = load_image("roll.png")

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y
