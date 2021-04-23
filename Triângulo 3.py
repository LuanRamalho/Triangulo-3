# -*- coding: utf-8 -*-
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0,5,157)
LIGHT_GREEN = (111,255,109)
GREEN = (0, 255, 0)
DARK_GREEN = (0,102,2)
LIGHT_RED = (255, 111, 97)
RED = (255, 0, 0)
DARK_RED = (137, 2, 0)
LIGHT_CYAN = (0, 255, 255)
CYAN = (0, 133, 244)
DARK_CYAN = (0,65,132)
GREENISH_YELLOW = (181,255,14)
YELLOW = (255, 255, 0)
DARK_YELLOW = (168, 165, 0)
ORANGE = (255, 116, 3)
DARK_ORANGE = (143, 64, 0 )
PURPLE = (117, 0, 244)
DARK_PURPLE = (64, 0, 113)
PINK = (240, 0, 236)
DARK_PINK = (168, 0, 166)
BROWN = (150, 75, 0)
LIGHT_GRAY = (210, 210, 210)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

pygame.init()


janela = pygame.display.set_mode((700,630))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    janela.fill((WHITE))

    # desenhando na superfície
    pygame.draw.polygon(janela, BLUE, [[10, 150], [85, 150], [45, 70]])
    pygame.draw.polygon(janela, DARK_YELLOW, [[100, 150], [175, 150], [135, 70]])
    pygame.draw.polygon(janela, DARK_RED, [[200, 150], [275, 150], [235, 70]])
    pygame.draw.polygon(janela, LIGHT_GREEN, [[300, 150], [375, 150], [335, 70]])
    pygame.draw.polygon(janela, ORANGE, [[400, 150], [475, 150], [435, 70]])
    pygame.draw.polygon(janela, PURPLE, [[500, 150], [575, 150], [535, 70]])
    pygame.draw.polygon(janela, CYAN, [[600, 150], [675, 150], [635, 70]])
    pygame.draw.polygon(janela, PINK, [[10, 300], [85, 300], [45, 220]])
    pygame.draw.polygon(janela, GRAY, [[100, 300], [175, 300], [135, 220]])
    pygame.draw.polygon(janela, GREENISH_YELLOW, [[200, 300], [275, 300], [235, 220]])
    pygame.draw.polygon(janela, DARK_ORANGE, [[300, 300], [375, 300], [335, 220]])
    pygame.draw.polygon(janela, LIGHT_CYAN, [[400, 300], [475, 300], [435, 220]])
    pygame.draw.polygon(janela, DARK_CYAN, [[500, 300], [575, 300], [535, 220]])
    pygame.draw.polygon(janela, LIGHT_GRAY, [[600, 300], [675, 300], [635, 220]])
    pygame.draw.polygon(janela, RED, [[10, 450], [85, 450], [45, 370]])
    pygame.draw.polygon(janela, GREEN, [[100, 450], [175, 450], [135, 370]])
    pygame.draw.polygon(janela, LIGHT_RED, [[200, 450], [275, 450], [235, 370]])
    pygame.draw.polygon(janela, DARK_BLUE, [[300, 450], [375, 450], [335, 370]])
    pygame.draw.polygon(janela, DARK_PURPLE, [[400, 450], [475, 450], [435, 370]])
    pygame.draw.polygon(janela, DARK_GRAY, [[500, 450], [575, 450], [535, 370]])
    pygame.draw.polygon(janela, LIGHT_GREEN, [[600, 450], [675, 450], [635, 370]])
    pygame.draw.polygon(janela, DARK_PINK, [[10, 600], [85, 600], [45, 520]])
    pygame.draw.polygon(janela, PURPLE, [[100, 600], [175, 600], [135, 520]])
    pygame.draw.polygon(janela, BROWN, [[200, 600], [275, 600], [235, 520]])
    pygame.draw.polygon(janela, DARK_GRAY, [[300, 600], [375, 600], [335, 520]])
    pygame.draw.polygon(janela, BLACK, [[400, 600], [475, 600], [435, 520]])
    pygame.draw.polygon(janela, GRAY, [[500, 600], [575, 600], [535, 520]])
    pygame.draw.polygon(janela, YELLOW, [[600, 600], [675, 600], [635, 520]])

    pygame.display.flip()




