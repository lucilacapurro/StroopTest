import pygame
import os
from datetime import datetime
import sys
import pygame_textinput

from StroopTest1 import stroopTest1

########################################################################################################################

class TextModule:
    def __init__(self,screen, screen_width, screen_height):
        self.font = pygame.font.SysFont(None, 90)
        self.smaller_font = pygame.font.SysFont(None, 60)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.text_surface = None

    def render_text(self, text, center=None, big_font=True):
        if big_font:
            self.text_surface = self.font.render(text, True, (0, 0, 0))
        else:
            self.text_surface = self.smaller_font.render(text, True, (0, 0, 0))
        if center:
            self.text_rect = self.text_surface.get_rect(center=center)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.text_surface, self.text_rect)

    def draw_no_bkg(self):
        self.screen.blit(self.text_surface, self.text_rect)

    def show_message(self, message, big_font=True, no_bkg=False):
        self.render_text(message, center=(self.screen_width//2, self.screen_height//2-200), big_font=big_font)
        if no_bkg:
            self.draw_no_bkg()
        else:
            self.draw()
        pygame.display.flip()


class menuPost:
    def __init__(self):
        pygame.init()
        screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.text_module = TextModule(self.screen,self.screen.get_width(), self.screen.get_height())
        self.running = True
        self.selected_code = None # code selected option

        self.participant_code = None
        self.participant_age = None

        self.gamestate = 'login'
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.rect = pygame.Rect(self.screen.get_width()/2-290, self.screen.get_height()/2-150, 580, 50)

    # participant code
    def login_screen(self):
        self.screen.fill((255, 255, 255))
        if self.selected_code: # writes selected_code
            pygame.draw.rect(self.screen, pygame.Color(0,0,0), self.rect, 4)
            font = pygame.font.Font(None, 40)
            code_text = font.render(self.selected_code, True, pygame.Color(0, 0, 0))
            code_rect = code_text.get_rect(left=self.rect.left + 10, centery=self.rect.centery)
            self.screen.blit(code_text, code_rect)
        else: # selected_code == None
            pygame.draw.rect(self.screen, pygame.Color(0,0,0), self.rect, 4)
        code_options = ["Code 1", "Code 2", "Code 3", "Code 4", "Code 5", "Code 6", "Code 7"] # possible code options for the dropdown menu
        dropdown_rect = pygame.Rect(self.screen.get_width()/2-290, self.screen.get_height()/2-100, 580, 30)
        font = pygame.font.Font(None, 24)
        for idx, option in enumerate(code_options):
            option_rect = dropdown_rect.copy()
            option_rect.y += idx * 30
            pygame.draw.rect(self.screen, pygame.Color(220,220,220), option_rect)
            text_surface = font.render(option, True, pygame.Color(0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (option_rect.x + 10, option_rect.y + 5)
            self.screen.blit(text_surface, text_rect)
            if option_rect.collidepoint(pygame.mouse.get_pos()): # Dropdown interaction: detects clicks and updates the selected option
                if pygame.mouse.get_pressed()[0]:  # mouse click on code option
                    self.selected_code = option # updates the selected option
        self.text_module.show_message("Seleccione el código del sujeto", big_font=False, no_bkg=True)

    # participant age 
    def age_screen(self):
        self.screen.fill((255, 255, 255))
        self.textinput.update(self.events)
        self.screen.blit(self.textinput.surface, (self.screen.get_width()/2-270, self.screen.get_height()/2-140))
        pygame.draw.rect(self.screen, pygame.Color(0,0,0), self.rect, 4)
        self.text_module.show_message("Ingrese la edad del sujeto", big_font=False, no_bkg=True)

    def run(self):
        while self.running:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT: # Quit
                    self.running = False
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE: # Esc to quit
                        self.running = False
                        sys.exit()
                    if event.key == pygame.K_RETURN: # ENTER
                        if self.gamestate == 'login' and self.selected_code != None: # ENTER to input the selected code
                            self.participant_code = self.selected_code
                            self.textinput.value = ""  # Clear the selected code
                            self.selected_code = None
                            self.gamestate = 'age' # after the code input, the age is requested
                        if self.gamestate == 'age' and len(self.textinput.value) > 0: # ENTER to input the participant's age
                            self.participant_age = self.textinput.value
                            self.gamestate = 'test1' # after the age input, starts the test

            if self.gamestate == 'login': # participant code request
                self.login_screen()
            
            elif self.gamestate == 'age': # participant age request
                self.age_screen()

            elif self.gamestate == 'test1': # begin test1
                app = stroopTest1(self.screen, self.screen.get_width(), self.screen.get_height())
                app.run()
                
            pygame.display.flip()

########################################################################################################################

if __name__ == '__main__':
    app = menuPost()
    app.run()
