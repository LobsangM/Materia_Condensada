import pygame
import numpy as np

class Visualizer:
    """
    Clase encargada de mostrar la simulación Monte Carlo en tiempo real.
    """
    def __init__(self, simulation, config):
        pygame.init()
        self.sim = simulation
        self.config = config
        self.screen_size = int(2 * (config["R"] + 50))
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.center = np.array([self.screen_size / 2, self.screen_size / 2])
        pygame.display.set_caption("Simulación Monte Carlo - Lennard-Jones")
        self.clock = pygame.time.Clock()
        self.running = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.circle(self.screen, (50, 50, 50), self.center.astype(int), self.config["R"], 1)

        for pos in self.sim.positions:
            x, y = self.center + pos
            pygame.draw.circle(self.screen, (255, 255, 0), (int(x), int(y)), 5)

        pygame.display.flip()

    def run(self):
        step = 0
        while self.running and step < self.config["max_steps"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.sim.step()
            self.draw()
            step += 1
            self.clock.tick(self.config["fps"])

        pygame.quit()
