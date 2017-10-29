import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблем."""
    def __init__(self, ai_settings, screen, ship):
        """Создает объект пули в текущей позиции корабля.""" 
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Создание пули в позиции (0,0) и назначение правильной позиции 
        self.image = pygame.image.load('img/bullet1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Позиция пули хранится в вещественном формате.
        self.y = float(self.rect.y)
        
        #self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """Перемещает пулю вверх по экрану."""
        self.y -= self.speed_factor # Обновление позиции пули в вещественном формате.
        self.rect.y = self.y # Обновление позиции прямоугольника.
    
    def draw_bullet(self):
        """Вывод пули на экран."""
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
        