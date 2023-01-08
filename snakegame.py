import os
import random
from time import sleep
trys = 0
while True:
    try:
        import pygame
        break
    except ImportError:
        os.system("pip install pygame --pre")
        sleep(10)
    trys += 1
    if trys == 3:
        print("Failed to install pygame")
        break

pygame.init()
black = (0, 0, 0)
white = (230, 230, 230)
yellow = (255, 255, 102)
grey = (200, 200, 200)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
window_height = 800
window_width = 800
snake_block = 20
snake_speed = 12
def Your_score(score):
    value = pygame.font.SysFont(None, 30).render("Your Score: " + str(score), True, red)
    SCREEN.blit(value, [0, 0])


def gameloop():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Snake Game')
    CLOCK = pygame.time.Clock()
    over = False
    gameclose = False
    lastpressed = None
    snake_list = []
    length_of_snake = 1
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(0, window_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, window_height - snake_block) / 20.0) * 20.0
    while not over:
        while gameclose == True:
            SCREEN.fill(white)
            message("game over, press c to play again or q to quit", red)
            Your_score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        over = True
                        gameclose = False
                    if event.key == pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lastpressed != "right":
                    x1_change = -snake_block
                    y1_change = 0
                    lastpressed = "left"
                elif event.key == pygame.K_RIGHT and lastpressed != "left":
                    x1_change = snake_block
                    y1_change = 0
                    lastpressed = "right"
                elif event.key == pygame.K_UP and lastpressed != "down":
                    y1_change = -snake_block
                    x1_change = 0
                    lastpressed = "up"
                elif event.key == pygame.K_DOWN and lastpressed != "up":
                    y1_change = snake_block
                    x1_change = 0
                    lastpressed = "down"
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            gameclose = True
        x1 += x1_change
        y1 += y1_change
        SCREEN.fill(white)
        drawGrid()
        pygame.draw.rect(SCREEN, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                gameclose = True
        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, window_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            while True:
                colision = False
                for segment in snake_list:
                    segmentindex = snake_list.index(segment)
                    if segment == [foodx, foody] and segmentindex != len(snake_list) - 1:
                        colision = True
                        foodx = round(random.randrange(0, window_width - snake_block) / 20.0) * 20.0
                        foody = round(random.randrange(0, window_height - snake_block) / 20.0) * 20.0
                        break
                else:
                    break
        CLOCK.tick(snake_speed)
def drawGrid():
    blockSize = 20
    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, grey, rect, 1)


def our_snake(snake_block, snake_list):
    for segment in range(len(snake_list)):
        green_value = 255 - (segment * 5)
        blue_value = 0 + (segment * 5)
        if green_value < 0:
            green_value = 0
        if blue_value > 255:
            blue_value = 255
        segment_color = (0, green_value, blue_value)
        pygame.draw.rect(SCREEN, black, [snake_list[segment][0] - 1, snake_list[segment][1] - 1, snake_block + 2, snake_block + 2], 1)
        pygame.draw.rect(SCREEN, segment_color, [snake_list[segment][0], snake_list[segment][1], snake_block, snake_block])

def message(msg, color):
    mesg = pygame.font.SysFont(None, 30).render(msg, True, color)
    SCREEN.blit(mesg, [window_width / 6, window_height / 3])





gameloop()