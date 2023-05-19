import pygame
import math

k = 2
W = 400 * k  # ширина игрового окна
H = 300 * k  # высота игрового окна
FPS = 30  # частота кадров в секунду
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (125, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GREEN_FIELD = (58, 181, 74)
BLUE = (0, 0, 255)
DARK_BLUE = (21, 34, 56)
FOV = (245, 183, 2)

sc = pygame.display.set_mode((300, 200))

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

running = True
alpha = math.radians(0)
betha = math.radians(90)
gamma = math.radians(180)
zeta = math.radians(270)
x = W // 2
y = H // 2
motion = 'stop'

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                motion = 'left'
            elif event.key == pygame.K_RIGHT:
                motion = 'right'
            elif event.key == pygame.K_UP:
                motion = 'up'
            elif event.key == pygame.K_DOWN:
                motion = 'down'
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = 'stop'

    screen.fill(GREEN_FIELD)
    pygame.draw.circle(sc, BLACK, (x, y), 5 * k)
    pygame.draw.circle(sc, BLACK, (x + 40 * math.cos(alpha), y + 40 * math.sin(alpha)), 3 * k)
    pygame.draw.circle(sc, BLACK, (x + 40 * math.cos(betha), y + 40 * math.sin(betha)), 3 * k)
    pygame.draw.circle(sc, BLACK, (x + 40 * math.cos(gamma), y + 40 * math.sin(gamma)), 3 * k)
    pygame.draw.circle(sc, BLACK, (x + 40 * math.cos(zeta), y + 40 * math.sin(zeta)), 3 * k)

    if motion == 'left':
        x -= 3
    elif motion == 'right':
        x += 3
    elif motion == 'up':
        y -= 3
    elif motion == 'down':
        y += 3

        # pygame.draw.circle(sc, BLACK, (W//2+40*math.cos(betha), H//2+40*math.sin(betha)), 3*k)
    # pygame.draw.circle(sc, WHITE, (W//2-40*math.cos(alpha), H//2+40*math.sin(alpha)), 3*k)
    # После отрисовки всего, переворачиваем экран
    alpha += 0.01
    betha += 0.01
    gamma += 0.01
    zeta += 0.01
    # поворот
    pygame.draw.circle(sc, BLUE, (10 // 2 + 100 * math.cos(alpha), 10 // 2 + 100 * math.sin(alpha)), 5 * k)
    pygame.display.flip()

pygame.quit()