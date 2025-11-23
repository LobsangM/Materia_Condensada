import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    """
    Función principal para cargar datos de simulación y generar una gráfica.
    """
    # 1. Validar y leer los argumentos de la línea de comandos
    if len(sys.argv) != 4:
        # Se esperan 3 argumentos: nombre_script, archivo_posiciones, string_params, radio
        print("Uso: python graficador.py <archivo_de_posiciones> <string_de_parametros> <radio_del_circulo>")
        sys.exit(1)

    input_filename = sys.argv[1]
    param_string = sys.argv[2]
    try:
        # El radio se recibe como string, hay que convertirlo a número
        radius = float(sys.argv[3])
    except ValueError:
        print("Error: El radio debe ser un número.")
        sys.exit(1)

    # 2. Cargar las posiciones desde el archivo
    try:
        positions = np.loadtxt(input_filename)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de entrada '{input_filename}'.")
        sys.exit(1)

    # Separar coordenadas X e Y
    x_coords, y_coords = positions[:, 0], positions[:, 1]

    # 3. Configurar y crear la gráfica
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 10))

    # Dibujar el círculo de confinamiento usando el radio recibido
    boundary = patches.Circle((0, 0), radius=radius, facecolor='none', edgecolor='#555555', linewidth=2, zorder=1)
    ax.add_patch(boundary)

    # Dibujar las partículas
    ax.scatter(x_coords, y_coords, s=25, c='yellow', zorder=2)

    # Configurar etiquetas, título y límites del gráfico
    ax.set_title("Visualización de Posiciones Finales de la Simulación", fontsize=16)
    ax.set_xlabel("Coordenada X")
    ax.set_ylabel("Coordenada Y")

    margin = 50
    ax.set_xlim(-radius - margin, radius + margin)
    ax.set_ylim(-radius - margin, radius + margin)
    ax.set_aspect('equal', adjustable='box') # Asegura que el círculo se vea como un círculo
    ax.grid(True, linestyle='--', color='gray', alpha=0.3)

    # 4. Guardar la figura en un archivo
    output_filename = f"imagenes/sim_{param_string}.png"
    plt.savefig(output_filename, dpi=150, bbox_inches='tight')
    
    # Este print se verá en la consola donde se ejecuta main.py
    print(f"Gráfica guardada en '{output_filename}'")

if __name__ == "__main__":
    main()