import pygame, os, sys, time, random

pygame.init()

screen = pygame.display.set_mode((800, 600))

entX = 400
entY = 300
s = 0

current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, 'resources')
image_path = os.path.join(resource_path, 'images')

wallsX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
wallsY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

icon = pygame.image.load(os.path.join(image_path, 'icon.png'))
pygame.display.set_icon(icon)

running = True

lastKey = "u"

for i in range(0, 10):
    wallsX[i] = random.randrange(0, 750)
    wallsY[i] = random.randrange(0, 550)
    while 410 > wallsX[i] - 10 and 410 < wallsX[i] + 60 and 310 > wallsY[i] and 310 < wallsY[i]+60:
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
    if s == 0:
        bulletX = entX
        bulletY = entY
    if pygame.mouse.get_pressed()[0]:
        if bulletX == entX and bulletY == entY and s == 0:
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
    for i in range(0, 10):
        pygame.draw.rect(screen, (50, 50, 50), (wallsX[i], wallsY[i], 50, 50))
    pygame.draw.circle(screen, (134, 0, 0), (bulletX, bulletY), 3)
    pygame.draw.circle(screen, (125, 0, 125), (entX, entY), 10)
    pygame.display.update()
