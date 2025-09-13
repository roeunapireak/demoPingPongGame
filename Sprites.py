
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_width, p_height, p_speed):
        super().__init__()

        self.image = transform.scale(image.load(p_image), (p_width, p_height))
        self.speed = p_speed

        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y


    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


