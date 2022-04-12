
import pygame
import os
from src.load_image import load_image


# path to file
direc_name = os.path.dirname(__file__)

# Class for dice sprite


class Dice(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, number=0):
        super().__init__()

        self.number = number

        self.imgs_dict = self._load_img()

        self.image = self.imgs_dict["1"]

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

    def update(self):
        self.image = self.imgs_dict[str(self.number)]

    def _load_img(self):
        imgs = {'1': load_image("dice1r.png"),
                '2': load_image("dice2r.png"),
                '3': load_image("dice3r.png"),
                '4': load_image("dice4r.png"),
                '5': load_image("dice5r.png"),
                '6': load_image("dice6r.png")}
        return imgs
