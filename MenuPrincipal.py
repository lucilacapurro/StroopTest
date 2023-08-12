import pygame
import sys

from MenuPre import menuPre
from MenuPost import menuPost

########################################################################################################################

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Stroop')
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("arialblack.ttf", 50)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:
        screen.fill((255, 255, 255))
        draw_text('Test de Stroop', font, (0, 0, 0), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_width = 280
        button_height = 80
        button_x = (screen_width - button_width) // 2
        button_pre_y = (screen_height - button_height) // 2 - 80
        button_post_y = (screen_height - button_height) // 2 + 80
        button_pre = pygame.Rect(button_x, button_pre_y, button_width, button_height)
        button_post = pygame.Rect(button_x, button_post_y, button_width, button_height)
        pygame.draw.rect(screen, (0, 0, 0), button_pre)
        pygame.draw.rect(screen, (0, 0, 0), button_post)
        draw_text('Pre', font, (255, 255, 255), screen, button_x+105, button_pre_y+25)
        draw_text('Post', font, (255, 255, 255), screen, button_x+95, button_post_y+25)

        click = False
        for event in pygame.event.get(): # event handling to respond to user input
            if event.type == pygame.QUIT: # QUIT
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # ESC to quit
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # click
                if event.button == 1:
                    click = True

        # PRE option
        if button_pre.collidepoint((mx, my)):
            if click: # PRE button pressed 
                app = menuPre()
                app.run() # runs PRE screen
        
        # POST option
        if button_post.collidepoint((mx, my)):
            if click: # POST button pressed 
                app = menuPost()
                app.run() # runs POST screen

        pygame.display.update()
        mainClock.tick(60)

########################################################################################################################

main_menu()
