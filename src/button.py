import pygame
from pieces import *

class Button():
    def __init__(self, color, x,y,width,height, text='',alliance = None,rank = None,img = None): #piece to take in piece object (to be set during setup when click)
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.button_surface = pygame.Surface((self.width,self.height), pygame.SRCALPHA)   # per-pixel alpha

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        self.button_surface.fill(self.getColor())
        win.blit(self.button_surface, (self.x, self.y))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 12)
            text = font.render(self.text, 1, (0,0,0))
            #Position the text on the center of the button
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def isPressed(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        mouseClick = pygame.mouse.get_pressed()
        if mouseClick[0] == True and self.isOver(pos):
            return True

        return False

    def getColor(self):
        #get button color
        return self.color

    def setColor(self,color):
        #set color of button
        self.color = color

    def update(self,color):
        self.setColor(color)

    def setPiece(alliance,rank,image):
        self.alliance=alliance
        self.rank=rank
        img=image

