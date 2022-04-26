import pygame

class Scoreboard:
    def __init__(self, x, y, text, done):
        self.x = x
        self.y = y
        self.text = text
        self.done = done

    def drawit(self,dp):
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, (15,255,255))
        pygame.draw.line(dp,(255,150,10),(self.x, self.y),(self.x + 300, self.y))
        pygame.draw.line(dp,(255,150,10),(self.x, self.y + 40),(self.x+ 300, self.y + 40))
        dp.blit(text,(self.x + 10, self.y + 10))        
        pygame.draw.line(dp,(255,150,10), (200, 200), (200,880))
        pygame.draw.line(dp,(255,150,10), (300, 200), (300,880))

    