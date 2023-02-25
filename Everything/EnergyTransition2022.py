import math
import numpy
import pygame
import random
import button

#import fpstimer as tm
#import ShowScreen as SC

pygame.init()

MaxX= 1000
MaxY= 750

##hint = SC.disp_txt("text",100,(100,400))

##timeWinScreen=1
##timer=0


screen = pygame.display.set_mode((MaxX, MaxY))

#load all the images (these are the croped images of healthy earth)
row1_column1= pygame.image.load('1st_earth.jpg')
row1_column2= pygame.image.load('2nd_earth.jpg')
row1_column3= pygame.image.load('3rd_earth.jpg')
row2_column1= pygame.image.load('4th_earth.jpg')
row2_column2= pygame.image.load('5th_earth.jpg')
row2_column3= pygame.image.load('6th_earth.jpg')
row3_column1= pygame.image.load('7th_earth.jpg')
row3_column2= pygame.image.load('8th_earth.jpg')
row3_column3= pygame.image.load('9th_2_last_orbit.jpg')
row3_column3_Final= pygame.image.load('9th_2_last_orbit_FINAL.jpg')


win0=pygame.image.load('Welcome_back.JPG')
win=pygame.transform.scale(win0,(MaxX,MaxY))


#this is the start page
main=pygame.image.load('edited_background_V3.png')
#This is the background when you start thegame
background_0 = pygame.image.load('MAIN_bck_last_orbit_FINAL.png') #'Competition(2).jpg'

Healthy_background=pygame.image.load('HEALTHY-1.jpg')

background=pygame.transform.scale(background_0,(MaxX,MaxY))

# Title and Icon
pygame.display.set_caption("ENERGY TRANSITION 2080")

#icon
icon = pygame.image.load('spaceship (2).png')
pygame.display.set_icon(icon)
#####################  PLAYER
# player
playerIgm1 = pygame.image.load('spaceship (2).png') #cat.png
playerIgm = pygame.transform.scale(playerIgm1, (32, 32))

Orbit = pygame.image.load('Orbit.png')


playerX = 500#520#370
playerY = 700 #100#480
playerX_change = 0
playerY_change =0
##################### END PLAYER


######################################## Storing values in lists

###################### ENEMY (CO2)
#creating Empty lists so i can store the image of every single CO2 w their unique X&Y speed (totalmspeed is constant)
#I learned this (how to have multiple enemies at the same time) from a youtube vid
enemyIgm =[]
enemyX=[]
enemyY=[]
EnemyX_change = []
EnemyY_change = []
TotalSpeed=1
num_of_enemies=6
randomY_around_the_earth=[0]*num_of_enemies

image_enemy_01=pygame.image.load('main_CO2(64pixel).png')
image_enemy=pygame.transform.scale(image_enemy_01,(32,32))
for i in range(num_of_enemies):
    enemyIgm.append(image_enemy)
    enemyX.append(random.randint(448, 528))
    enemyY.append(random.randint(140, 265))
    #this part picks a random location on earth for each single one of these to appear
    angle=numpy.deg2rad(random.randint(0,90))
    EnemyX_change.append(math.cos(angle)*TotalSpeed*random.randrange(-1, 2, 2))
     #i used 'random.randrange(-1, 2, 2)' here o get either positive 1 or negative 1
    EnemyY_change.append(math.sin(angle)*TotalSpeed*random.randrange(-1, 2, 2))
###################### END of CO2 (enemy) part


###################### GREEN
#Exactly the same thing as i did for enemy (CO2) but this timefor green energy pics
greenIgm =[]
greenX=[]
greenY=[]
greenX_change = []
greenY_change = []
num_of_greens=6
randomY_around_the_earth=[0]*num_of_enemies

for i in range(num_of_greens):
    image_green=pygame.image.load('GreenPower_'+str(i)+'.png')
    greenIgm.append(image_green)#'final-boss-Enemy.png'
    greenX.append(random.randint(448, 528)) #(0,735)
    greenY.append(random.randint(140, 265)) #(0, 735)
    greenX_change.append(random.randrange(-1, 2, 2))#(1)
    greenY_change.append(random.randrange(-1, 2, 2))#40
###################### END of green part
######################################## The part of Storing values in lists is done!




###################### bullet
bulletIgm_01 = pygame.image.load('fire.png')
bulletIgm=pygame.transform.scale(bulletIgm_01,(16,16))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
#in the break out gme (assigment 4) we used 1 and zeros but here i wil use 'ready'and'fire'
bullet_state = 'ready'
###################### bullet-DONE!


######################Warning messages
WarningIgm=[]
for i in range(6):
    #i edited all the images and did some reaserch and wrote short messages about each green energysource..
    #so when you accidently shoot wind energy it shows a message about wind energy and maybe a fun fact
    warningImage=pygame.image.load('Warning_'+ str(i) +'.png')
    #I have 6 unit warnings...which will be shown when u accidently shoot the green resources instead of CO2.
    # using 'pygame.image.load('Warning_'+ str(i) +'.png')'"is how i stored the images in the list (as can be seen before)

    WarningIgm.append(warningImage)
Warning_x=0
Warning_Y=700

WarningX_change = 0
WarningY_change = TotalSpeed*1.5
#WarningY_change is dependent on Totalspeed (of green and CO2 icons) bcz game runs w difff speeds on diff computers...in this when you change the time stp..speed of the warning changes prportionally
Warning_State='ready'
Warning_State_1=0
######################



######################score
score_value=0
#green_score_value=0 #remove later -(suopposed to reset the game)
font=pygame.font.Font('freesansbold.ttf',15)
#donwload font from dafont.com (free) and pu it in the folder (learned form youtube)
textX=10
textY=10
######################



def show_score(x,y):
    good_job=''
    good_job1=''
    y1=y+20
    new_score_value=score_value
    if score_value>=9:
        y1+=0
        new_score_value=9
        good_job='WELL DONE! ' #i coldn't find a way to write new lines so for creating new lines i hadto write each line sperately w its own coordinates
        description1='Earth is fully habitable as of now.  '
        description2='Bring down the % CO2 produced'
        description3='by fosil fuel to 0 in order to be able'
        description4='to use the wormhole to get home.'
        score0_1=font.render(description1,True,(255,255,255))
        score0_2=font.render(description2,True,(255,255,255))
        score0_3=font.render(description3,True,(255,255,255))
        score0_4=font.render(description4,True,(255,255,255))
        screen.blit(score0_1,(x,y+50))
        screen.blit(score0_2,(x,y+70))
        screen.blit(score0_3,(x,y+90))
        screen.blit(score0_4,(x,y+110))
        pygame.draw.polygon(screen,(255,255,255), ((5,50), (265,50), (265,140), (5,140)) ,3)
    score=font.render('Earth is  '+str(round(new_score_value*11.1,1))+'  %'+ '  habitable.  '+good_job,True, (255,255,255))
 # donwload font from dafont.com (free) and pu it in the folder
    screen.blit(score,(x,y))
    
    if score_value>15:
        good_job1='WELL DONE! Use the worm hole to cross the debris orbit. Welcome home!'
    score1=font.render('Fossil Fuel based CO2:  '+str(round(100-new_score_value*6.6))+'  %',True, (255,255,255))
    screen.blit(score1,(x,y1))
##################################################################
def player(x, y):
    # needs two variable/enteries (1-what, 2-coordinates(,))
    screen.blit(playerIgm, (x, y))

def enemy(x, y, i,enemyIgm):
    screen.blit(enemyIgm[i], (x, y))

def fire_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletIgm, (x , y ))

def show_warning( y,i):
    global Warning_State
    Warning_State = 'fire'
    screen.blit(WarningIgm[i],(10 , y ))

def iscollision(enemyX, enemyY, bulletX, bulletY,radius):#ignore radius..
    distance=bulletX-enemyX
    Ydistance=bulletY-enemyY
    if -16<distance<32 and -16<Ydistance<32:# bcz images (CO2 and greeen resources) are all 32 pxels
        return True
    else:
        return False


###################################
#load button images (credits to youtube lol..had no idea how to do his..learned this part ompletely form youtbe)
start_img = pygame.image.load('start_buttom.png').convert_alpha()
start_button = button.Button(120, 660, start_img, 1)

###################################

timestep=1#1

meow=False
meow1=False
running = True
while running:
    # RGB => Red, Green, & Blue (base of all colors) (no more than 255)
    # you can use google to go from color to RGB values
    screen.fill((0, 50, 0))
    screen.blit(main,(0,0))
    # Background image

    #########


    if start_button.draw(screen):
        print('START')
        meow=True
############MAIN GAME LOOP -AFTER YOU PRESS START ####################################
    while meow:


        screen.blit(background, (0, 0))


#well basically i came up the idea of earth beoing healthier as you kill CO2..
        #So i found two pictures (healthy earth and not healthy earth) and cropeed the healthy part
        # to diff parts...so after everytime u kill a CO2...the cropped part appears on
        # top of of the back gournd(unhealthy earth)..it makes it look lik earth s getting better
        if score_value>=1:
            screen.blit(row1_column1, (0, 0))
            if score_value>=2:
                screen.blit(row1_column2, (465, 0))
                if score_value>=3:
                    screen.blit(row1_column3, (520, 0))
                    if score_value>=4:
                        screen.blit(row2_column1, (0, 155))
                        if score_value>=5:
                            screen.blit(row2_column2, (465, 155))
                            if score_value >= 6:
                                screen.blit(row2_column3, (520, 155))
                                if score_value >= 7:
                                    screen.blit(row3_column1, (0, 210))
                                    if score_value >= 8:
                                        screen.blit(row3_column2, (465, 210))
                                        if score_value >= 9:
                                            screen.blit(row3_column3, (520, 210))
                                            #After the earth is fully saved...CO2 will stop respawning..meaning we can fianlly get rid of all the CO2 in the game
                                            if score_value>=10:
                                                num_of_enemies=5
                                                if score_value>=11:
                                                    num_of_enemies=4
                                                    if score_value>=12:
                                                        num_of_enemies=3
                                                        if score_value>=13:
                                                            num_of_enemies=2
                                                            if score_value>=14:
                                                                num_of_enemies=1
                                                                if score_value>=15:
                                                                    num_of_enemies=0
                                                                    screen.blit(row3_column3_Final, (520, 210))
                                                                    if 580>playerX>406 and 90<playerY<265:
                                                                        screen.blit(win,(0,0))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meow = False
                pygame.quit()



            if event.type==pygame.MOUSEBUTTONDOWN:
                Xmouse, Ymouse=pygame.mouse.get_pos() # i enede up not using this after watching youtube which showed a easier way(using classes(seee file 'button')
            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -7
                    #print('Left arrow is pressed')
                if event.key == pygame.K_RIGHT:
                    playerX_change = +7
                if event.key==pygame.K_UP:
                    playerY_change= -7
                if event.key == pygame.K_DOWN:
                    playerY_change = +7

                    #print('Right arrow is pressed')
                if event.key == pygame.K_SPACE:
                    if bullet_state == 'ready':
                        # get the current x coordinate of the spaceship
                        bulletX = playerX+8
                        bulletY=playerY
                        fire_fire(bulletX, bulletY)

                        #####################

            # KEYDOWN pressing that key/any bottom on the key bord
            # KEYUP releasing that press
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    playerY_change=0
                   # print('Keystroke has been released')

        meow = True

        playerX += playerX_change
        playerY+= playerY_change


####################basically the boundaries (just like assigment 40
        if playerX <= 0:
            playerX = 0

        elif playerX >= MaxX - 32:
          playerX = MaxX - 32


    #TELEPORT (after getting rid of all Co2 a wormhole will apear which will teleport u to
        #the other side of the debris orbit..so u can get home(earth)
        if playerY>480 and playerY<500 :
                playerY = 480
        if playerY<552 and playerY>500:
            playerY=552

        if playerY >= MaxY - 33:  # 540
            playerY = MaxY - 33



    ############33                               CO2
    ########################################3 ENEMY
        # checkiong for boundaries of the enemy so it doesn't go out of the bound
        for i in range(num_of_enemies):
            # enemy movement
            enemyX[i] += EnemyX_change[i]
            enemyY[i] +=EnemyY_change[i]
            #checking each one of the enemies movements
            if enemyX[i] <= 0 or enemyX[i] >= MaxX-32:
                EnemyX_change[i] = EnemyX_change[i]*-1
            if enemyY[i] <=0 or enemyY[i]>= 480:
                EnemyY_change[i]=EnemyY_change[i]*-1
###############checking elemnt number i for colliosion

            collision_enemy = iscollision(enemyX[i], enemyY[i], bulletX, bulletY,32)
            collision_spacecraft = iscollision(enemyX[i], enemyY[i], playerX, playerY,32)
            if collision_enemy:
                bulletY = playerY
                bullet_state = 'ready'
                score_value += 1


                #random place on earth - to appear/respawn again
                randomY_around_the_earth[i]=random.randint(-60,+60)
                enemyY[i]=randomY_around_the_earth[i] +130
                enemyX[i]=math.sqrt((60**2)-randomY_around_the_earth[i]**2)
                enemyX[i]=enemyX[i]*(random.randrange(-1, 2, 2))+488 #for a given Y there are two x's...here randomly the x value is multiplied by either one or negative one

                #random velocit (x and y) after deiing (to respawn w)
                angle1 = numpy.deg2rad(random.randint(0, 90))
                EnemyX_change[i]=(math.cos(angle)*TotalSpeed*random.randrange(-1, 2, 2))  # (1)
                EnemyY_change[i]=(math.sin(angle)*TotalSpeed*random.randrange(-1, 2, 2))

            enemy(enemyX[i], enemyY[i],i,enemyIgm)

    ####################################################################################### GREEN
        for i in range(num_of_greens):
            greenX[i] += greenX_change[i]
            greenY[i] +=greenY_change[i]
            #checking each one of the enemies movements
            if greenX[i] <= 0 or greenX[i] >= MaxX:
                greenX_change[i] = greenX_change[i]*-1
            if greenY[i] <=0 or greenY[i]>= 480:
                greenY_change[i]=greenY_change[i]*-1

        # if u hit the side start going back
#######################################################not sure
            # collision(was not in the for loop at first-had to put it here so it checks for each one of the nemies)
            collision_green = iscollision(greenX[i], greenY[i], bulletX, bulletY,40)





            if collision_green:

                bulletY = playerY#480
                bullet_state = 'ready'

                show_warning(Warning_Y,i)
                Number=i

    
                #random place on earth - to /respawn again
                randomY_around_the_earth[i]=random.randint(-60,+60)
                greenY[i]=randomY_around_the_earth[i] +130
                greenX[i]=math.sqrt((60**2)-randomY_around_the_earth[i]**2)
                greenX[i]=greenX[i]*(random.randrange(-1, 2, 2))+488 #for a given Y there are two x's...here randomly the x value is multiplied by either one or negative one
    
                #random velocit (x and y) after deiing to respawn again
                greenX_change[i]=(random.randrange(-1, 2, 2))  # (1)
                greenY_change[i]=(random.randrange(-1, 2, 2))

            enemy(greenX[i], greenY[i], i,greenIgm)


        # get the current x coordinate of the spaceship

    ######################################################################################

        # bullet movement
        # so basically before pressing space bar the state was ready sp this code did not even work
        # but after that the function gets called when pression space bar..its state changes ..which will result in this
        if bulletY <=0:
            bulletY = playerY#480
            bullet_state = 'ready'

        if bullet_state == 'fire':
            fire_fire(bulletX, bulletY)
            bulletY -= bulletY_change

        if Warning_Y<=-750:
            Warning_Y=MaxY
            Warning_State='ready'

        if Warning_State=='fire':
            show_warning(Warning_Y,Number)
            Warning_Y -= WarningY_change


        player(playerX, playerY)

        show_score(textX,textY)

        if score_value>=15:
             if playerX>800 and playerX<864and playerY>600 and playerY<664:
                playerX=83
                playerY=380
        pygame.time.wait(timestep)

        pygame.display.update()
 ###############################################################################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #pygame.quit()
    pygame.display.update()
