import pygame, os, sys, time

pygame.init()

screen = pygame.display.set_mode((800, 600))
entX = 400
entY = 300
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images')

icon = pygame.image.load(os.path.join(image_path, 'icon.png'))
pygame.display.set_icon(icon)
running = True
while running:
    pygame.time.delay(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    screen.fill((129,117,146))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        entX -= 1
        if entX < 10:
            entX = 10
    elif keys[pygame.K_RIGHT]:
        entX += 1
        if entX > 790:
            entX = 790
    if keys[pygame.K_UP]:
        entY -= 1
        if entY < 10:
            entY = 10
    elif keys[pygame.K_DOWN]:
        entY += 1
        if entY > 590:  
            entY = 590
    pygame.draw.circle(screen, (125, 0, 125), (entX, entY), 10)
    pygame.display.update()
