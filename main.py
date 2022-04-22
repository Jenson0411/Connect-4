import pygame
from connect4 import board
from connect4.constant import *
from connect4.board import Board
from connect4.piece import Piece
import time

board = Board()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect 4')



FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(BLUE)
    game_ended = False
    
    turn = RED
    
    while(run):
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                coord = pygame.mouse.get_pos()
                x = coord[0]
                y = coord[1]
                row = 0
                col = 0
                
                for i in range(0, WIDTH, int(DIAMETER)):
                    if i <= x <= i+ DIAMETER:
                        col = int(i //DIAMETER)
                
                
                row = board.calc_row(col)
                if(row != None ):
                    board.add_piece(row, col, turn)
                    if(board.check_win(turn, row, col)):
                        game_ended = True
                
                    elif(board.check_board_full()):
                        game_ended = True
                        turn = WHITE
                    else:
                        if turn == RED:
                            turn = YELLOW
                        else:
                            turn = RED
        
        if(game_ended):
            break
        else:        
            board.draw(WIN)
            pygame.display.update()     
        
    if(game_ended):
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        
        if turn == RED:
            message = "RED HAS WON"
        elif turn == YELLOW:
            message = "YELLOW HAS WON"
            
        elif turn == WHITE:
            message = "Tie"
        
        text_surface = my_font.render(message, False, (0,0,0))
        WIN.blit(text_surface, (0,0))
        board.draw(WIN)
        WIN.blit(text_surface, (0,0))
        pygame.display.update()  
        time.sleep(2) 
        
    pygame.quit()

main()
