import numpy as np
from calculations import LennardJones
import yaml

class MonteCarloSimulation:
    """
    Implementa el algoritmo de Metropolis Monte Carlo
    para un conjunto de partículas en un círculo 2D.
    """
    def __init__(self, config):
        self.N = config["N"]
        self.R = config["R"]
        self.epsilon = config["epsilon"]
        self.sigma = config["sigma"]
        self.kB_T = config["kB_T"]
        self.step_size = config["step_size"]
        self.max_steps = config["max_steps"]

        self.lj = LennardJones(self.epsilon, self.sigma)
        self.positions = self._initialize_positions()
        self.energy = self.lj.total_energy(self.positions)

    def _initialize_positions(self):
        """Genera posiciones iniciales aleatorias dentro del círculo."""
        positions = []
        for _ in range(self.N):
            r = self.R * np.sqrt(np.random.random())
            theta = 2 * np.pi * np.random.random()
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            positions.append(np.array([x, y]))
        return np.array(positions)

    def step(self):
        """Ejecuta un paso de Monte Carlo."""
        i = np.random.randint(0, self.N)
        move = (np.random.rand(2) - 0.5) * 2 * self.step_size
        new_pos = self.positions[i] + move

        # No permite movimientos fuero del circulo
        if np.linalg.norm(new_pos) > self.R:
            return False

        dE = self.lj.delta_energy(self.positions, i, new_pos)
        if dE < 0 or np.random.random() < np.exp(-dE / self.kB_T):
            self.positions[i] = new_pos
            self.energy += dE
            return True
        return False

    def run(self):
        """Ejecuta toda la simulación."""
        accepted = 0
        for _ in range(self.max_steps):
            if self.step():
                accepted += 1
        return accepted / self.max_steps

def load_config(filename="config.yaml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
