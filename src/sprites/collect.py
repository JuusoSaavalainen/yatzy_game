import pygame
import os
from src.load_image import load_image

direc_name = os.path.dirname(__file__)

class Collect(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = load_image("collect.png")

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y
