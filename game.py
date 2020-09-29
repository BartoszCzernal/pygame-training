import pygame
pygame.init()

win_width = 500
win_height = 500

win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
velocity = 5
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > velocity:
            x -= velocity
        else:
            x = 0
    if keys[pygame.K_RIGHT]:
        if x < win_width - width - velocity:
            x += velocity
        else:
            x = win_width - width
    if keys[pygame.K_UP]:
        if y > velocity:
            y -= velocity
        else:
            y = 0
    if keys[pygame.K_DOWN]:
        if y < win_height - height - velocity:
            y += velocity
        else:
            y = win_height - height

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()