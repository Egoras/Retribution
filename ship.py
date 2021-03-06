import pygame 



class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings =  ai_settings
        self.image = pygame.image.load('img/ship1.png')
        self.shipLeft = pygame.image.load('img/shipLeft.png')
        self.shipRight = pygame.image.load('img/shipRight.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана. 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx) # Сохранение вещественной координаты центра корабля. 
    def update(self): 
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = self.shipRight
            self.center += self.ai_settings.ship_speed_factor 
        if self.moving_left and self.rect.left > 0:
            self.image = self.shipLeft
            self.center -= self.ai_settings.ship_speed_factor 
        self.rect.centerx = self.center # Обновление атрибута rect на основании self.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect) # определяется метод blitme(), который выводит изображение на экран в позиции, заданной self.rect.
        
        
    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.center = self.screen_rect.centerx