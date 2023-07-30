import pygame as pg
from vika_config import W, H, k
from game import Game
import neat
import os


class FootballGame:
    def __init__(self, window):
        self.game = Game(window)
        self.red_soccer = self.game.red_soccer
        self.blue_soccer = self.game.blue_soccer
        self.ball = self.game.ball

    def test_ai(self):
        run = True
        clock = pg.time.Clock()
        while run:
            clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break

            keys = pg.key.get_pressed()
            if keys[pg.K_w]:
                self.game.move_soccer(red=True, forward=1, left=0)
            if keys[pg.K_s]:
                self.game.move_soccer(red=True, forward=-1, left=0)
            if keys[pg.K_q]:
                self.game.move_soccer(red=True, forward=0, left=1)
            if keys[pg.K_e]:
                self.game.move_soccer(red=True, forward=0, left=-1)
            if keys[pg.K_UP]:
                self.game.move_soccer(red=False, forward=1, left=0)
            if keys[pg.K_DOWN]:
                self.game.move_soccer(red=False, forward=-1, left=0)
            if keys[pg.K_SLASH]:
                self.game.move_soccer(red=False, forward=0, left=1)
            if keys[pg.K_RSHIFT]:
                self.game.move_soccer(red=False, forward=0, left=-1)
            else:
                self.game.move_soccer(red=True, forward=0, left=0)
                self.game.move_soccer(red=False, forward=0, left=0)

            game_info = self.game.loop()
            print(game_info.score)
            self.game.draw()
            pg.display.update()

        pg.quit()

    def train_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
            distance1 = ((self.ball.x - self.blue_soccer.x)**2 + (self.ball.y - self.blue_soccer.y)**2)**0.5
            output1 = net1.activate((self.ball.x, self.ball.y, self.ball.vx, self.ball.vy, self.blue_soccer.x,
                                    self.blue_soccer.y, distance1))
            decision1 = output1.index(max(output1))

            if decision1 == 0:
                pass
            elif decision1 == 1:
                self.game.move_soccer(red=False, forward=1, left=0)
            elif decision1 == 2:
                self.game.move_soccer(red=False, forward=-1, left=0)
            elif decision1 == 3:
                self.game.move_soccer(red=False, forward=0, left=-1)
            elif decision1 == 4:
                self.game.move_soccer(red=False, forward=0, left=1)

            distance2 = ((self.ball.x - self.red_soccer.x) ** 2 + (self.ball.y - self.red_soccer.y) ** 2) ** 0.5
            output2 = net2.activate((self.ball.x, self.ball.y, self.ball.vx, self.ball.vy, self.red_soccer.x,
                                    self.red_soccer.y, distance2))
            decision2 = output2.index(max(output2))

            if decision2 == 0:
                pass
            elif decision2 == 1:
                self.game.move_soccer(red=True, forward=1, left=0)
            elif decision2 == 2:
                self.game.move_soccer(red=True, forward=-1, left=0)
            elif decision2 == 3:
                self.game.move_soccer(red=True, forward=0, left=-1)
            elif decision2 == 4:
                self.game.move_soccer(red=True, forward=0, left=1)
            # print(output1, output2)

            game_info = self.game.loop()

            self.game.draw()
            pg.display.update()
            if game_info.score[0] >= 1 or game_info.score[1] >= 1 or game_info.time > 2500:
                self.calculate_fitness(genome1, genome2, game_info)
                break

    def calculate_fitness(self, genome1, genome2, game_info):
        r1 = ((self.ball.x - 12*k)**2 + (self.ball.y - 95*k)**2)**0.5
        r2 = ((self.ball.x - 12*k)**2 + (self.ball.y - 205*k)**2)**0.5
        r3 = ((self.ball.x - 387*k)**2 + (self.ball.y - 95*k)**2)**0.5
        r4 = ((self.ball.x - 387*k)**2 + (self.ball.y - 205*k)**2)**0.5
        if 95*k <= self.ball.y <= 205*k:
            distance1 = self.ball.x - 12*k
            distance2 = 387*k - self.ball.x
        else:
            distance1 = min(r1, r2)
            distance2 = min(r3, r4)
        genome1.fitness += 1/(distance1+5)
        genome2.fitness += 1/(distance2+5)



def eval_genomes(genomes, config):
    window = pg.display.set_mode((W, H))

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = FootballGame(window)
            game.train_ai(genome1, genome2, config)

def run_neat(config):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-1')
    # p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)


local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, "config.txt")
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
run_neat(config)
