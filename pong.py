from pygame import *
import random
window = display.set_mode((700,500))
win_width = 700
win_height = 500
display.set_caption('pong')
background = transform.scale(image.load('back.png'), (700,500))
clock = time.Clock()
run = True
font.init()
font = font.SysFont('Arial',70)
score1 = 0
score2 = 0
SCORE1 = font.render(str(score1), True, (50,255,50))
SCORE2 = font.render(str(score2), True, (50,255,50))
FPS = 60
direction =[-1,1]

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size1, player_size2,  player_vert, player_horiz):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(1*player_size1,1*player_size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.horiz = player_horiz
        self.vert = player_vert    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        #self.rect.y = ball.rect.y
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        #self.rect.y = ball.rect.y
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        global score1
        global score2
        
        if self.rect.y < 0:
            self.vert = 1
        if self.rect.y > 450:
            self.vert = -1
        self.rect.x += self.horiz * self.speed
        self.rect.y += self.vert * self.speed
        if self.rect.x < 0:
            self.rect.x = 325
            self.rect.y = 225
            self.vert = random.choice(direction)
            self.horiz = random.choice(direction)
            score2 += 1
        if self.rect.x > 650:
            self.rect.x = 325
            self.rect.y = 225  
            self.vert = random.choice(direction)
            self.horiz = random.choice(direction)          
            score1 += 1
    def right(self):
        self.horiz = 1
    def left(self):
        self.horiz = -1
        
        

player1 = Player1('stiahnuť.png', 680, 210, 5, 20, 80, 0, 0)
player2 = Player2('stiahnuť.png', 0, 210, 5, 20, 80, 0, 0)
ball = Ball( 'ball.png', 325, 225, 5, 50, 50, -1, 1)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if run == True:
        window.blit(background,(0,0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.update()
        ball.reset()


        if sprite.collide_rect(ball, player1):
            ball.left()
        if sprite.collide_rect(ball, player2):
            ball.right()

        SCORE1 = font.render(str(score1), True, (50,255,50))
        SCORE2 = font.render(str(score2), True, (50,255,50))
        window.blit(SCORE1, (10,10))
        window.blit(SCORE2, (660,10))





        clock.tick(FPS)
        display.update()