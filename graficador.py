import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    """
    Función principal para cargar datos de simulación y generar una gráfica.
    """
    if len(sys.argv) != 4:
        print("Uso: python graficador.py <archivo_de_posiciones> <string_de_parametros> <radio_del_circulo>")
        sys.exit(1)

    input_filename = sys.argv[1]
    param_string = sys.argv[2]
    radius = float(sys.argv[3])
    positions = np.loadtxt(input_filename)

    x_coords, y_coords = positions[:, 0], positions[:, 1]

    # --- NUEVA SECCIÓN: Preparar el texto de los parámetros ---
    # Parsea el param_string (ej: s50000_N100_...) para mostrarlo en la gráfica
    params_list = param_string.split('_')
    display_params = []
    for p in params_list:
        if p.startswith('s'):
            display_params.append(f"Pasos: {p[1:]}")
        elif p.startswith('kT'):
            # El prefijo es de 2 caracteres
            display_params.append(f"Energía (kT): {p[2:].replace('-', '.')}")
        else:
            # El resto de prefijos son de 1 caracter (N, R, ε, σ)
            display_params.append(f"{p[0]}: {p[1:].replace('-', '.')}")
    
    info_text = "\n".join(display_params)
    # --- FIN DE LA NUEVA SECCIÓN ---


    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 10))

    boundary = patches.Circle((0, 0), radius=radius, facecolor='none', edgecolor='#555555', linewidth=2, zorder=1)
    ax.add_patch(boundary)

    ax.scatter(x_coords, y_coords, s=25, c='yellow', zorder=2)

    # --- NUEVA SECCIÓN: Añadir el texto a la gráfica ---
    # Coloca el texto en la esquina superior izquierda.
    # transform=ax.transAxes usa coordenadas relativas al tamaño de la gráfica (0,0 es abajo-izquierda, 1,1 es arriba-derecha).
    ax.text(0.03, 0.97, info_text,
            transform=ax.transAxes,
            fontsize=12,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))
    # --- FIN DE LA NUEVA SECCIÓN ---


    ax.set_title("Visualización de Posiciones Finales de la Simulación", fontsize=16)
    ax.set_xlabel("Coordenada X")
    ax.set_ylabel("Coordenada Y")

    margin = 50
    ax.set_xlim(-radius - margin, radius + margin)
    ax.set_ylim(-radius - margin, radius + margin)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle='--', color='gray', alpha=0.3)

    output_filename = f"imagenes/{param_string}.png"
    plt.savefig(output_filename, dpi=150, bbox_inches='tight')
    
    print(f"Gráfica guardada en '{output_filename}'")

if __name__ == "__main__":
    main()