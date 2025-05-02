import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'ball1':
            ball1 = pygame.image.load("Catcher/images/ball1.png").convert_alpha()
            self.random_img = [ball1]
        elif type == 'ball2':
            ball2 = pygame.image.load("Catcher/images/ball2.png").convert_alpha()
            self.random_img = [ball2]
        else:
            ball3 = pygame.image.load("Catcher/images/ball3.png").convert_alpha()
            self.random_img = [ball3]
        self.animation_index = 0
        self.image = self.random_img[self.animation_index]
        self.rect = self.image.get_rect(midtop=(randint(20, 880), 0))

    

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.random_img): self.animation_index = 0
        self.image = self.random_img[int(self.animation_index)]
        

    def update(self):
        self.animation_state()
        self.rect.y += 5
        self.destroy()


    def destroy(self):
        if self.rect.y >= 670:
            self.rect.y = 670
    
       