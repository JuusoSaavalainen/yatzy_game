import pygame
import os
from src.load_image import load_image
# path to file
direc_name = os.path.dirname(__file__)

# Class for dice sprite
class Lock(pygame.sprite.Sprite):
    '''Class containing the sprites for the lock and unlock
    event in game, Makes possible the (easy)(fast) switch'''
    def __init__(self, x=0, y=0, number=0):
        super().__init__()

        self.selected = False
        self.number = number
        self.imgs_dict = self._load_img()
        self.image = self.imgs_dict["1"]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = self.imgs_dict[str(self.number)]

    def _load_img(self):
        imgs = {'1': load_image("lock.png"),
                '2': load_image("unlock.png"),}
        return imgs

