import pygame
import random

from src.rules import Checkrules
from src.yatzy_scoreboard import Scoreboard
from src.sprites.turns import Turns
from src.sprites.number import NumValues
from src.sprites.collect import Collect
from src.sprites.dice import Dice
from src.sprites.roll import Roll
from src.sprites.lock import Lock


class Draw:
    def __init__(self, dp):

        self.possible_score = [False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.done_score = [False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.selectedlist = [False,False,False,False,False]
        self.dice_names = []
        self.score_pointer = -1
        self.draw_pointer = -1
        self.dp = dp
        self.calculator = 3
        self.dice_sum = 0
        self.game_sum = 0
        self.counter_up = 0
        self.rounds = 13
        self.warning = False
        self.duplicates = False

        self.dice1 = pygame.sprite.Group()
        self.dice2 = pygame.sprite.Group()
        self.dice3 = pygame.sprite.Group()
        self.dice4 = pygame.sprite.Group()
        self.dice5 = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()
        self.dices = pygame.sprite.Group()
        self.turns = pygame.sprite.Group()
        self.numbers = pygame.sprite.Group()

        self.locks = pygame.sprite.Group()
        self.lock1 = pygame.sprite.Group()
        self.lock2 = pygame.sprite.Group()
        self.lock3 = pygame.sprite.Group()
        self.lock4 = pygame.sprite.Group()
        self.lock5 = pygame.sprite.Group()


        self._intialize_sprites()


    def _intialize_sprites(self):             
        self.dice1.add(Dice(100, 60, 1))
        self.dice2.add(Dice(205, 60, 1))
        self.dice3.add(Dice(310, 60, 1))
        self.dice4.add(Dice(415, 60, 1))
        self.dice5.add(Dice(520, 60, 1))

        self.collect = Collect(750, 100)
        self.roll = Roll(750, 30)
        self.turns = Turns(100,0)
        self.numbers = NumValues(400,0,2)

        self.lock1.add(Lock(100,165,1))
        self.lock2.add(Lock(205,165,1))
        self.lock3.add(Lock(310,165,1))
        self.lock4.add(Lock(415,165,1))
        self.lock5.add(Lock(520,165,1))

        self.all_sprites.add(
            self.dice1,
            self.dice2,
            self.dice3,
            self.dice4,
            self.dice5,
            self.roll,
            self.collect,
            self.turns,
            self.numbers,
            self.lock1,
            self.lock2,
            self.lock3,
            self.lock4,
            self.lock5,
        )

        self.locks.add(
            self.lock1,
            self.lock2,
            self.lock3,
            self.lock4,
            self.lock5,
        )

        self.dices.add(
            self.dice1,
            self.dice2,
            self.dice3,
            self.dice4,
            self.dice5
        )

    def initialize_fonts(self):
        self.rulesfont = pygame.font.Font(None, 27)
        self.ggfont = pygame.font.Font(None, 47)
        self.pointfont = pygame.font.Font(None, 30)


    def print_scoreboard(self):
        self.ones = Scoreboard(0,200,'1s', self.done_score[0])
        self.twos = Scoreboard(0,240,'2s', self.done_score[1])
        self.threes = Scoreboard(0,280,'3s', self.done_score[2])
        self.fours = Scoreboard(0,320,'4s', self.done_score[3])
        self.fives = Scoreboard(0,360,'5s', self.done_score[4])
        self.sixes = Scoreboard(0,400,'6s', self.done_score[5])
        self.upscore = Scoreboard(0,440,'TOTAL UP', False)
        self.bonusbasic = Scoreboard(0,480,'Bonus', False)
        self.uptotal = Scoreboard(0,520,'UPPER TOTAL',False)
        self.threekind = Scoreboard(0,560,'3 of a kind', self.done_score[6])
        self.fourkind = Scoreboard(0,600,'4 of a kind', self.done_score[7])
        self.fullhouse = Scoreboard(0,640,'Full House', self.done_score[8])
        self.small_straight = Scoreboard(0,680,'Small Straight', self.done_score[9])
        self.large_straight = Scoreboard(0,720,'Big Straight', self.done_score[10])
        self.yatzee = Scoreboard(0,760,'Yahtzee', self.done_score[11])
        self.chance = Scoreboard(0,800,'Change', self.done_score[12])
        self.grandtotal = Scoreboard(0,840,'GRAND TOTAL', False)
        self.ones.drawit(self.dp)
        self.twos.drawit(self.dp)
        self.threes.drawit(self.dp)
        self.fours.drawit(self.dp)
        self.fives.drawit(self.dp)
        self.sixes.drawit(self.dp)
        self.upscore.drawit(self.dp)
        self.bonusbasic.drawit(self.dp)
        self.uptotal.drawit(self.dp)
        self.threekind.drawit(self.dp)
        self.fourkind.drawit(self.dp)
        self.small_straight.drawit(self.dp)
        self.large_straight.drawit(self.dp)
        self.fullhouse.drawit(self.dp)
        self.yatzee.drawit(self.dp)
        self.chance.drawit(self.dp)
        self.grandtotal.drawit(self.dp)


    def print_rules(self):
        self.initialize_fonts()
        text = self.rulesfont.render('- You can choose the score to pick or overwrite by clicking the field', True, (255,255,255))
        text2 = self.rulesfont.render('- With *number* keys you can lock dices and with *u* you can unlock all', True, (255,255,255))
        text3 = self.rulesfont.render('- Each round you hace 3 rolls and in the whole game you have 13 rounds', True, (255,255,255))
        text4 = self.rulesfont.render('- You can roll the dices by pressing Roll~ or *spacebar*', True, (255,255,255))
        self.dp.blit(text3,(350,410))
        self.dp.blit(text,(350,450))     
        self.dp.blit(text2,(350,490)) 
        self.dp.blit(text4,(350,530))

    def first_roll(self):
        if self.rounds == 0:
            text = self.ggfont.render(f'Game over, GG! Your score was {self.game_sum}', True, (255,255,255))
            text2 = self.ggfont.render('insert instructions to playagain here<-', True, (255,255,255))
            self.dp.blit(text,(330,850))
            self.dp.blit(text2,(330,900))
        for i,dice in enumerate(self.dices):
                    if self.selectedlist[i] != True:
                        dice.number = random.randint(1, 6)
                        dice.update()

    def roll_dice(self, x, y, key):
        if self.rounds > 0 and (self.counter_up + self.rounds) == 13:
            if self.roll.rect.collidepoint(x, y) or key == pygame.K_SPACE:
                if self.calculator == 1:
                    return   
                self.calculator -= 1 
                self.numbers.number = self.calculator
                self.numbers.update()
                for i,dice in enumerate(self.dices):
                    if self.selectedlist[i] != True:
                        dice.number = random.randint(1, 6)
                        dice.update()
                
    

    def get_hand(self, x, y):
        self.dice_names = []
        for dice in self.dices:
            self.dice_names.append(dice.number)
        score = self.dice_names
        self.dice_names = []
        self.click_score(score,x,y)


    def select_dice(self, key):
        if key == pygame.K_1:
            if self.selectedlist[0]:
                self.selectedlist[0] = False
            if self.selectedlist[0] == False:
                self.selectedlist[0] = True  

        if key == pygame.K_2:
            if self.selectedlist[1]:
                self.selectedlist[1] = False
            if self.selectedlist[1] == False:
                self.selectedlist[1] = True  

        if key == pygame.K_3:
            if self.selectedlist[2]:
                self.selectedlist[2] = False
            if self.selectedlist[2] == False:
                self.selectedlist[2] = True   

        if key == pygame.K_4:
            if self.selectedlist[3]:
                self.selectedlist[3] = False
            if self.selectedlist[3] == False:
                self.selectedlist[3] = True   

        if key == pygame.K_5:
            if self.selectedlist[4]:
                self.selectedlist[4] = False
            if self.selectedlist[4] == False:
                self.selectedlist[4] = True 

        for i,lock in enumerate(self.locks):
            if self.selectedlist[i] == True:
                lock.number = 2
                lock.update()

    def unlock(self, key):
        if key == pygame.K_u:
            for i,lock in enumerate(self.locks):
                lock.number = 1
                lock.update()
                self.selectedlist[i] = False
                

    def click_score(self, score, x, y):
        if 0 <= x <= 300:
            if 200 < x < 400 or 560 < x < 800:
                if 200 < y < 240:
                    self.score_pointer = 0
                    self.draw_pointer = 200
                elif 240 < y < 280:
                    self.score_pointer = 1
                    self.draw_pointer = 240
                elif 280 < y < 320:
                    self.score_pointer = 2
                    self.draw_pointer = 280
                elif 320 < y < 360:
                    self.score_pointer = 3
                    self.draw_pointer = 320
                elif 360 < y < 400:
                    self.score_pointer = 4
                    self.draw_pointer = 360
                elif 400 < y < 440:
                    self.score_pointer = 5
                    self.draw_pointer = 400
                elif 560 < y < 600:
                    self.score_pointer = 6
                    self.draw_pointer = 560
                elif 600 < y < 640:
                    self.score_pointer = 7
                    self.draw_pointer = 600
                elif 640 < y < 680:
                    self.score_pointer = 8
                    self.draw_pointer = 640
                elif 680 < y < 720:
                    self.score_pointer = 9
                    self.draw_pointer = 680
                elif 720 < y < 760:
                    self.score_pointer = 10
                    self.draw_pointer = 720
                elif 760 < y < 800:
                    self.score_pointer = 11
                    self.draw_pointer = 760
                elif 800 < y < 840:
                    self.score_pointer = 12
                    self.draw_pointer = 800
                self.selected_score = self.choice(score, self.score_pointer,self.draw_pointer)
        
    def choice(self,score, score_pointer,draw_pointer):
        if self.done_score[score_pointer]:
            return

        helpers = Checkrules()
        helper2 = helpers.possibility_all(self.possible_score,score)

        if helper2[score_pointer]:
            self.numbers.number = 3
            self.calculator = 3
            self.numbers.update()
            self.rounds -= 1
            points = helpers.points(score, score_pointer)
            self.done_score[score_pointer] = True
            text = self.pointfont.render(str(points), True, (255,255,255))
            self.dp.blit(text,(240,draw_pointer+10))       
            self.game_sum += points
            self.counter_up += 1
            self.unlock(pygame.K_u)
            self.first_roll()
            
        else:
            self.numbers.number = 3
            self.calculator = 3
            self.numbers.update()
            self.rounds -= 1
            self.done_score[score_pointer] = True
            text = self.pointfont.render('0', True, (255,255,255))
            self.dp.blit(text,(240,draw_pointer+10))       
            self.counter_up += 1
            self.unlock(pygame.K_u)
            self.first_roll()