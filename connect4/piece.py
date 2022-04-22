import pygame
from .constant import DIAMETER, RADIUS
class Piece:
    PADDING = 5
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color 
        self.posX = 0
        self.posY = 0
        self.calc_pos()
        
    def calc_pos(self):
        self.posX = DIAMETER * self.col + RADIUS
        self.posY = DIAMETER * self.row + RADIUS
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.posX,self.posY), RADIUS - self.PADDING, 100 )
    
    def get_color(self):
        return self.color
        