from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, plaer_x, plaer_y, plaer_speed, rect_with, rect_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (rect_with, rect_height))
        self.speed = plaer_speed
        self.rect = self.image.get_rect()
        self.rect.x = plaer_x
        self.rect.y = plaer_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Plaer(GameSprite):
    def update(self, move):
        keys = key.get_pressed()
        if move == True:
            if keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.x < win_width - 20:
                self.rect.x += self.speed
            if keys[K_UP] and self.rect.y >5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < win_height - 20:
                self.rect.y += self.speed  
        # elif move == False:



class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 100:
            self.direction = 'right'
        if self.rect.x >= 510:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


win_width = 700
win_height = 530
window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
background = transform.scale(image.load('halls.jpg'), (win_width, win_height))

z = 2
plaer = Plaer('hero.png', 620, 450, z, 30, 30)
enemy = Enemy('cyborg.png', (win_width/2), (win_height/2), z, 120, 60)
final = GameSprite('treasure.png', 20, 300, 0, 65, 65)

r = 102
g = 0
b = 0
#стены
walls = []

w1 = Wall(r, g, b, 100, 10, 500, 10)
w2 = Wall(r, g, b, 100, 510, 500, 10)
w3 = Wall(r, g, b, 100, 10, 10, 150)
w4 = Wall(r, g, b, 100, 260, 10, 150)
w5 = Wall(r, g, b, 100, 260, 100, 10)
w6 = Wall(r, g, b, 100, 160, 150, 10)
w7 = Wall(r, g, b, 250, 110, 10, 50)
w8 = Wall(r, g, b, 250, 110, 100, 10)
w9 = Wall(r, g, b, 300, 10, 10, 100)
w10 = Wall(r, g, b, 150, 60, 150, 10)

w11 = Wall(r, g, b, 150, 60, 10, 50)
w12 = Wall(r, g, b, 600, 10, 10, 400)
w13 = Wall(r, g, b, 350, 60, 10, 50)
w14 = Wall(r, g, b, 350, 60, 200, 10)
w15 = Wall(r, g, b, 500, 60, 10, 250)
w16 = Wall(r, g, b, 450, 160, 100, 10)
w17 = Wall(r, g, b, 550, 110, 10, 50)
w18 = Wall(r, g, b, 550, 110, 50, 10)
w19 = Wall(r, g, b, 450, 310, 100, 10)
w20 = Wall(r, g, b, 450, 110, 10, 150)

w21 = Wall(r, g, b, 400, 110, 50, 10)
w22 = Wall(r, g, b, 350, 260, 100, 10)
w23 = Wall(r, g, b, 400, 260, 10, 100)
w24 = Wall(r, g, b, 400, 360, 100, 10)
w25 = Wall(r, g, b, 500, 360, 10, 50)
w26 = Wall(r, g, b, 550, 410, 50, 10)
w27 = Wall(r, g, b, 100, 460, 100, 10)
w28 = Wall(r, g, b, 200, 410, 10, 50)
w29 = Wall(r, g, b, 100, 410, 100, 10)
w30 = Wall(r, g, b, 200, 260, 10, 50)

w31 = Wall(r, g, b, 150, 360, 10, 50)
w32 = Wall(r, g, b, 150, 360, 100, 10)
w33 = Wall(r, g, b, 250, 360, 10, 100)
w34 = Wall(r, g, b, 250, 410, 50, 10)
w35 = Wall(r, g, b, 350, 210, 50, 10)
w36 = Wall(r, g, b, 350, 160, 10, 50)
w37 = Wall(r, g, b, 300, 160, 50, 10)
w38 = Wall(r, g, b, 300, 160, 10, 100)
w39 = Wall(r, g, b, 250, 260, 50, 10)
w40 = Wall(r, g, b, 250, 260, 10, 50)

w41 = Wall(r, g, b, 250, 310, 100, 10)
w42 = Wall(r, g, b, 350, 310, 10, 150)
w43 = Wall(r, g, b, 350, 410, 100, 10)
w44 = Wall(r, g, b, 350, 460, 100, 10)
w45 = Wall(r, g, b, 500, 460, 10, 50)
w46 = Wall(r, g, b, 150, 210, 10, 50)
w47 = Wall(r, g, b, 150, 210, 100, 10)
w48 = Wall(r, g, b, 300, 460, 10, 50)
w49 = Wall(r, g, b, 150, 110, 50, 10)
# # w50 = Wall(r, g, b, )

walls.append(w1)
walls.append(w2)
walls.append(w3)
walls.append(w4)
walls.append(w6)
walls.append(w7)
walls.append(w8)
walls.append(w9)
walls.append(w10)
walls.append(w11)
walls.append(w12)
walls.append(w13)
walls.append(w14)
walls.append(w15)
walls.append(w16)
walls.append(w17)
walls.append(w18)
walls.append(w19)
walls.append(w20)
walls.append(w21)
walls.append(w22)
walls.append(w23)
walls.append(w24)
walls.append(w25)
walls.append(w26)
walls.append(w27)
walls.append(w28)
walls.append(w29)
walls.append(w30)
walls.append(w31)
walls.append(w32)
walls.append(w33)
walls.append(w34)
walls.append(w35)
walls.append(w36)
walls.append(w37)
walls.append(w38)
walls.append(w39)
walls.append(w40)
walls.append(w41)
walls.append(w42)
walls.append(w43)
walls.append(w44)
walls.append(w45)
walls.append(w46)
walls.append(w47)
walls.append(w48)
walls.append(w49)
# walls.append(w50)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!!!', True, (255, 215, 0))
lose = font.render('YOU LOSE', True, (180, 0, 0))

move = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        

        window.blit(background, (0 ,0))
        plaer.reset()
        enemy.reset()
        final.reset()

        plaer.update(move)
        enemy.update()

        #стены
        for w in walls:
            w.draw_wall()

        if sprite.collide_rect(plaer, final):
            z = 0
            window.blit(win, (200, 200))
            finish = True
            move = False
            money.play()

        for w in walls:
            if  sprite.collide_rect(plaer, w):
                z = 0
                window.blit(lose, (200, 200))
                finisf = True
                move = False
                kick.play()

        if sprite.collide_rect(plaer, enemy):
            z = 0
            window.blit(lose, (200, 200))
            finisf = True
            move = False
            kick.play()

        # if sprite.collide_rect(plaer, enemy) or sprite.collide_rect(plaer, w1) or sprite.collide_rect(plaer, w2) or sprite.collide_rect(plaer, w3) or sprite.collide_rect(plaer, w4) or sprite.collide_rect(plaer, w5) or sprite.collide_rect(plaer, w6) or sprite.collide_rect(plaer, w7) or sprite.collide_rect(plaer, w8) or sprite.collide_rect(plaer, w9) or sprite.collide_rect(plaer, w10) or sprite.collide_rect(plaer, w11) or sprite.collide_rect(plaer, w12) or sprite.collide_rect(plaer, w13) or sprite.collide_rect(plaer, w14) or sprite.collide_rect(plaer, w15) or sprite.collide_rect(plaer, w16) or sprite.collide_rect(plaer, w17) or sprite.collide_rect(plaer, w18) or sprite.collide_rect(plaer, w19) or sprite.collide_rect(plaer, w20) or sprite.collide_rect(plaer, w21) or sprite.collide_rect(plaer, w22) or sprite.collide_rect(plaer, w23) or sprite.collide_rect(plaer, w24) or sprite.collide_rect(plaer, w25) or sprite.collide_rect(plaer, w26) or sprite.collide_rect(plaer, w27) or sprite.collide_rect(plaer, w28) or sprite.collide_rect(plaer, w29) or sprite.collide_rect(plaer, w30) or sprite.collide_rect(plaer, w31) or sprite.collide_rect(plaer, w32) or sprite.collide_rect(plaer, w33) or sprite.collide_rect(plaer, w34) or sprite.collide_rect(plaer, w35) or sprite.collide_rect(plaer, w36) or sprite.collide_rect(plaer, w37) or sprite.collide_rect(plaer, w38) or sprite.collide_rect(plaer, w39) or sprite.collide_rect(plaer, w40) or sprite.collide_rect(plaer, w41) or sprite.collide_rect(plaer, w42) or sprite.collide_rect(plaer, w43) or sprite.collide_rect(plaer, w44) or sprite.collide_rect(plaer, w45) or sprite.collide_rect(plaer, w46) or sprite.collide_rect(plaer, w47) or sprite.collide_rect(plaer, w48) or sprite.collide_rect(plaer, w49):
        #     z = 0
        #     window.blit(lose, (200, 200))
        #     finisf = True
        #     kick.play()

    clock.tick(FPS)
    display.update()


