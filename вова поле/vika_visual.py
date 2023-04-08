import pygame as pg
from vika_config import WHITE, k, W, H, BLUE, YELLOW, RED, GREEN_FIELD, DARK_RED, DARK_BLUE, teamb, teamr
from vika_physics import RoboSoccer


def init():
    pg.init()
    pg.mixer.init()  # для звука
    screen = pg.display.set_mode((W, H))
    screen.fill(GREEN_FIELD)
    pg.display.flip()
    pg.display.set_caption("RoboFootball - Z")
    clock = pg.time.Clock()
    return screen, clock

def draw_field(sc):
    pg.draw.rect(sc, WHITE, (10 * k, 10 * k, W - (20 * k), H - (20 * k)), 5 * k)
    # разметка поля
    pg.draw.line(sc, WHITE, (W // 2, 10 * k), (W // 2, H - (11 * k)), 5 * k)
    pg.draw.circle(sc, WHITE, (W // 2, H // 2), 30 * k, 5 * k)
    pg.draw.circle(sc, WHITE, (W // 2, H // 2), 5 * k)
    pg.draw.line(sc, WHITE, (40 * k, 95 * k), (40 * k, 205 * k), 5 * k)
    pg.draw.line(sc, WHITE, (40 * k, 95 * k), (10 * k, 95 * k), 5 * k)
    pg.draw.line(sc, WHITE, (40 * k, 205 * k), (10 * k, 205 * k), 5 * k)
    pg.draw.line(sc, WHITE, (360 * k, 95 * k), (360 * k, 205 * k), 5 * k)
    pg.draw.line(sc, WHITE, (360 * k, 95 * k), (389 * k, 95 * k), 5 * k)
    pg.draw.line(sc, WHITE, (360 * k, 205 * k), (389 * k, 205 * k), 5 * k)
    # Ворота
    pg.draw.line(sc, BLUE, (12 * k, 95 * k), (12 * k, 205 * k), 4 * k)
    pg.draw.circle(sc, BLUE, (12 * k, 95 * k), 4 * k)
    pg.draw.circle(sc, BLUE, (12 * k, 205 * k), 4 * k)
    pg.draw.line(sc, YELLOW, (387 * k, 95 * k), (387 * k, 205 * k), 4 * k)
    pg.draw.circle(sc, YELLOW, (387 * k, 95 * k), 4 * k)
    pg.draw.circle(sc, YELLOW, (387 * k, 205 * k), 4 * k)

def draw_soccers(sc):
    blue_soccer_x = W // 2 + 35 * k
    blue_soccer_y = H // 2

    red_soccer_x = W // 2 - 35 * k
    red_soccer_y = H // 2

    Blue_soccer = RoboSoccer(blue_soccer_x, blue_soccer_y, teamb)
    Blue_soccer.spawn()

    Red_soccer = RoboSoccer(red_soccer_x, red_soccer_y, teamr)
    Red_soccer.spawn()
