import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Catcher/images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (450, 700)
        
        self.player_speed = 10
    

    def player_movements(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.player_speed
        
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.player_speed
    

    def player_collision(self):
        if self.rect.x >= 780: self.rect.x = 780
        elif self.rect.x <= 0: self.rect.x = 0

    
    def update(self):
        self.player_movements()
        self.player_collision()