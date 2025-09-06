import pygame

class MainScreen:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.length = 1000
        self.width = 800
        self.screen = pygame.display.set_mode((self.length, self.width))

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            pygame.display.flip()
