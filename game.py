import pygame, os, sys, time, random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("8-bit shooter")
entX = 400
entY = 300
enemyX = random.randrange(10, 790)
enemyY = random.randrange(10, 590)

s = 0

current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, 'resources')
sound_path = os.path.join(resource_path, 'sounds')
image_path = os.path.join(resource_path, 'images')

wallsX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
wallsY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

icon = pygame.image.load(os.path.join(image_path, 'icon.png'))
pygame.display.set_icon(icon)

running = True

lastKey = "u"

sound = pygame.mixer.Sound(os.path.join(sound_path, 'Hit 1.wav'))
music = pygame.mixer.music.load(os.path.join(sound_path, 'bgm.wav'))

pygame.mixer.music.play(-1)

for i in range(0, 10):
    wallsX[i] = random.randrange(0, 750)
    wallsY[i] = random.randrange(0, 550)
    
    while 410 > wallsX[i] - 10 and 410 < wallsX[i] + 60 and 310 > wallsY[i] and 310 < wallsY[i]+60 and enemyX+10 > wallsX[i] - 10 and enemyX+10 < wallsX[i] + 60 and enemyY+10 > wallsY[i] and enemyY+10 < wallsY[i]+60:
        wallsX[i] = random.randrange(0, 750)
        wallsY[i] = random.randrange(0, 550)

while running:
    
    pygame.time.delay(7)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    
    screen.fill((129,117,146))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        lastKey = "l"
        entX -= 1
        
        if entX < 10:
            entX = 10
        
        for i in range(0, 10):
            if entX < wallsX[i] + 60 and entX > wallsX[i] - 10 and entY > wallsY[i] - 10 and entY < wallsY[i]+60:
                entX += 1
    
    elif keys[pygame.K_RIGHT]:
        lastKey = "r"
        entX += 1
        
        if entX > 790:
            entX = 790
        
        for i in range(0, 10):
            if entX > wallsX[i] - 10 and entX < wallsX[i]+60 and entY > wallsY[i] - 10 and entY < wallsY[i]+60:
                entX -= 1
    
    if keys[pygame.K_UP]:
        lastKey = "u"
        entY -= 1
        
        if entY < 10:
            entY = 10
        
        for i in range(0, 10):
            if entX > wallsX[i]-10 and entX < wallsX[i] + 60 and entY < wallsY[i]+60 and entY > wallsY[i] - 10:
                entY += 1
    
    elif keys[pygame.K_DOWN]:
        lastKey = "d"
        entY += 1
        
        if entY > 590:  
            entY = 590
        
        for i in range(0, 10):
            if entX > wallsX[i]-10 and entX < wallsX[i] + 60 and entY < wallsY[i]+60 and entY > wallsY[i] - 10:
                entY -= 1
    
    elif keys[pygame.K_r]:
        enemyX = random.randrange(10, 790)
        enemyY = random.randrange(10, 590)
    
    elif keys[pygame.K_F1]:
        entX = random.randrange(10, 790)
        entY = random.randrange(10, 590)
    
    if s == 0:
        bulletX = entX
        bulletY = entY
    
    if pygame.mouse.get_pressed()[0]:
        if bulletX == entX and bulletY == entY and s == 0:
            sound.play()
            lk = lastKey
            s = 1
    
    if s == 1:
        if lk == "l":
            bulletX -= 2
       
        elif lk == "r":
            bulletX += 2
        
        elif lk == "u":
            bulletY -= 2
        
        elif lk == "d":
            bulletY += 2
        
        if bulletX <= -3 or bulletX >= 803 or bulletY <= -3 or bulletY >= 603:
            s = 0
        
        if bulletX > enemyX - 10 and bulletX < enemyX + 10 and bulletY > enemyY - 10 and bulletY < enemyY + 10:
            s = 0
            enemyX = random.randrange(10, 790)
            enemyY = random.randrange(10, 590)
        
        for i in range(0, 10):
            if bulletX > wallsX[i]-3 and bulletX < wallsX[i] + 53 and bulletY < wallsY[i]+53 and bulletY > wallsY[i] - 3:
                s = 0
    
    for i in range(0, 10):
        pygame.draw.rect(screen, (50, 50, 50), (wallsX[i], wallsY[i], 50, 50))
    
    pygame.draw.circle(screen, (134, 0, 0), (bulletX, bulletY), 3)
    pygame.draw.circle(screen, (125, 0, 125), (entX, entY), 10)
    pygame.draw.circle(screen, (0, 0, 125), (enemyX, enemyY), 10)
    
    pygame.display.update()
