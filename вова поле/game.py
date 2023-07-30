import pygame as pg
from vika_config import W, H, BLACK, k
from vika_physics import RoboSoccer, Ball
from vika_visual import draw_field
import math
pg.init()


class GameInfo:
    def __init__(self, ball_x, ball_y, ball_vx, ball_vy, red_x, red_y, blue_x, blue_y, red_score, blue_score, time):
        self.ball_pos = (ball_x, ball_y)
        self.ball_v = (ball_vx, ball_vy)
        self.red_pos = (red_x, red_y)
        self.blue_pos = (blue_x, blue_y)
        self.score = (red_score, blue_score)
        self.time = time


class Game:
    def __init__(self, window):
        self.win_W = W
        self.win_H = H

        self.red_soccer = RoboSoccer('red')
        self.blue_soccer = RoboSoccer('blue')
        self.ball = Ball()

        self.score = (0, 0)
        self.window = window
        self.time = 0

    def draw_score(self):
        font = pg.font.SysFont(None, 24)
        img = font.render(str(int(self.score[0])) + " " + (str(int(self.score[1]))), True, BLACK)
        self.window.blit(img, (W / 2, 20))

    def draw(self):
        draw_field(self.window)
        self.red_soccer.draw()
        self.blue_soccer.draw()
        self.ball.draw()
        self.draw_score()

    def move_soccer(self, red=True, forward=1, left=1):
        if red:
            if forward == 1:
                # self.red_soccer.move(pg.K_w)
                if self.red_soccer.y >= 6 * k:
                    self.red_soccer.x += 5 * (math.cos(self.red_soccer.angle))
                    self.red_soccer.y += 5 * (math.sin(self.red_soccer.angle + math.pi))
            elif forward == 0:
                # self.red_soccer.move(None)
                pass
            elif forward == -1:
                # self.red_soccer.move(pg.K_s)
                if self.red_soccer.y <= H - 6 * k:
                    self.red_soccer.x += -5 * (math.cos(self.red_soccer.angle))
                    self.red_soccer.y += 5 * (math.sin(self.red_soccer.angle))
            if left == 1:
                # self.red_soccer.move(pg.K_q)
                if self.red_soccer.angle >= 2 * math.pi:
                    self.red_soccer.angle = 0
                self.red_soccer.angle += 0.2
            elif left == 0:
                # self.red_soccer.move(None)
                pass
            elif left == -1:
                # self.red_soccer.move(pg.K_e)
                if self.red_soccer.angle <= 0:
                    self.red_soccer.angle += 2 * math.pi
                self.red_soccer.angle -= 0.2
        else:
            if forward == 1:
                # self.blue_soccer.move(pg.K_UP)
                if self.blue_soccer.y >= 6 * k:
                    self.blue_soccer.x += 5 * (math.cos(self.blue_soccer.angle))
                    self.blue_soccer.y += 5 * (math.sin(self.blue_soccer.angle + math.pi))
            elif forward == 0:
                # self.blue_soccer.move(None)
                pass
            elif forward == -1:
                # self.blue_soccer.move(pg.K_DOWN)
                if self.blue_soccer.y <= H - 6 * k:
                    self.blue_soccer.x += -5 * (math.cos(self.blue_soccer.angle))
                    self.blue_soccer.y += 5 * (math.sin(self.blue_soccer.angle))
            if left == 1:
                # self.blue_soccer.move(pg.K_SLASH)
                if self.blue_soccer.angle >= 2 * math.pi:
                    self.blue_soccer.angle = 0
                self.blue_soccer.angle += 0.2
            elif left == 0:
                # self.blue_soccer.move(None)
                pass
            elif left == -1:
                # self.blue_soccer.move(pg.K_RSHIFT)
                if self.blue_soccer.angle <= 0:
                    self.blue_soccer.angle += 2 * math.pi
                self.blue_soccer.angle -= 0.2

    def loop(self):
        # self.blue_soccer.move(None)  # переписать для нейросети
        self.blue_soccer.hit_ball(self.ball)
        # self.red_soccer.move(None)
        self.red_soccer.hit_ball(self.ball)
        self.ball.move()
        self.score = (self.ball.red_goals, self.ball.blue_goals)
        self.time += 1
        game_info = GameInfo(self.ball.x, self.ball.y, self.ball.vx, self.ball.vy, self.red_soccer.x, self.red_soccer.y, self.blue_soccer.x, self.blue_soccer.y, self.score[0], self.score[1], self.time)
        return game_info

    def reset(self):
        self.ball.reset()
        self.red_soccer.reset()
        self.blue_soccer.reset()
        self.score = (self.ball.red_goals, self.ball.blue_goals)

