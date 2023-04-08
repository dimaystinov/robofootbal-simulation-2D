import pygame
from vika_visual import draw_field, draw_soccers, init
from vika_config import FPS

screen, clock = init()
running = True

while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    draw_field(screen)
    draw_soccers(screen)
    pygame.display.flip()
pygame.quit()
