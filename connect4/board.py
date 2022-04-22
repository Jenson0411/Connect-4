import pygame
from connect4.piece import Piece
from .constant import *

class Board:
    PADDING = 5
    def __init__(self):
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
    
    def draw(self, win):
        win.fill(BLUE)
        
        for row in range(0, WIDTH+1,int(DIAMETER)):
            for column in range(0, HEIGHT+1,int(DIAMETER)):
                pygame.draw.circle(win, WHITE, (row+RADIUS,column+RADIUS), RADIUS-self.PADDING, 100)
        
        self.draw_pieces(win)
    
    def calc_row(self, col):
        for row in range(ROWS, 0, -1):
            if(self.board[row-1][col] == 0):
                return row-1
            
    
    
    def draw_pieces(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(win)
    
    def add_piece(self, row, col, color):
        self.board[row][col] = Piece(row, col,color)
        
    def check_win(self, color, row, col):
        return self.check_horizontal(color, row, col) or self.check_vertical(color, row, col) or self.check_diagonal(color, row, col)
        
        
    def check_horizontal(self, color, row, col):
        return (1+self.max_horizontal_left(color, row, col-1) + self.max_horizontal_right(color, row, col+1))>=4
    
    def max_horizontal_left(self, color, row, col):
        if col<0  or col>=COLS:
            return 0
        
        elif self.board[row][col] == 0:
            return 0
        
        elif self.board[row][col].get_color() != color:
            return 0
        
        else:
            return 1+self.max_horizontal_left(color, row, col-1)
        
    def max_horizontal_right(self, color, row, col):
        if col<0  or col>=COLS:
            return 0
        
        elif self.board[row][col] == 0:
            return 0
        
        elif self.board[row][col].get_color() != color:
            return 0
        
        else:
            return 1+self.max_horizontal_right(color, row, col+1)
    
    def check_vertical(self,color, row, col):
         return (1 + self.max_vertical_right(color, row+1, col) + self.max_vertical_left(color, row-1, col))>=4
    
    
    def max_vertical_left(self, color, row, col):
        if row<0  or row>=ROWS:
            return 0
        
        elif self.board[row][col] == 0:
            return 0
        
        elif self.board[row][col].get_color() != color:
            return 0
        
        else:
            return 1+self.max_vertical_left(color, row-1, col)
        
    def max_vertical_right(self, color, row, col):
        if row<0  or row>=ROWS:
            return 0
        
        elif self.board[row][col] == 0:
            return 0
        
        elif self.board[row][col].get_color() != color:
            return 0
        
        else:
            return 1+self.max_vertical_right(color, row+1, col)
        
        
    def check_diagonal(self, color, row, col):
        return (max(1+ self.max_diagonal_top_left(color, row+1, col-1),
                    1+ self.max_diagonal_top_right(color, row+1, col+1),
                    1+ self.max_diagonal_bottom_left(color, row-1, col-1),
                    1+ self.max_diagonal_bottom_right(color, row-1, col+1)))>=4

    
    def max_diagonal_top_right(self, color, row, col):
        if row<0  or row>=ROWS or col<0 or col>=COLS:
            return 0
        
        elif self.board[row][col] == 0:
            return 0
        
        elif self.board[row][col].get_color() != color:
            return 0
        
        else:
            return 1 + self.max_diagonal_top_right(color, row+1, col+1)
    
    def max_diagonal_top_left(self, color, row, col):
        if row<0  or row>=ROWS or col<0 or col>=COLS:
            return 0
        
        elif self.board[row][col] == 0:
            return 0
        
        elif self.board[row][col].get_color() != color:
            return 0
        
        else:
            return 1 + self.max_diagonal_top_left( color, row+1, col-1) 
    
    def max_diagonal_bottom_left(self, color, row, col):
        if row<0  or row>=ROWS or col<0 or col>=COLS:
            return 0
        
        elif self.board[row][col] == 0:
            return 0
        
        elif self.board[row][col].get_color() != color:
            return 0
        
        else:
            return 1 + self.max_diagonal_bottom_left( color, row-1, col-1)
        
    def max_diagonal_bottom_right(self, color, row, col):
        if row<0  or row>=ROWS or col<0 or col>=COLS:
            return 0
        
        elif self.board[row][col] == 0:
            return 0
        
        elif self.board[row][col].get_color() != color:
            return 0
        
        else:
            return 1 + self.max_diagonal_bottom_left( color, row-1, col+1)
        
    def check_board_full(self):
        for row in range(ROWS):
            for col  in range(COLS):
                if(self.board[row][col] == 0):
                    return False
        return True