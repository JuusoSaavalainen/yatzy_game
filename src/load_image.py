import pygame
import os

dirname = os.path.dirname(__file__)

def load_image(file):
    '''Function to handle the path for dowloading images'''
    return pygame.image.load(os.path.join(dirname, "assets", file))
