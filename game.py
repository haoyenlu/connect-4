import pygame
import board

pygame.init()

screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))


running = True

radius = 30

Board = board.Board(7,7,(50,50),radius)


piece = {"blue":(0,0,255),"red":(255,0,0)}

turn = "blue"

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = Board.get_pos(event.pos)
            if pos != None:
                win = Board.put_object(piece[turn],pos)
                
                print(win)
                turn = "red" if turn == "blue" else "blue"

            

    Board.draw(screen)

    pygame.display.update()