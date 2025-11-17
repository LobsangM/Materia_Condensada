from run import MonteCarloSimulation, load_config
from visualizer import Visualizer

def main():
    config = load_config("config.yaml")
    sim = MonteCarloSimulation(config)
    vis = Visualizer(sim, config)
    vis.run()

    # Guarda posiciones finales
    import numpy as np
    np.savetxt("positions_final.txt", sim.positions)
    print("Simulación completada. Posiciones guardadas en positions_final.txt")

if __name__ == "__main__":
    main()
