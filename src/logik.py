import pygame
import random
from src.sprites.collect import Collect
from src.sprites.dice import Dice
from src.sprites.roll import Roll


class Draw:
    def __init__(self, yatzy_board):
        self.dice1 = pygame.sprite.Group()
        self.dice2 = pygame.sprite.Group()
        self.dice3 = pygame.sprite.Group()
        self.dice4 = pygame.sprite.Group()
        self.dice5 = pygame.sprite.Group()
        self.dice6 = pygame.sprite.Group()
        self.collect = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.dices = pygame.sprite.Group()

        self._intialize_sprites(yatzy_board)

    def _intialize_sprites(self, yatzy_board):

        self.dice1.add(Dice(100, 0, 1))
        self.dice2.add(Dice(200, 0, 1))
        self.dice3.add(Dice(300, 0, 1))
        self.dice4.add(Dice(400, 0, 1))
        self.dice5.add(Dice(500, 0, 1))
        self.dice6.add(Dice(600, 0, 1))
        self.roll = Roll(750, 0)
        self.collect.add(Collect(750, 50))

        self.all_sprites.add(
            self.dice1,
            self.dice2,
            self.dice3,
            self.dice4,
            self.dice5,
            self.dice6,
            self.roll,
            self.collect)

        self.dices.add(
            self.dice1,
            self.dice2,
            self.dice3,
            self.dice4,
            self.dice5,
            self.dice6,
        )

    def roll_dice(self, x, y):
        if self.roll.rect.collidepoint(x, y):
            for dice in self.dices:
                dice.number = random.randint(1, 6)
                dice.update()
