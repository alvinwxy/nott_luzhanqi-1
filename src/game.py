import pygame
from board import Board
pygame.init()

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (247, 255, 0)
black = (0, 0, 0)

mouseX = 0
mouseY = 0

displayX = 1200
displayY = 716   #1 extra pixel to see the last line

board = Board(100,55,13,5)

win=pygame.display.set_mode((700,700))

gameDisplay=pygame.display.set_mode((displayX,displayY))
pygame.display.set_caption("Testing Codes")
gameDisplay.fill(white)

pieceData = {"Field Marshal": [1], "General": [1], "Lieutenant General": [2], "Brigadier": [2], "Colonel": [2], "Major": [2], "Captain": [3], "Platoon Commander": [3], "Engineer": [3], "Landmine": [3], "Bomb": [2], "Flag": [1]}

rankData = {"Field Marshal": 1, "General": 2, "Lieutenant General": 3, "Brigadier": 4, "Colonel": 5, "Major": 6, "Captain": 7, "Platoon Commander": 8, "Engineer": 9, "Landmine": 0, "Bomb": 0, "Flag": "F"}

def genPieceObject(x, y, item, color, showEnemy, drawShadow):

    if drawShadow == True:

        shadowImage = pygame.image.load("bin\Piece Shadow.png")
        gameDisplay.blit(shadowImage, (x + 2, y + 2))

    pieceRect = pygame.Rect(x, y, 50, 50)  #50 by 50 because its the size of the icons
    pygame.draw.rect(gameDisplay, color, pieceRect)

    if color != blue or showEnemy == True or alwaysShowEnemy == True:
            
        image = pygame.image.load("bin\\" + item + ".png")
        gameDisplay.blit(image, (x, y))
        

    return pieceRect


def setupPhase():

    global pieceData, ready

    gameDisplay.fill(white)

    #draws text and pieces beside board
    titleTextObj = pygame.font.Font("bin\OpenSans.ttf", 38)
    titleTextSurfaceObj = titleTextObj.render("PIECES", True, black)
    titleTextRectObj = titleTextSurfaceObj.get_rect()
    titleTextRectObj.center = (925, 75)
    gameDisplay.blit(titleTextSurfaceObj, titleTextRectObj)

    textObj = pygame.font.Font("bin\OpenSans.ttf", 18)

    x = 745
    y = 150

    for item in pieceData:
        #drawing pieces icon

        textSurfaceObj = textObj.render(item, True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (x, y)
        gameDisplay.blit(textSurfaceObj, textRectObj)

        numTextSurfaceObj = textObj.render("x" + str(pieceData[item][0]), True, black)
        numTextRectObj = numTextSurfaceObj.get_rect()
        numTextRectObj.center = (x, y + 100)
        gameDisplay.blit(numTextSurfaceObj, numTextRectObj)

        if pieceData[item][0] != 0:

            ready = False
            pieceRect = genPieceObject(x - 25, y + 25, item, yellow, False, False)
            pieceData[item] = [pieceData[item][0], pieceRect]


        if x > 1050:

            x = 745
            y += 150

        else:
            x += 120
            
    #drawing done icon

    buttonRect = pygame.Rect(displayX - 115, displayY - 55, 100, 40)
    pygame.draw.rect(gameDisplay, red, buttonRect)

    endPhaseTextSurfaceObj = textObj.render("DONE", True, black)
    endPhaseTextRectObj = endPhaseTextSurfaceObj.get_rect()
    endPhaseTextRectObj.center = (buttonRect.left + 50, buttonRect.top + 20)
    gameDisplay.blit(endPhaseTextSurfaceObj, endPhaseTextRectObj)

    if buttonRect.left < mouseX < buttonRect.right and buttonRect.top < mouseY < buttonRect.bottom and mouseClicked == True:
        pieceData = {"Field Marshal": 1, "General": 1, "Lieutenant General": 2, "Brigadier": 2, "Colonel": 2, "Major": 2, "Captain": 3, "Platoon Commander": 3, "Engineer": 3, "Landmine": 3, "Bomb": 2, "Flag": 1}
        gameDisplay.fill(white)
         
            

def drawBoard(board): 
    board.draw(gameDisplay)
    
run=True

setupPhase()

while run:
    pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    board.update(pygame.mouse.get_pos())

    drawBoard(board)

    pygame.display.update()

pygame.quit()