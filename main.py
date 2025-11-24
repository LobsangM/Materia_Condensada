from run import MonteCarloSimulation, load_config
from visualizer import Visualizer
import subprocess
import sys
import numpy as np
import os

def main():
    config = load_config("config.yaml")
    sim = MonteCarloSimulation(config)
    # Descomentar dos líneas siguietnes si se quiere visualizar la simulación (más lento)
    # vis = Visualizer(sim, config)
    # vis.run()
    # Comentar si solo se quiere ejecutar (más rápido)
    acceptance_rate, avg_dist_history = sim.run()
    print(f"Simulación completada. Tasa de aceptación final: {acceptance_rate:.2f}")

    # Guarda posiciones finales
    positions_file = "positions_final.txt"
    np.savetxt(positions_file, sim.positions)
    print("Simulación completada. Posiciones guardadas en positions_final.txt")

    # --- NUEVO BLOQUE PARA GUARDAR PARÁMETROS DE RED ---
    output_dir = "parametros_red"
    os.makedirs(output_dir, exist_ok=True)

    # Para nombrar la imagen final
    param_string = (
        f"s{config['max_steps']}_"
        f"N{config['N']}_"
        f"R{config['R']}_"
        f"ε{str(config['epsilon']).replace('.', '-')}_"
        f"σ{str(config['sigma']).replace('.', '-')}_"
        f"kT{str(config['kB_T']).replace('.', '-')}"
    )

   # Define el nombre para el único archivo de salida
    output_file = f"{output_dir}/{param_string}_avg_dist.txt"

    # Convierte el diccionario {paso: promedio} a un array de 2 columnas para guardarlo
    data_to_save = np.array(list(avg_dist_history.items()))

    # Guarda el array en un único archivo de texto
    np.savetxt(output_file, data_to_save, fmt='%.8f', header='Paso Promedio_Distancia_Minima')
    
    print(f"Evolución del parámetro de red guardada en '{output_file}'")

    subprocess.run([
        sys.executable, 
        "graficador.py", 
        positions_file, 
        param_string, 
        str(config["R"]),
        str(config["sigma"])
    ], check=True)

if __name__ == "__main__":
    main()
