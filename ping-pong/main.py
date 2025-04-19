from pygame import *
from time import sleep

window = display.set_mode((900, 600))
background = transform.scale(image.load('table.png'), (900, 600))

window.blit(background, (0,0))

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, pos_x, pos_y, speed, width, height):
        super().__init__()
        self.img = transform.scale(image.load(img), (width, height))
        self.rect = self.img.get_rect()
        self.speed = speed
        self.rect.x = pos_x
        self.rect.y = pos_y

    def reset(self):
        window.blit(self.img, self.rect)

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

p1 = Player('player.png', 0, 225, 5, 20, 150)
p2 = Player('player.png', 880, 225, 5, 20, 150)
ball = GameSprite('ball.png', 435, 285, 10, 30, 30)

speed_x = 5
speed_y = 5

points_1 = 0
points_2 = 0

font.init()
nfont = font.Font(None, 60)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    p1.update_l()
    p2.update_r()
    p1.reset()
    p2.reset()
    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
        speed_x *= -1

    if ball.rect.y <= 0 or ball.rect.y >= 570:
        speed_y *= -1

    if ball.rect.x <= 0:
        points_2 += 1
        ball.rect.x, ball.rect.y = 435, 285

    if ball.rect.x >= 870:
        points_1 += 1
        ball.rect.x, ball.rect.y = 435, 285

    if points_1 >= 5:
        p1_winner = font.Font(None, 90).render('Player 1 win!', True, (125, 100, 0))
        window.blit(p1_winner, (380, 295))
        sleep(2)
        break

    if points_2 >= 5:
        p2_winner = font.Font(None, 90).render('Player 2 win!', True, (125, 100, 0))
        window.blit(p2_winner, (380, 295))
        sleep(2)
        break

    p1_points = nfont.render(str(points_1), True, (255,255,255))
    p2_points = nfont.render(str(points_2), True, (255,255,255))
    window.blit(p1_points, (50, 20))
    window.blit(p2_points, (850, 20))

    display.update()
    clock.tick(60)