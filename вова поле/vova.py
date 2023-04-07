import pygame
import random
import math


class Robo_soccer:
    def __init__(self, x, y, head_color, body_color, head_radius, team):
        self.x = x
        self.y = y
        self.head_color = head_color
        self.body_color = body_color
        self.head_radius = head_radius
        self.team = team

    def spawn(self):
        pygame.draw.rect(sc, self.body_color, (self.x - 6 * k, self.y - 9 * k, 12 * k, 18 * k))
        pygame.draw.circle(sc, self.head_color, (self.x, self.y), self.head_radius)
        fov = 20
        fov_thickness = 2
        if self.team == 'red':
            pygame.draw.lines(sc, FOV, True, [[self.x, self.y], [self.x + fov * k, self.y + fov * k],
                                              [self.x + fov * k, self.y - fov * k]], fov_thickness * k)
        if self.team == 'blue':
            pygame.draw.lines(sc, FOV, True, [[self.x, self.y], [self.x - fov * k, self.y + fov * k],
                                              [self.x - fov * k, self.y - fov * k]], fov_thickness * k)


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
screen.fill(GREEN_FIELD)
pygame.display.flip()
pygame.display.set_caption("RoboFootball - Z")
clock = pygame.time.Clock()

# Робот коорды + радиус башки
blue_soccer_x = W // 2 + 35 * k
blue_soccer_y = H // 2

red_soccer_x = W // 2 - 35 * k
red_soccer_y = H // 2

head_r = 5 * k

teamb = 'blue'
teamr = 'red'

running = True
alpha = 0
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_w:
            y += 10

    # Обновление

    # Рендеринг
    screen.fill(GREEN_FIELD)

    # границы поля
    pygame.draw.rect(sc, WHITE, (10 * k, 10 * k, W - (20 * k), H - (20 * k)), 5 * k)
    # разметка поля
    pygame.draw.line(sc, WHITE, (W // 2, 10 * k), (W // 2, H - (11 * k)), 5 * k)
    pygame.draw.circle(sc, WHITE, (W // 2, H // 2), 30 * k, 5 * k)
    pygame.draw.circle(sc, WHITE, (W // 2, H // 2), 5 * k)
    pygame.draw.line(sc, WHITE, (40 * k, 95 * k), (40 * k, 205 * k), 5 * k)
    pygame.draw.line(sc, WHITE, (40 * k, 95 * k), (10 * k, 95 * k), 5 * k)
    pygame.draw.line(sc, WHITE, (40 * k, 205 * k), (10 * k, 205 * k), 5 * k)
    pygame.draw.line(sc, WHITE, (360 * k, 95 * k), (360 * k, 205 * k), 5 * k)
    pygame.draw.line(sc, WHITE, (360 * k, 95 * k), (389 * k, 95 * k), 5 * k)
    pygame.draw.line(sc, WHITE, (360 * k, 205 * k), (389 * k, 205 * k), 5 * k)
    # Ворота
    pygame.draw.line(sc, BLUE, (12 * k, 95 * k), (12 * k, 205 * k), 4 * k)
    pygame.draw.circle(sc, BLUE, (12 * k, 95 * k), 4 * k)
    pygame.draw.circle(sc, BLUE, (12 * k, 205 * k), 4 * k)
    pygame.draw.line(sc, YELLOW, (387 * k, 95 * k), (387 * k, 205 * k), 4 * k)
    pygame.draw.circle(sc, YELLOW, (387 * k, 95 * k), 4 * k)
    pygame.draw.circle(sc, YELLOW, (387 * k, 205 * k), 4 * k)
    # Роботы саккеры
    Blue_soccer = Robo_soccer(blue_soccer_x, blue_soccer_y, BLUE, DARK_BLUE, head_r, teamb)
    Blue_soccer.spawn()

    Red_soccer = Robo_soccer(red_soccer_x, red_soccer_y, RED, DARK_RED, head_r, teamr)
    Red_soccer.spawn()

    # После отрисовки всего, переворачиваем экран
    alpha += 0.01
    //поворот
    pygame.draw.circle(sc, BLUE, (W // 2 + 100*math.cos(alpha), H // 2  + 100*math.sin(alpha)), 5 * k)
    pygame.display.flip()

pygame.quit()