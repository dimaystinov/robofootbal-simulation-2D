import pygame as pg
import math
from vika_config import FOV, k, W, H, head_r, BLUE, DARK_BLUE, RED, DARK_RED, BLACK

sc = pg.display.set_mode((W, H))


class RoboSoccer:
    def __init__(self, team):
        self.head_radius = head_r
        self.team = team
        if team == 'blue':
            self.head_color = BLUE
            self.body_color = DARK_BLUE
            self.x = W // 2 + 35 * k
            self.y = H // 2
            self.angle = math.pi
        else:
            self.head_color = RED
            self.body_color = DARK_RED
            self.x = W // 2 - 35 * k
            self.y = H // 2
            self.angle = 0

    def draw(self):
        fov = 20
        fov_thickness = 2
        if self.angle == 0:
            pg.draw.rect(sc, self.body_color, (self.x - 6 * k, self.y - 9 * k, 12 * k, 18 * k))
            pg.draw.lines(sc, FOV, True, [[self.x, self.y], [self.x + fov * k, self.y + fov * k],
                                          [self.x + fov * k, self.y - fov * k]], fov_thickness * k)
        elif self.angle == math.pi:
            pg.draw.rect(sc, self.body_color, (self.x - 6 * k, self.y - 9 * k, 12 * k, 18 * k))
            pg.draw.lines(sc, FOV, True, [[self.x, self.y], [self.x - fov * k, self.y + fov * k],
                                          [self.x - fov * k, self.y - fov * k]], fov_thickness * k)
        elif self.angle == math.pi / 2:
            pg.draw.rect(sc, self.body_color, (self.x - 9 * k, self.y - 6 * k, 18 * k, 12 * k))
            pg.draw.lines(sc, FOV, True, [[self.x, self.y], [self.x - fov * k, self.y - fov * k],
                                          [self.x + fov * k, self.y - fov * k]], fov_thickness * k)
        elif self.angle == math.pi * 1.5:
            pg.draw.rect(sc, self.body_color, (self.x - 9 * k, self.y - 6 * k, 18 * k, 12 * k))
            pg.draw.lines(sc, FOV, True, [[self.x, self.y], [self.x - fov * k, self.y + fov * k],
                                          [self.x + fov * k, self.y + fov * k]], fov_thickness * k)
        pg.draw.circle(sc, self.head_color, (self.x, self.y), self.head_radius)

        pg.draw.line(sc, RED, (self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5)),
                               self.y + k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))),
                     (self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5)),
                      self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))))
        pg.draw.line(sc, RED, (self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5)),
                               self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))),
                     (self.x - k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5)),
                      self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))))

    def if_keys(self):
        keys = pg.key.get_pressed()
        if keys:
            self.move(keys)

    def move(self, keys):
        if keys[pg.K_w]:
            if self.y >= 6 * k:
                self.y -= 2
                self.angle = math.pi / 2
        if keys[pg.K_a]:
            if self.x >= 9 * k:
                self.x -= 2
                self.angle = math.pi
        if keys[pg.K_s]:
            if self.y <= H - 6 * k:
                self.y += 2
                self.angle = math.pi * 1.5
        if keys[pg.K_d]:
            if self.x <= W - 9 * k:
                self.x += 2
                self.angle = 0
        # FIXME по диагонали движется в 2 раза быстрее

    def hit_ball(self, ball):
        # FIXME сделать нормальные хитбоксы, если поставить больше ball.v будет неопределенное поведение
        if (self.angle == 0) or (self.angle == math.pi):
            x1 = self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5))
            y1 = self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))
            y2 = self.y + k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))
            if (x1 < ball.x + ball.r < x1 + 12*k) and ((y1 <= ball.y <= y2) or (y2 <= ball.y <= y1)):
                #ball.x = x1 - ball.r-1
                ball.vx = -2
            elif (x1 - 12*k < ball.x - ball.r < x1) and ((y1 <= ball.y <= y2) or (y2 <= ball.y <= y1)):
                #ball.x = x1 + ball.r+1
                ball.vx = 2
        else:
            x1 = self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5))
            x2 = self.x - k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5))
            y1 = self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))
            if (y1 < ball.y + ball.r < y1 + 12*k) and ((x1 <= ball.x <= x2) or (x2 <= ball.x <= x1)):
                ball.vy = -2
            elif (y1 - 12*k < ball.y - ball.r < y1) and ((x1 <= ball.x <= x2) or (x2 <= ball.x <= x1)):
                ball.vy = 2


class Ball:
    def __init__(self):
        self.x = W / 2
        self.y = H / 2
        self.vx = 0
        self.vy = 0
        self.r = 10
        self.a = 0.99
        self.angle = 0

    def draw(self):
        pg.draw.circle(sc, BLACK, (self.x, self.y), self.r)

    def move(self):
        if (self.r <= self.x <= W-self.r) and (self.r <= self.y <= H-self.r):
            self.x += self.vx
            self.y += self.vy
        elif not (self.r <= self.x <= W-self.r):
            if self.r > self.x:
                self.x = self.r
            else:
                self.x = W - self.r
            self.vx *= -1
        elif not (self.r <= self.y <= H-self.r):
            if self.r > self.y:
                self.y = self.r
            else:
                self.y = H - self.r
            self.vy *= -1
        self.vx *= self.a
        self.vy *= self.a
        if abs(self.vx) < 0.1:
            self.vx = 0
        if abs(self.vy) < 0.1:
            self.vy = 0
