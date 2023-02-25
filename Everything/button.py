import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action




''''print('hi')
import pygame
import random
import math

enemyIgm =[]
enemyX=[]
enemyY=[]
EnemyX_change = []
EnemyY_change = []
num_of_enemies=6
randomY_around_the_earth=[0]*num_of_enemies

for i in range(num_of_enemies):
    enemyIgm.append(pygame.image.load('CO2(64pixel).png'))#'final-boss-Enemy.png'
    enemyX.append(random.randint(448, 528)) #(0,735)
    enemyY.append(random.randint(90, 170)) #(0, 735)
    EnemyX_change.append(random.randrange(-1, 2, 2))#(1)
    EnemyY_change.append(random.randrange(-1, 2, 2))#40


def enemy(x, y, i,screen):
    screen.blit(enemyIgm[i], (x, y))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX-50) - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False



def enemy_maker(MaxX,MaxY,bulletX, bulletY,screen,playerY,score_value):
    for i in range(num_of_enemies):
        # enemy movement
        enemyX[i] += EnemyX_change[i]
        enemyY[i] += EnemyY_change[i]
        # checking each one of the enemies movements
        if enemyX[i] <= 0 or enemyX[i] >= MaxX:
            EnemyX_change[i] = EnemyX_change[i] * -1
        if enemyY[i] <= 0 or enemyY[i] >= MaxY:
            EnemyY_change[i] = EnemyY_change[i] * -1

        # if u hit the side start going back

        # collision(was not in the for loop at first-had to put it here so it checks for each one of the nemies)
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY  # 480
            bullet_state = 'ready'
            score_value += 1

            # pygame.draw.rect(background,(0,0,0),((488,175),(10,10)))
            # pygame.draw.rect(background, (0, 0, 0), ((488, 90+170), (10, 10))) => #radius about (170-90)/2=40

            # random place on earth - to appear again
            randomY_around_the_earth[i] = random.randint(-40, +40)
            enemyY[i] = randomY_around_the_earth[i] + 130
            enemyX[i] = math.sqrt((40 ** 2) - randomY_around_the_earth[i] ** 2)
            enemyX[i] = enemyX[i] * (random.randrange(-1, 2,
                                                      2)) + 488  # for a given Y there are two x's...here randomly the x value is multiplied by either one or negative one

            # random velocit (x and y) after deiing
            EnemyX_change[i] = (random.randrange(-1, 2, 2))  # (1)
            EnemyY_change[i] = (random.randrange(-1, 2, 2))

            # enemyX[i]=random.randint(0,736)
            # enemyY[i]=random.randint(50,150)
        # this was not in the loof at firts-now it is bcz it creates each enemy w its case
        enemy(enemyX[i], enemyY[i], i,screen)'''''