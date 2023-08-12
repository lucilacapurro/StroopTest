import pygame
from pygame.locals import *
import time
import os
import sys

########################################################################################################################

# Absolute path:
actual_dir= os.path.abspath(os.path.dirname(__file__))
alarm_file = 'alarm_beep.wav'
path_alarm_file = os.path.join(actual_dir, alarm_file) # alarm wav sound file relative path

########################################################################################################################

class stroopTest3:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clock = pygame.time.Clock()

        self.button_size_x = 130
        self.button_size_y = 30
        self.button_padding_x = 10
        self.button_padding_y = 30
        self.buttons = []

        self.initial_time = 1  # countdown begins at 45 secs
        self.elapsed_time = 0
        self.clock_running = False
        self.running = False
        self.test_ended = False
        self.show_message = False
        self.score = None
        self.PCscore = None
        self.selected_button = None
        self.selected_x2 = False
        self.selected_save = False
        pygame.mixer.init()
        self.alarm_sound = pygame.mixer.Sound(path_alarm_file)  # alarm sound

    def create_buttons(self):
        column_texts = [
            ["VERDE", "ROJO", "AZUL", "VERDE", "ROJO", "AZUL", "ROJO", "VERDE", "AZUL", "ROJO"], 
            ["VERDE", "AZUL", "ROJO", "VERDE", "ROJO", "VERDE", "AZUL", "ROJO", "VERDE", "AZUL"],  
            ["AZUL", "VERDE", "AZUL", "ROJO", "VERDE", "AZUL", "VERDE", "ROJO", "VERDE", "ROJO"], 
            ["AZUL", "ROJO", "VERDE", "AZUL", "VERDE", "AZUL", "ROJO", "VERDE", "AZUL", "ROJO"], 
            ["VERDE", "ROJO", "VERDE", "AZUL", "ROJO", "VERDE", "ROJO", "AZUL", "ROJO", "AZUL"],
            ["VERDE", "AZUL", "ROJO", "VERDE", "AZUL", "VERDE", "ROJO", "AZUL", "ROJO", "VERDE"],
            ["ROJO", "AZUL", "ROJO", "VERDE", "AZUL", "VERDE", "AZUL", "ROJO", "AZUL", "ROJO"],
            ["VERDE", "ROJO", "VERDE", "AZUL", "VERDE", "ROJO", "AZUL", "ROJO", "VERDE", "AZUL"],
            ["VERDE", "ROJO", "VERDE", "ROJO", "AZUL", "ROJO", "AZUL", "VERDE", "ROJO", "VERDE"],
            ["AZUL", "VERDE", "AZUL", "ROJO", "AZUL", "ROJO", "VERDE", "AZUL", "VERDE", "ROJO"],
        ]

        for row in range(10):
            for col in range(10):
                x = col * (self.button_size_x + self.button_padding_x) + 20
                y = row * (self.button_size_y + self.button_padding_y) + 170
                word_button = pygame.Rect(x, y, self.button_size_x, self.button_size_y)
                button = pygame.draw.rect(self.screen, (255, 255, 255), word_button)
                text = column_texts[col][row]
                score = str(col * 10 + row + 1)
                self.buttons.append((button, text, row, col, score))

    def draw_ui(self):
        self.screen.fill((255, 255, 255))

        # Task name 
        font = pygame.font.SysFont(None, 45)
        task_text = "Test de Stroop 3"
        text_surface = font.render(task_text, True, (0, 0, 0))
        self.screen.blit(text_surface, (20, 20))

        # Draw clock
        font = pygame.font.SysFont(None, 36)
        if self.initial_time > self.elapsed_time > 0: 
            time_color = (255, 255, 255) # white (invisible) during countdown
        elif self.elapsed_time >= self.initial_time: 
            time_color = (255, 0, 0) # red when count down reaches zero
        else:
            time_color = (0, 0, 0)  # black before starting the countdown at 45 secs 
        time_text = "Tiempo: {:.0f}".format(max(self.initial_time - self.elapsed_time, 0))  # counts down
        text_surface = font.render(time_text, True, time_color)  # sets defined color
        self.screen.blit(text_surface, (self.screen_width/2-100, 50))

        # Draw clock start/reset button
        button_start_reset = pygame.Rect(self.screen_width/2+50, 50, self.button_size_x, self.button_size_y)
        pygame.draw.rect(self.screen, (0, 0, 0), button_start_reset)
        font = pygame.font.SysFont(None, 24)
        button_text = "Empezar" if not self.clock_running else "Reiniciar"
        text_surface = font.render(button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_start_reset.center)
        self.screen.blit(text_surface, text_rect)

        # Draw x2 button
        button_x2 = pygame.Rect(self.screen_width/2+350, 50, 50, 30)
        if self.selected_x2: 
            pygame.draw.rect(self.screen, (255, 0, 0), button_x2)
        else: 
            pygame.draw.rect(self.screen, (0, 0, 0), button_x2)
        font = pygame.font.SysFont(None, 24)
        button_text = "x2"
        text_surface = font.render(button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_x2.center)
        self.screen.blit(text_surface, text_rect)

        # Draw save button
        button_save = pygame.Rect(self.screen_width/2+450, 50, 100, 30)
        pygame.draw.rect(self.screen, (0, 0, 0), button_save)
        font = pygame.font.SysFont(None, 24)
        button_text = "Guardar"
        text_surface = font.render(button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_save.center)
        self.screen.blit(text_surface, text_rect)

        # Draw buttons
        red = (255, 0, 0)
        green = (0, 205, 50)
        blue = (0, 0, 255)
        column_colors = [
            [red, blue, green, red, blue, green, blue, red, green, blue], 
            [red, green, blue, red, blue, red, green, blue, red, green],  
            [green, red, green, blue, red, green, red, blue, red, blue], 
            [green, blue, red, green, red, green, blue, red, green, blue],
            [red, blue, red, green, blue, red, blue, green, blue, green],
            [red, green, blue, red, green, red, blue, green, blue, red],
            [blue, green, blue, red, green, red, green, blue, green, blue],
            [red, blue, red, green, red, blue, green, blue, red, green],
            [red, blue, red, blue, green, blue, green, red, blue, red],
            [green, red, green, blue, green, blue, red, green, red, blue],
        ]

        for button, text, row, col, score in self.buttons:
            pygame.draw.rect(self.screen, (255, 255, 255), button)
            font = pygame.font.SysFont(None, 24)
            if button == self.selected_button and self.test_ended: 
                text_surface = font.render(text, True, (0, 0, 0))
            else:
                color = column_colors[col][row]
                text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(center=button.center)
            self.screen.blit(text_surface, text_rect)

        # Show End of the Test message
        if self.show_message:
            font = pygame.font.SysFont(None, 30)
            message_text = "Fin del Test 1. Presione la palabra hasta dónde llegó el participante. Si completó una vuelta además presione x2. Luego presione Guardar."
            text_surface = font.render(message_text, True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(self.screen_width // 2, 120))
            self.screen.blit(text_surface, text_rect)


        pygame.display.flip()


    # logout message end of test
    def end_screen(self):
        self.screen.fill((255, 255, 255))
        self.text_module.show_message("Ingrese la edad del sujeto", big_font=False, no_bkg=True)


    def run(self):
        self.create_buttons()
        self.running = True

        mx, my = pygame.mouse.get_pos()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # click on buttons
                    
                    button_start_reset = pygame.Rect(self.screen_width/2+50, 50, 130, 30)
                    if button_start_reset.collidepoint(event.pos): # click on start_button
                        self.clock_running = not self.clock_running # toggles the clock condition starts/reset
                        self.start_time = time.time()
                        if not self.clock_running: 
                            self.elapsed_time = 0  # resets the count down
                            self.start_time = time.time()
                    
                    for button, text, row, col, score in self.buttons:
                        if button.collidepoint(event.pos):  # click on buttons
                            self.selected_button = button 
                            self.score = score
                    
                    button_x2 = pygame.Rect(self.screen_width/2+350, 50, 50, 30)
                    if button_x2.collidepoint(event.pos): # click on x2_button
                        if self.test_ended: 
                            self.selected_x2 = not self.selected_x2
                    
                    button_save = pygame.Rect(self.screen_width/2+450, 50, 100, 30)
                    if button_save.collidepoint(event.pos): # click on save_button
                        if self.test_ended:
                            if self.selected_button != None: # allows saving if a word button is selected
                                self.selected_save = not self.selected_save
                                if self.selected_x2: # considers the x2 button
                                    self.PCscore = int(self.score) + 100 # calculates the P score
                                else:
                                    self.PCscore = int(self.score)
                                print("PC score:", self.PCscore)

                                self.show_message = False
                                self.screen.fill((255, 255, 255))  # Fill the screen with white color to clear the content
                                font = pygame.font.SysFont(None, 30)
                                message_text = "Fin del test. Los datos fueron guardados. A continuación se cerrará el programa"
                                text_surface = font.render(message_text, True, (0, 0, 0))  # Green color for success
                                text_rect = text_surface.get_rect(center=(self.screen_width // 2, 150))
                                self.screen.blit(text_surface, text_rect)
                                pygame.display.flip()
                                pygame.time.wait(4000)  # Wait for 2 seconds to show the message
                                sys.exit()

            if self.clock_running:
                self.elapsed_time = time.time() - self.start_time
                if self.elapsed_time >= self.initial_time: # countdown reaches 0
                    self.clock_running = False
                    self.show_message = True # shows end of the test message
                    self.alarm_sound.play() # plays alarm beep
                    self.test_ended = True

            self.draw_ui()
            self.clock.tick(60)
        
        pygame.display.flip()
