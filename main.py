
from pygame import *
from Sprites import GameSprite, Player

background = (200, 255, 255)

window = display.set_mode((600, 500)) # widht, height


clock = time.Clock()


ball = GameSprite(p_image='img/tennis-ball.png', 
                  p_x=50, p_y=50, 
                  p_width=60, p_height=60, 
                  p_speed=1)

rocket1 = Player(p_image='img/racket.png', 
                  p_x=5, p_y=240, 
                  p_width=30, p_height=150, 
                  p_speed=2)

rocket2 = Player(p_image='img/racket.png', 
                  p_x=560, p_y=240, 
                  p_width=30, p_height=150, 
                  p_speed=2)

speed_x = 2
speed_y = 2

font.init()
font1 = font.Font(None, 35)
player1_lose = font1.render('PLAYER 1 LOSES!', True, (180, 0, 0))
player2_lose = font1.render('PLAYER 2 LOSES!', True, (180, 0, 0))

run = True
finsh = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if finsh:
        window.fill(background)
        ball.reset(window)

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y >= 440 or ball.rect.y <= 0 :
            speed_y *= -1

        if sprite.collide_rect(rocket2,ball) or sprite.collide_rect(rocket1,ball): 
            speed_x *= -1

        if ball.rect.x <= 0: 
            window.blit(player1_lose, (200, 200))
            finsh = False

        if ball.rect.x >= 600: 
            window.blit(player2_lose, (200, 200))
            finsh = False


        rocket1.reset(window)
        rocket1.update_rocket1()

        rocket2.reset(window)
        rocket2.update_rocket2()


    display.update()
    clock.tick(60)

