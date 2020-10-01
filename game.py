import pygame
pygame.init()

win_width = 500
win_height = 480

win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("First Game")

walk_right = [pygame.image.load(f"R{frame}.png") for frame in range(1, 10)]
walk_left = [pygame.image.load(f"L{frame}.png") for frame in range(1, 10)]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
velocity = 5

is_jump = False
jump_count = 10
left = False
right = False
walk_count = 0


def redraw_game_window():
    global walk_count
    win.blit(bg, (0, 0))

    if walk_count + 1 >= 27:
        walk_count = 0
    if left:
        win.blit(walk_left[walk_count//3], (x, y))
        walk_count += 1
    elif right:
        win.blit(walk_right[walk_count//3], (x, y))
        walk_count += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        left = True
        right = False
        if x > velocity:
            x -= velocity
        else:
            x = 0
    elif keys[pygame.K_RIGHT]:
        right = True
        left = False
        if x < win_width - width - velocity:
            x += velocity
        else:
            x = win_width - width
    else:
        right = False
        left = False
        walk_count = 0
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= jump_count ** 2 * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    redraw_game_window()

pygame.quit()