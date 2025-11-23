from run import MonteCarloSimulation, load_config
from visualizer import Visualizer
import subprocess
import sys
import numpy as np

def main():
    config = load_config("config.yaml")
    sim = MonteCarloSimulation(config)
    # Descomentar dos líneas siguietnes si se quiere visualizar la simulación (más lento)
    # vis = Visualizer(sim, config)
    # vis.run()
    # Comentar si solo se quiere ejecutar (más rápido)
    sim.run()

    # Guarda posiciones finales
    positions_file = "positions_final.txt"
    np.savetxt(positions_file, sim.positions)
    print("Simulación completada. Posiciones guardadas en positions_final.txt")

    # Para nombrar la imagen final
    param_string = (
        f"s{config['max_steps']}_"
        f"N{config['N']}_"
        f"R{config['R']}_"
        f"ε{str(config['epsilon']).replace('.', '-')}_"
        f"σ{str(config['sigma']).replace('.', '-')}_"
        f"kT{str(config['kB_T']).replace('.', '-')}"
    )
    subprocess.run([
        sys.executable, 
        "graficador.py", 
        positions_file, 
        param_string, 
        str(config["R"])
    ], check=True)

if __name__ == "__main__":
    main()
