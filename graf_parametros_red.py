import sys
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Carga y grafica la evolución de un parámetro de red desde un archivo de texto.
    """
    # 1. Validar y obtener el nombre del archivo desde la línea de comandos
    if len(sys.argv) != 2:
        print("Uso: python plot_evolution.py <ruta_al_archivo_de_datos>")
        print("Ejemplo: python plot_evolution.py parametros_red/s50000_N100_..._avg_dist.txt")
        sys.exit(1)
        
    input_filename = sys.argv[1]

    # 2. Cargar los datos desde el archivo
    try:
        # np.loadtxt ignora automáticamente las líneas que empiezan con '#' (el encabezado)
        data = np.loadtxt(input_filename)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{input_filename}'")
        sys.exit(1)
    
    # Separar los datos en columnas para el eje X (pasos) y el eje Y (distancia)
    steps = data[:, 0]
    avg_distances = data[:, 1]

    # 3. Crear la gráfica
    plt.style.use('seaborn-v0_8-whitegrid') # Un estilo visualmente agradable para análisis
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(steps, avg_distances, marker='o', linestyle='-', markersize=5, label='Promedio Dist. Mínima')

    # Configurar etiquetas y título para que la gráfica sea clara
    ax.set_title("Evolución del Parámetro de Red Durante la Simulación", fontsize=16)
    ax.set_xlabel("Paso de la Simulación (Step)", fontsize=12)
    ax.set_ylabel("Promedio de la Distancia Mínima", fontsize=12)
    ax.legend()
    
    # Ajustar los límites para que la gráfica no se sienta apretada
    ax.set_xlim(left=0)
    
    print("Mostrando la gráfica... Cierra la ventana para terminar el programa.")

    # 4. Mostrar la gráfica interactiva
    plt.show()

if __name__ == "__main__":
    main()