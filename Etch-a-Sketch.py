import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Etch-a-Sketch')

FPS = 10

clock = pygame.time.Clock()

pygame.display.update()

def gameLoop():
    gameExit = False

    rect_x = 300
    rect_y = 400

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rect_y -= 10
                elif event.key == pygame.K_RIGHT:
                    rect_y += 10
                elif event.key == pygame.K_UP:
                    rect_x -= 10
                elif event.key == pygame.K_DOWN:
                    rect_x += 10

        pygame.draw.rect(gameDisplay, black, (rect_x, rect_y), 10)

    pygame.display.update()

    clock.tick(FPS)

gameLoop()