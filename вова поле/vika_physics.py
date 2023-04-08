import pygame
from vika_config import FOV, k, W, H, head_r, BLUE, DARK_BLUE, RED, DARK_RED

sc = pygame.display.set_mode((W, H))


class RoboSoccer:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.head_radius = head_r
        self.team = team
        if team == 'blue':
            self.head_color = BLUE
            self.body_color = DARK_BLUE
        else:
            self.head_color = RED
            self.body_color = DARK_RED

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

    """"def move(self, keys):
        if keys[pg.K_w]:
            y -= 1
        if keys[pg.K_a]:
            x -= 1
        if keys[pg.K_s]:
            y += 1
        if keys[pg.K_d]:
            x += 1
    """


