import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Etch-a-Sketch')

pygame.display.update()


def gameLoop():
    gameExit = False

    rect_x = 300
    rect_y = 400

    move_left = False
    move_right = False
    move_up = False
    move_down = False

    gameDisplay.fill(white)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                    move_right = False
                    move_up = False
                    move_down = False
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                    move_left = False
                    move_up = False
                    move_down = False
                elif event.key == pygame.K_UP:
                    move_up = True
                    move_left = False
                    move_right = False
                    move_down = False
                elif event.key == pygame.K_DOWN:
                    move_down = True
                    move_left = False
                    move_right = False
                    move_up = False

        if move_left == True:
            rect_x -= 5
        elif move_right == True:
            rect_x += 5
        elif move_up == True:
            rect_y -= 5
        elif move_down == True:
            rect_y += 5

        pygame.draw.rect(gameDisplay, black, [rect_x, rect_y, 5, 5])
        pygame.display.update()


gameLoop()
