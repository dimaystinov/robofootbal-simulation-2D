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
        #pg.draw.rect(sc, self.body_color, ((self.x -  math.cos(self.angle ), (self.y) - math.sin(self.angle ), (self.x) + math.cos(self.angle), (self.y) + math.sin(self.angle))))
        pg.draw.lines(sc, FOV, True, [[self.x, self.y],
                                      [self.x + 2 * fov * math.cos(self.angle + 1),
                                       self.y + 2 * fov * math.sin(self.angle + 1 - math.pi)],
                                      [self.x + 2 * fov * math.cos((self.angle - 1)),
                                       self.y + 2 * fov * math.sin(self.angle - 1 - math.pi)]], fov_thickness * k)
        pg.draw.circle(sc, self.head_color, (self.x + math.cos(self.angle + 1), self.y + math.sin(self.angle)),
                       self.head_radius)
        if(self.head_color == BLUE):
            font = pg.font.SysFont(None, 24)
            img = font.render(str(int(self.angle/math.pi*180)), True, BLUE)
            sc.blit(img, (20, 20))
            img = font.render(str(int(self.x) )+ ' ' +str(int(self.y)) , True, BLUE)
            sc.blit(img, (20, 40))

        '''
        pg.draw.line(sc, RED, (self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5)),
                               self.y + k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))),
                     (self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5)),
                      self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))))
        pg.draw.line(sc, RED, (self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5)),
                               self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))),
                     (self.x - k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5)),
                      self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))))'''

    def if_keys(self):
        keys = pg.key.get_pressed()
        if keys:
            self.move(keys)

    def move(self, keys):
        if self.team == 'blue':
            if keys[pg.K_UP]:
                if self.y >= 6 * k:
                    self.x += 5*(math.cos(self.angle))
                    self.y += 5*(math.sin(self.angle + math.pi))
            if keys[pg.K_LEFT]:
                if self.x >= 9 * k:
                    self.x += 5 * (math.cos(self.angle + math.pi / 2))
                    self.y += 5 * (math.sin(self.angle - math.pi / 2))
            if keys[pg.K_DOWN]:
                if self.y <= H - 6 * k:
                    self.x += -5 * (math.cos(self.angle))
                    self.y += 5 * (math.sin(self.angle))
            if keys[pg.K_RIGHT]:
                if self.x <= W - 9 * k:
                    self.x += 5 * (math.cos(self.angle - math.pi / 2))
                    self.y += 5 * (math.sin(self.angle + math.pi / 2))

            if keys[pg.K_SLASH]:
                if self.angle >= 2*math.pi:
                    self.angle = 0
                self.angle += 0.2
            if keys[pg.K_RSHIFT]:
                if self.angle <= 0:
                    self.angle += 2 * math.pi
                self.angle -= 0.2
        else:
            if keys[pg.K_w]:
                if self.y >= 6 * k:
                    self.x += 5 * (math.cos(self.angle))
                    self.y += 5 * (math.sin(self.angle + math.pi))
            if keys[pg.K_a]:
                if self.x >= 9 * k:
                    self.x += 5 * (math.cos(self.angle + math.pi / 2))
                    self.y += 5 * (math.sin(self.angle - math.pi / 2))
            if keys[pg.K_s]:
                if self.y <= H - 6 * k:
                    self.x += -5 * (math.cos(self.angle))
                    self.y += 5 * (math.sin(self.angle))
            if keys[pg.K_d]:
                if self.x <= W - 9 * k:
                    self.x += 5 * (math.cos(self.angle - math.pi / 2))
                    self.y += 5 * (math.sin(self.angle + math.pi / 2))

            if keys[pg.K_q]:
                if self.angle >= 2 * math.pi:
                    self.angle = 0
                self.angle += 0.2
            if keys[pg.K_e]:
                if self.angle <= 0:
                    self.angle += 2 * math.pi
                self.angle -= 0.2


        # FIXME по диагонали движется в 2 раза быстрее

    def hit_ball(self, ball, bx, by ,br, rx,ry,rr):
        # FIXME сделать нормальные хитбоксы, если поставить больше ball.v будет неопределенное поведение
        if (ball.x - bx) ** 2 + (ball.y - by) ** 2 >= (br + ball.r) ** 2:
            self.hit_flag = True
        if (ball.x - bx) ** 2 + (ball.y - by) ** 2 <= (br + ball.r) ** 2 and self.hit_flag:
            try:
                angle = math.atan((ball.y - self.y) / (ball.x - self.x))
                print(round(angle * 180 / 3.14), 2)
                coef = 1
                if (self.x - ball.x) > 0:
                    coef = -1

                ball.vx = 10 * math.cos(angle) * coef
                ball.vy = 10 * math.sin(angle) * coef
                print('bx', ball.x, 'by', ball.y, 'px', self.x, 'py', self.y, 'coef', coef, 'vx', ball.vx, 'vy',
                      ball.vy)
                self.hit_flag = False

            except:
                pass

        '''if (self.angle == 0) or (self.angle == math.pi):
            x1 = self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5))
            y1 = self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))
            y2 = self.y + k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))
            if (x1 < ball.x + ball.r < x1 + 12 * k) and ((y1 <= ball.y <= y2) or (y2 <= ball.y <= y1)):
                # ball.x = x1 - ball.r-1
                ball.vx = 10
            elif (x1 - 12 * k < ball.x - ball.r < x1) and ((y1 <= ball.y <= y2) or (y2 <= ball.y <= y1)):
                # ball.x = x1 + ball.r+1
                ball.vx = -10
        else:
            x1 = self.x + k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5))
            x2 = self.x - k * 117 ** 0.5 * math.cos(self.angle + math.atan(1.5))
            y1 = self.y - k * 117 ** 0.5 * math.sin(self.angle + math.atan(1.5))
            if (y1 < ball.y + ball.r < y1 + 12 * k) and ((x1 <= ball.x <= x2) or (x2 <= ball.x <= x1)):
                ball.vy = 10
            elif (y1 - 12 * k < ball.y - ball.r < y1) and ((x1 <= ball.x <= x2) or (x2 <= ball.x <= x1)):
                ball.vy = -10'''



class Ball:
    def __init__(self):
        self.x = W / 2
        self.y = H / 2
        self.vx = 0
        self.vy = 0
        self.r = 10
        self.a = 0.99
        self.angle = 0
        self.blue_goals = 0
        self.red_goals = 0

    def draw(self):
        if (self.x <= 25) and (190 <= self.y <= 410):
            self.blue_goals += 1
            self.x = W / 2
            self.y = H / 2
            self.vx = 0
            self.vy = 0

        if (self.x >= 775) and (190 <= self.y <= 410):
            self.red_goals += 1
            self.x = W / 2
            self.y = H / 2
            self.vx = 0
            self.vy = 0

        pg.draw.circle(sc, BLACK, (self.x, self.y), self.r)
        font = pg.font.SysFont(None, 24)
        img = font.render(str(int(self.red_goals)) + " " +(str(int(self.blue_goals))), True, BLUE)
        sc.blit(img, (W / 2, 20))

    def move(self):
        if (self.r <= self.x <= W - self.r) and (self.r <= self.y <= H - self.r):
            self.x += self.vx
            self.y += self.vy
        elif not (self.r <= self.x <= W - self.r):
            if self.r > self.x:
                self.x = self.r
            else:
                self.x = W - self.r
            self.vx *= -1
        elif not (self.r <= self.y <= H - self.r):
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
