import pygame
import math
import numpy as np
from scipy.signal import convolve2d

class Board:
    def __init__(self,row,col,origin,radius):
        self.row = row
        self.col = col
        self.origin = origin
        self.radius = radius
        self.position = [[0] * self.col for _ in range(self.row)]
        self.piece = [[(255,255,255)] * self.col for _ in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                self.position[i][j] = (self.origin[0]+j*self.radius*2.1,self.origin[1]+i*self.radius*2.1)
        
        horizontal_kernel = np.array([[1,1,1,1]])
        vertical_kernel = np.transpose(horizontal_kernel)
        diag1_kernel = np.eye(4,dtype=np.uint8)
        diag2_kernel = np.fliplr(diag1_kernel)
        self.detection_kernel = [horizontal_kernel,vertical_kernel,diag1_kernel,diag2_kernel]


            
    
    def draw(self,surface):
        for i in range(self.row):
            for j in range(self.col):
                pygame.draw.circle(surface,color = self.piece[i][j],center=self.position[i][j],radius=self.radius)

    def get_pos(self,pos):
        for i in range(self.row):
            for j in range(self.col):
                distance = math.hypot(pos[0] - self.position[i][j][0],pos[1] - self.position[i][j][1])
                if distance <= self.radius:
                    return (i,j)
        
        return None
    
    def put_object(self,color,pos):
        for k in reversed(range(self.row)):
            if self.piece[k][pos[1]] == (255,255,255):
                self.piece[k][pos[1]] = color 
                break
        win = self.check_if_connect_4(color)

        return win
        
   
    
    def check_if_connect_4(self,color):
        board = self.turn_board(color)
        for kernel in self.detection_kernel:
            if (convolve2d(board,kernel,mode="valid") == 4).any():
                return True
        return False


    def turn_board(self,color):
        board = [[0]*self.row for _ in range(self.col)]
        for i in range(self.row):
            for j in range(self.col):
                if self.piece[i][j] == color:
                    board[i][j] = 1
        
        return board
    
