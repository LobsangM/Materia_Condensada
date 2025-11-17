import numpy as np

class LennardJones:
    """
    Clase para calcular energía total y variaciones de energía
    usando el potencial de Lennard-Jones en 2D.
    """
    def __init__(self, epsilon=1.0, sigma=1.0):
        self.epsilon = epsilon
        self.sigma = sigma

    def potential(self, r):
        """Potencial Lennard-Jones U(r) = 4ε[(σ/r)^12 - (σ/r)^6]."""
        if r == 0:
            return 0
        sr6 = (self.sigma / r) ** 6
        return 4 * self.epsilon * (sr6**2 - sr6)

    def total_energy(self, positions):
        """Calcula la energía total del sistema."""
        E = 0.0
        N = len(positions)
        for i in range(N):
            for j in range(i + 1, N):
                r = np.linalg.norm(positions[i] - positions[j])
                E += self.potential(r)
        return E

    def delta_energy(self, positions, index, new_pos):
        """
        Calcula el cambio de energía al mover una partícula específica.
        """
        N = len(positions)
        dE = 0.0
        for j in range(N):
            if j != index:
                r_old = np.linalg.norm(positions[index] - positions[j])
                r_new = np.linalg.norm(new_pos - positions[j])
                dE += self.potential(r_new) - self.potential(r_old)
        return dE
