import pygame as pg
from vika_visual import draw_field, init
from vika_config import FPS, teamb, teamr
from vika_physics import RoboSoccer, Ball

screen, clock = init()
running = True

blue_soccer = RoboSoccer(teamb)
red_soccer = RoboSoccer(teamr)
soccers = [blue_soccer, red_soccer]
ball = Ball()

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            event_keydown = event
    blue_soccer.if_keys()
    blue_soccer.hit_ball(ball)
    red_soccer.if_keys()
    red_soccer.hit_ball(ball)
    ball.move()

    draw_field(screen)
    ball.draw()
    ball.draw_score()
    for soccer in soccers:
        soccer.draw()
    pg.display.flip()
pg.quit()
