import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    """
    Función principal para cargar datos y generar una gráfica con escala dinámica.
    """
    # 1. Validar y leer 4 argumentos: script, posiciones, params, radio, sigma
    if len(sys.argv) != 5:
        print("Uso: python graficador.py <archivo_posiciones> <param_string> <radio_circulo> <sigma>")
        sys.exit(1)

    input_filename = sys.argv[1]
    param_string = sys.argv[2]
    radius = float(sys.argv[3])
    sigma = float(sys.argv[4])
    positions = np.loadtxt(input_filename)

    x_coords, y_coords = positions[:, 0], positions[:, 1]
    
    # Parsea el string de parámetros para el texto informativo (sin cambios)
    params_list = param_string.split('_')
    display_params = []
    for p in params_list:
        if p.startswith('s'):
            display_params.append(f"Pasos: {p[1:]}")
        elif p.startswith('kT'):
            display_params.append(f"Energía (kT): {p[2:].replace('-', '.')}")
        else:
            display_params.append(f"{p[0]}: {p[1:].replace('-', '.')}")
    info_text = "\n".join(display_params)

    # --- CAMBIO 1: DIBUJAR PARTÍCULAS CON RADIO REAL ---
    particle_radius = sigma / 2.0

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 10))

    # Dibuja el contenedor
    boundary = patches.Circle((0, 0), radius=radius, facecolor='none', edgecolor='#555555', linewidth=2, zorder=1)
    ax.add_patch(boundary)

    # Dibuja cada partícula como un círculo con radio físico sigma/2
    # Esto reemplaza a ax.scatter para un control preciso del tamaño.
    for x, y in zip(x_coords, y_coords):
        particle_patch = patches.Circle((x, y), radius=particle_radius, facecolor='yellow', zorder=2)
        ax.add_patch(particle_patch)

    # Añade el texto informativo (sin cambios)
    ax.text(0.03, 0.97, info_text,
            transform=ax.transAxes,
            fontsize=12,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))

    ax.set_title("Visualización de Posiciones Finales de la Simulación", fontsize=16)
    ax.set_xlabel("Coordenada X")
    ax.set_ylabel("Coordenada Y")

    # --- CAMBIO 2: LÍMITES DINÁMICOS DEL GRÁFICO ---
    # Ajusta los límites para que el contenedor ocupe ~90% del espacio visual.
    plot_limit = radius / 0.9
    ax.set_xlim(-plot_limit, plot_limit)
    ax.set_ylim(-plot_limit, plot_limit)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle='--', color='gray', alpha=0.3)

    output_filename = f"imagenes/{param_string}.png"
    plt.savefig(output_filename, dpi=150, bbox_inches='tight')
    
    print(f"Gráfica guardada en '{output_filename}'")

if __name__ == "__main__":
    main()