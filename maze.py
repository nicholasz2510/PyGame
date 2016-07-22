import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Maze')

maze1 = pygame.image.load('maze1.png')

list_of_barriers = [[[[244, 176], [567, 232]], [[0, 0], [800, 30]], [[766, 0], [800, 600]], [[0, 570], [800, 600]],
                 [[0, 0], [30, 600]]], ]

list_of_portals = [[[, ], [, ]], ]

pygame.display.update()

# Return False when touching barrier, return True when not touching barrier
def can_move(barriers, rect_x, rect_y):
    for rect in barriers:
        top_left_point = rect[0]
        bottom_right_point = rect[1]
        if rect_x > top_left_point[0] and rect_x < bottom_right_point[0] and rect_y > top_left_point[1] and rect_y < bottom_right_point[1]:
            return False
    return True


def portal(points, rect_x, rect_y):
    for portal in points:
        top_left_point = portal[0]
        bottom_right_point = portal[1]
        if rect_x > top_left_point[0] and rect_x < bottom_right_point[0] and rect_y > top_left_point[1] and rect_y < bottom_right_point[1]:
            return True
    return False

def next_level():



def gameLoop():
    gameExit = False
    acceleration = 0

    rect_x = 300
    rect_y = 400

    rect_width = 5
    rect_height = 5

    speed = 1

    move_left = False
    move_right = False
    move_up = False
    move_down = False

    walls = list_of_barriers[0]
    portal =

    gameDisplay.fill(white)
    gameDisplay.blit(maze1, (0, 0))

    while not gameExit:
        if (speed * acceleration) < 5:
            acceleration += .001
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not move_left:
                        acceleration = 0
                    move_left = True
                    move_right = False
                    move_up = False
                    move_down = False
                elif event.key == pygame.K_RIGHT:
                    if not move_right:
                        acceleration = 0
                    move_right = True
                    move_left = False
                    move_up = False
                    move_down = False
                elif event.key == pygame.K_UP:
                    if not move_up:
                        acceleration = 0
                    move_up = True
                    move_left = False
                    move_right = False
                    move_down = False
                elif event.key == pygame.K_DOWN:
                    if not move_down:
                        acceleration = 0
                    move_down = True
                    move_left = False
                    move_right = False
                    move_up = False

        if move_left:
            if can_move(walls, rect_x, rect_y):
                rect_x -= (speed * acceleration)
            else:
                rect_x += 1
        elif move_right:
            if can_move(walls, rect_x, rect_y):
                rect_x += (speed * acceleration)
            else:
                rect_x -= 1
        elif move_up:
            if can_move(walls, rect_x, rect_y):
                rect_y -= (speed * acceleration)
            else:
                rect_y += 1
        elif move_down:
            if can_move(walls, rect_x, rect_y):
                rect_y += (speed * acceleration)
            else:
                rect_y -= 1

        if portal(portals, rect_x, rect_y):
            next_level()

        if can_move(walls, rect_x, rect_y):
            pygame.draw.rect(gameDisplay,
                             (acceleration * 195 % 255, acceleration * 195 % 255, acceleration * 195 % 255),
                             [rect_x, rect_y, rect_width, rect_height])
            pygame.display.update()


gameLoop()
