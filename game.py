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


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 10

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.left:
            win.blit(walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.right:
            win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(char, (self.x, self.y))


def redraw_game_window():
    win.blit(bg, (0, 0))
    man.draw(win)
    pygame.display.update()


man = Player(300, 410, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        man.left = True
        man.right = False
        if man.x > man.velocity:
            man.x -= man.velocity
        else:
            man.x = 0
    elif keys[pygame.K_RIGHT]:
        man.right = True
        man.left = False
        if man.x < win_width - man.width - man.velocity:
            man.x += man.velocity
        else:
            man.x = win_width - man.width
    else:
        man.right = False
        man.left = False
        man.walk_count = 0
    if not man.is_jump:
        if keys[pygame.K_SPACE]:
            man.is_jump = True
            man.right = False
            man.left = False
    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= man.jump_count ** 2 * 0.5 * neg
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 10
    redraw_game_window()

pygame.quit()