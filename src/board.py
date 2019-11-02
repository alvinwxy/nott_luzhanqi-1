import pygame
import operator
from button import Button

class Board:
    def __init__(self,width,height,numRow,numCol):
        self.red = pygame.Color(200,50,50)
        self.green = pygame.Color(50,200,50)
        self.yellow = pygame.Color(200,200,50)
        self.blue = pygame.Color(50,50,200)
        self.purple = pygame.Color(200,50,200)
        self.width = width
        self.height = height
        self.numRow = numRow
        self.numCol = numCol
        self.board = self.initialise()
        self.button = self.initialiseButton()

    def initialise(self):
        """Initialise the game board"""
        #Set all as Soldier Station
        board = [["SS" for j in range(self.numCol)] for i in range(self.numRow)]

        #Setting Camp
        board[2][1] = "CP"
        board[2][3] = "CP"
        board[3][2] = "CP"
        board[4][1] = "CP"
        board[4][3] = "CP"
        board[8][1] = "CP"
        board[8][3] = "CP"
        board[9][2] = "CP"
        board[10][1] = "CP"
        board[10][3] = "CP"

        #Setting Headquarters
        board[0][1] = "HQ"
        board[0][3] = "HQ"
        board[12][1] = "HQ"
        board[12][3] = "HQ"

        #Setting Front Line
        board[6][0] = "FL"
        board[6][2] = "FL"
        board[6][4] = "FL"

        #Setting Mountain Border
        board[6][1] = "MB"
        board[6][3] = "MB"

        return board

    def initialiseButton(self):
        color = (200,200,200)
        button = [[Button(color,i*self.width,j*self.height,self.width,self.height,"placeholder") for i in range(self.numCol)] for j in range(self.numRow)]

        for i in range(self.numRow):
            for j in range(self.numCol):
                color = Board.updateColor(self,self.board[i][j])

                button[i][j].setColor(color)

        return button


    def draw(self,surface):
        """Draw the Board"""
        for j in range(self.numCol):
            for i in range(self.numRow):
                self.button[i][j].draw(surface,2)

    def updateColor(self,gridType):
        if gridType == "SS":
            color = self.red
        elif gridType == "CP":
            color = self.green
        elif gridType == "HQ":
            color = self.yellow
        elif gridType == "FL":
            color = self.blue
        elif gridType == "MB":
            color = self.purple

        return color

    def update(self,pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        for i in range(self.numRow):
            for j in range(self.numCol):
                if self.button[i][j].isPressed(pos):
                    #make button darker
                    color = tuple(x + y for x, y in zip(self.button[i][j].getColor(), (-100,-100,-100)))
                elif self.button[i][j].isOver(pos):
                    #make button brighter
                    color = tuple(x + y for x, y in zip(self.button[i][j].getColor(), (50,50,50)))
                else:
                    color = Board.updateColor(self,self.board[i][j])

                invalidColor = False
                for k in range(3):
                    if color[k] > 255 or color[k] < 0:
                        invalidColor = True
                
                if not invalidColor:
                    self.button[i][j].update(color)
