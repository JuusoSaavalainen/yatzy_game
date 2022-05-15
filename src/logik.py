import pygame
import random

from src.data.database_connection import get_database_connection
from src.repot.yatzyrepo import Loginrepo
from src.rules import Checkrules
from src.yatzy_scoreboard import Scoreboard
from src.sprites.turns import Turns
from src.sprites.number import NumValues
from src.sprites.dice import Dice
from src.sprites.roll import Roll
from src.sprites.lock import Lock


class Draw:
    '''Luokka jonka avulla pelin logiikkaa ylläpidetään ja joitakin komponenttejä piirretään
    
    Attributes:
        possible_score = list that includes booleans for every possible score
        selectedlist = list that indicates if dice is lockd 
        dice_names = list that is used to store values of the hanb
        score_pointer = pointer that indicates the score that user tries to click
        draw_pointer = pointer that indicates the place that user is trying to click
        dp = display of the game
        calculator = round calculator
        game_sum = tells the total score of a current game
        up_score = tells the total score of upperbracket used to show the current upscore
        counter_up = helps to specify the round and turn
        rounds = value of avaible rounds in game

    Args:
        dp = takes the wanted display to use
        name = currently still working on this  -> will be the username of current player
    '''


    def __init__(self, dp):
        '''Constructor of the class that also intializes the sprites

        Args:
        dp = takes the wanted display to use
        name = currently still working on this  -> will be the username of current player'''

        self.possible_score = [False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.done_score = [False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.selectedlist = [False,False,False,False,False]
        self.dice_names = []
        self.score_pointer = -1
        self.draw_pointer = -1
        self.dp = dp
        self.calculator = 3
        self.game_sum = 0
        self.up_score = 0
        self.counter_up = 0
        self.rounds = 13

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

        self.roll = Roll(750, 100)
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
        ''' Method that intializes fonts'''
        self.rulesfont = pygame.font.Font(None, 27)
        self.ggfont = pygame.font.Font(None, 47)
        self.pointfont = pygame.font.Font(None, 30)


    def print_scoreboard(self):
        '''Method that draws the scorecard'''
        self.ones = Scoreboard(0,200,'1s', self.done_score[0])
        self.twos = Scoreboard(0,240,'2s', self.done_score[1])
        self.threes = Scoreboard(0,280,'3s', self.done_score[2])
        self.fours = Scoreboard(0,320,'4s', self.done_score[3])
        self.fives = Scoreboard(0,360,'5s', self.done_score[4])
        self.sixes = Scoreboard(0,400,'6s', self.done_score[5])
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
        pygame.draw.rect(self.dp, (0, 0, 0), pygame.Rect(1,441,350,39))  
        board_text = self.pointfont.render('^ Upperscore ^', True, (74,155,74))
        self.dp.blit(board_text, (10, 450))

    def print_rules(self):
        '''This method is used to draw the instrucktions to the screen'''
        self.initialize_fonts()
        text = self.rulesfont.render('- You can choose the score to pick or overwrite by clicking the field', True, (255,255,255))
        text2 = self.rulesfont.render('- With *number* keys you can lock dices and with *u* you can unlock all', True, (255,255,255))
        text3 = self.rulesfont.render('- Each round you hace 3 rolls and in the whole game you have 13 rounds', True, (255,255,255))
        text4 = self.rulesfont.render('- You can roll the dices by pressing Roll~ or *spacebar*', True, (255,255,255))
        text5 = self.rulesfont.render('- Bonus can be claimed by having uppertotal > 62', True, (255,255,255))
        text6 = self.rulesfont.render('- The goal of the game is to obtain as many points as possible', True, (255,255,255))
        self.dp.blit(text3,(350,290))
        self.dp.blit(text,(350,330))     
        self.dp.blit(text2,(350,370)) 
        self.dp.blit(text4,(350,410))
        self.dp.blit(text5,(350,450))
        self.dp.blit(text6,(350,250))


    def first_roll(self):
        '''Method that is avare of the rounds and is used to reset the roll after scoring
        and for updating the database scores after game ends'''
        if self.rounds == 0:
            connection = get_database_connection()
            helper_1 = Loginrepo(connection)
            helper_1.update_score(self.game_sum)
            text = self.ggfont.render(f'Game over, GG! Your score was {self.game_sum}', True, (1,255,255))
            text0 = self.ggfont.render(f'Press right upper corner (X) to exit', True, (1,255,255))
            text2 = self.ggfont.render('Press "J" to play again! ' , True, (1,255,255))
            self.dp.blit(text,(330,550))
            self.dp.blit(text2,(330,600))
            self.dp.blit(text0,(330,650))

        for i,dice in enumerate(self.dices):
                    if self.selectedlist[i] != True:
                        dice.number = random.randint(1, 6)
                        dice.update()
                        
    def roll_dice(self, x, y, key):
        '''This method is used for the regular roll
        Args:
            x,y = used for keeping up with the points of screen that are used
            key = used bcs the space roll option, basicly used to see if spacebar is pressed
        '''
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
        ''' Method to collect info about the dices that are currently on screen
        Args:
            x,y = to keep up with the clicks on monitor
        '''
        self.dice_names = []
        for dice in self.dices:
            self.dice_names.append(dice.number)
        score = self.dice_names
        self.dice_names = []
        self.click_score(score,x,y)


    def select_dice(self, key):
        '''Method used to set the dices to lock mode
        Args:
            Key = indicates the key that is pressed for knowing witch dice to lock
        '''
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
        '''Method that is used for releasing the lockd dices
        Args: 
            key = indicated the pressed key
        '''
        if key == pygame.K_u:
            for i,lock in enumerate(self.locks):
                lock.number = 1
                lock.update()
                self.selectedlist[i] = False
                

    def click_score(self, score, x, y):
        '''Method used for checking the clicks of the scorecard
        Args:
            score = takes in the current score to be used on the choice method as an imput
            x,y = indicates the position of a click
        '''
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
        '''Method used for updating the scorecard , checking the avaible score options and
        handeling the 0 roll situation

        Args:
            All arguments are just info from the click method to know the parameters
            for filling the right scores to right places
        '''
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

            if self.score_pointer <= 5:
                self.up_score += points
            
            if self.up_score >= 63:
                self.game_sum += 50
                self.up_score += 50
                bonus = self.pointfont.render(('50'), True, (255,255,255))
                self.dp.blit(bonus,(240,490))

            self.done_score[score_pointer] = True
            self.game_sum += points
            text = self.pointfont.render(str(points), True, (255,255,255))
            text2 = self.pointfont.render(str(self.game_sum), True, (255,155,155))
            text3 = self.pointfont.render(str(self.up_score), True, (74,155,74))
            pygame.draw.rect(self.dp, (0, 0, 0), pygame.Rect(201,841,98,37))  
            pygame.draw.rect(self.dp, (0, 0, 0), pygame.Rect(201,521,98,37))
            self.dp.blit(text,(240,draw_pointer+10))
            self.dp.blit(text2,(240,850))
            self.dp.blit(text3,(240,530))
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