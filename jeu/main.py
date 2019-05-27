import pygame

pygame.init()

SCREENWIDTH = 500 # variables de tailles de l'écan
SCREENHEIGHT = 480

win = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("GN'G")

walkRight = [pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R1.png'), # liste des sprites de marche s'il va a droite
             pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R2.png'),
             pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R3.png'),
             pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R4.png'),
             pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R5.png'),
             pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R6.png'),
             pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R7.png'),
             pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R8.png'),
             pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/R9.png')]
walkLeft = [pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L1.png'),  # liste des sprites de marche s'il va a gauche
            pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L2.png'),
            pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L3.png'),
            pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L4.png'),
            pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L5.png'),
            pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L6.png'),
            pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L7.png'),
            pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L8.png'),
            pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/L9.png')]
bg = pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/bg.jpg')
char = pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/standing.png')
projec = pygame.image.load('C:/Users/efergefe/Desktop/prog/py/jeu/projectile.png')
clock = pygame.time.Clock()

class player():
    def __init__(self, x ,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height= height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 10
        self.standing = True

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self .right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0],(self.x, self.y))


class projectile():
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        win.blit(projec, (self.x, self.y))

def reDrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# boucle MAIN
man = player(300,410,64,64)
bullets = []
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0 :
            bullet.x += (bullet.vel*2)
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel :
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < SCREENWIDTH - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    reDrawGameWindow()

pygame.quit()
