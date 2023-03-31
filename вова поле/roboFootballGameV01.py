import pygame
import random
k = 1
W = 400*k  # ширина игрового окна
H = 300*k # высота игрового окна
FPS = 30 # частота кадров в секунду
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
GREEN_FIELD = (58,181,74)
BLUE = (0, 0, 255)

sc = pygame.display.set_mode((300, 200))

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((W, H))
screen.fill(GREEN_FIELD)
pygame.display.flip()
pygame.display.set_caption("RoboFootball - Z")
clock = pygame.time.Clock()

#Робот коорды + радиус башки
x = W//2
y = H//2
r = 5*k

running = True
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
    #границы поля
    pygame.draw.rect(sc, WHITE, (10*k, 10*k, W-(20*k), H-(20*k)), 5*k)
    #разметка поля
    pygame.draw.line(sc, WHITE, (W//2, 10*k), (W//2,H-(11*k)), 5*k)
    pygame.draw.circle(sc, WHITE, (W//2,H//2), 30*k, 5*k)
    pygame.draw.circle(sc, WHITE, (W//2,H//2), 5*k)
    pygame.draw.line(sc, WHITE, (40*k,95*k), (40*k, 205*k), 5*k)
    pygame.draw.line(sc, WHITE, (40*k,95*k), (10*k, 95*k), 5*k)
    pygame.draw.line(sc, WHITE, (40*k,205*k), (10*k,205*k), 5*k)
    pygame.draw.line(sc, WHITE, (360*k, 95*k), (360*k,205*k), 5*k)
    pygame.draw.line(sc, WHITE, (360*k,95*k), (389*k, 95*k), 5*k)
    pygame.draw.line(sc, WHITE, (360*k,205*k), (389*k,205*k), 5*k)
    #Ворота
    pygame.draw.line(sc, BLUE, (12*k, 95*k), (12*k,205*k), 4*k)
    pygame.draw.circle(sc, BLUE, (12*k, 95*k), 4*k)
    pygame.draw.circle(sc, BLUE, (12*k, 205*k), 4*k)
    pygame.draw.line(sc, YELLOW, (387*k, 95*k), (387*k,205*k), 4*k)
    pygame.draw.circle(sc, YELLOW, (387*k, 95*k), 4*k)
    pygame.draw.circle(sc, YELLOW, (387*k, 205*k), 4*k)
    #Робот1
    pygame.draw.circle(sc, BLUE, (x, y), r)
    
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
