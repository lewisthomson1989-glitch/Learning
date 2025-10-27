import pygame
from pygame.locals import *

pygame.init()


screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Knots_And_Crosses")

line_width = 6
markers = []
clicked = False
pos = (0, 0)
player = 1
winner = 0
game_over = False

green = (126, 204, 147)
red = (173, 83, 76)
blue = (77, 127, 201)

# Define font
font = pygame.font.SysFont(None, 40)

# create play again rectangle
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

for x in range(3):
    row = [0] * 3
    markers.append(row)


def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(
            screen, grid, (0, x * 100), (screen_width, x * 100), line_width
        )
        pygame.draw.line(
            screen,
            grid,
            (x * 100, 0),
            (
                x * 100,
                screen_height,
            ),
            line_width,
        )


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(
                    screen,
                    green,
                    (x_pos * 100 + 15, y_pos * 100 + 15),
                    (x_pos * 100 + 85, y_pos * 100 + 85),
                    line_width,
                )
                pygame.draw.line(
                    screen,
                    green,
                    (x_pos * 100 + 15, y_pos * 100 + 85),
                    (x_pos * 100 + 85, y_pos * 100 + 15),
                    line_width,
                )
            if y == -1:
                pygame.draw.circle(
                    screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width
                )
            y_pos += 1
        x_pos += 1


def check_winner():
    global winner
    global game_over

    x_pos = 0
    for x in markers:
        # check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True

        # check rows
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == -3:
            winner = 2
            game_over = True
        x_pos += 1

    # check cross (outside the for loop)
    if (
        markers[0][0] + markers[1][1] + markers[2][2] == 3
        or markers[2][0] + markers[1][1] + markers[0][2] == 3
    ):
        winner = 1
        game_over = True
    if (
        markers[0][0] + markers[1][1] + markers[2][2] == 3
        or markers[2][0] + markers[1][1] + markers[0][2] == -3
    ):
        winner = 2
        game_over = True

    if game_over == False:
        tie = True
        for row in markers:
            for i in row:
                if i == 0:
                    tie = False

        if tie == True:
            game_over = True
            winner = 0


def draw_winner(winner):
    if winner != 0:
        win_text = "Player" + str(winner) + " wins!"
    elif winner == 0:
        win_text = "you have tied!"

    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(
        screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50)
    )
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = "Play Again?"
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


run = True
while run:
    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()

    if game_over == True:
        draw_winner(winner)
        # check for mouseclick to see if player has clicked on Play Again:

        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset vairables
                markers = []
                pos = (0, 0)
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0] * 3
                    markers.append(row)

    pygame.display.update()


pygame.quit()
