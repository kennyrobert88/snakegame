import time, pygame, random 
pygame.init()
# Using pygame for the GUI
displayWidth = 800
displayHeight = 600
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.update()
pygame.display.set_caption("Snake game")
blue, red, white, black, green, yellow = (0, 0, 155), (255, 0, 0), (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 255, 102)
clock = pygame.time.Clock()
snakeBlock, snakeSpeed = 10, 15

fontStyle, scoreFont = pygame.font.SysFont("bahnschrift", 25), pygame.font.SysFont("comicsansms", 35)
# The while loop that runs the game
fontStyle = pygame.font.SysFont(None, 50)

def ourSnake(snakeBlock, snakeList):
    for s in snakeList:
        pygame.draw.rect(display, black, [s[0], s[1], snakeBlock, snakeBlock])

def yourScore(score):
    value = scoreFont.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])

def message(msg, color):
    mesg = fontStyle.render(msg, True, color)
    display.blit(mesg, [displayWidth / 14, displayHeight / 4])
    
def gameLoop():
    gameOver, gameClose = False, False
    xPosition, yPosition = displayWidth / 2, displayHeight / 2
    xPositionChange, yPositionChange = 0, 0
    snakeList = []
    lengthOfSnake = 1
    xFood, yFood = round(random.randrange(0, displayWidth - snakeBlock) / 10.0) * 10, round(random.randrange(0, displayHeight - snakeBlock) / 10.0) * 10

    while not gameOver:
        # Creating menu bar
        while gameClose == True:
            display.fill(blue)
            message("You Lost! Please press Q-quit and C-start", red)
            yourScore(lengthOfSnake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver, gameClose = True, False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            # print(event) # This become all the logs
            # Adding breakout from the loops
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xPositionChange, yPositionChange = -snakeBlock, 0
                elif event.key == pygame.K_RIGHT:
                    xPositionChange, yPositionChange = snakeBlock, 0
                elif event.key == pygame.K_UP:
                    xPositionChange, yPositionChange = 0, -snakeBlock
                elif event.key == pygame.K_DOWN:
                    xPositionChange, yPositionChange = 0, snakeBlock       
        # Using logic for the game
        if xPosition < 0 or yPosition < 0 or xPosition >= displayWidth or yPosition >= displayHeight:
            gameClose = True
        xPosition += xPositionChange
        yPosition += yPositionChange
        display.fill(white)
        pygame.draw.rect(display, green, [xFood, yFood, snakeBlock, snakeBlock])
        snakeList.append([xPosition, yPosition])

        if len(snakeList) > lengthOfSnake:
            del snakeList[0]
        
        for s in snakeList[:-1]:
            if s == [xPosition, yPosition]:
                gameClose = True
        ourSnake(snakeBlock, snakeList)
        yourScore(lengthOfSnake - 1)
        pygame.display.update()
        if xPosition == xFood and yPosition == yFood:
            print("Yummy!!")
            xFood, yFood = round(random.randrange(0, displayWidth - snakeBlock) / 10.0) * 10, round(random.randrange(0, displayHeight - snakeBlock) / 10.0) * 10
            lengthOfSnake += 1
        clock.tick(snakeSpeed)
    pygame.quit()
    quit()
gameLoop()