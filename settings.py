import pygame
class Settings(): 
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_image = pygame.image.load('img/starBackground.bmp')
        self.ship_speed_factor = 1.5
        # парамерты пули
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.alien_speed_factor = 1.5
        self.ship_limit = 3 
        self.fleet_drop_speed = 15
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1