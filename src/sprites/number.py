import pygame
import os
from src.load_image import load_image

# path to file
direc_name = os.path.dirname(__file__)

# Class for number sprite
class NumValues(pygame.sprite.Sprite):
    '''Class that is used to store and refer the
    round number in the game. Is used everytime that rolling 
    happens and stores the all possible values for rolls left.'''
    def __init__(self, x=0, y=0, number=0):
        super().__init__()

        self.number = number
        self.imgs_dict = self._load_img()
        self.image = self.imgs_dict["3"]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = self.imgs_dict[str(self.number)]

    def _load_img(self):
        imgs = {'1': load_image("one.png"),
                '2': load_image("two.png"),
                '3': load_image("three.png"),}
        return imgs