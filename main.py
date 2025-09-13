
from pygame import *
from Sprites import GameSprite

background = (200, 255, 255)

window = display.set_mode((600, 500)) # widht, height
window.fill(background)

clock = time.Clock()


ball = GameSprite(p_image='img/tennis-ball.png', 
                  p_x=50, p_y=50, 
                  p_width=60, p_height=60, 
                  p_speed=3)


run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    ball.reset(window)

    display.update()
    clock.tick(60)

