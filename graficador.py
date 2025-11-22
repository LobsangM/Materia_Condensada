import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# --- Parámetros de la simulación (obtenidos de config.yaml) ---
# Es importante usar el mismo radio que en la simulación para que la escala sea correcta.
R = 300.0
INPUT_FILENAME = "positions_final.txt"
# PARAMETROS = "config.yaml"

# --- 1. Cargar las posiciones desde el archivo ---
try:
    positions = np.loadtxt(INPUT_FILENAME)
    # parametros = np.loadtxt(PARAMETROS)
    print(f"Se cargaron {len(positions)} posiciones desde '{INPUT_FILENAME}'.")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{INPUT_FILENAME}'.")
    print("Por favor, asegúrate de que el archivo está en el mismo directorio que este script.")
    exit()
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
    exit()

# Extraer las coordenadas X e Y para la gráfica
x_coords = positions[:, 0]
y_coords = positions[:, 1]

# --- 2. Crear la gráfica ---
# Usamos un estilo con fondo oscuro para simular la ventana de pygame
plt.style.use('dark_background')

# Crear una figura y un eje. figsize controla el tamaño de la ventana.
fig, ax = plt.subplots(figsize=(10, 10))

# Dibujar el círculo de confinamiento
# Le damos un color gris claro, sin relleno (facecolor='none') y un orden bajo (zorder=1)
# para que aparezca detrás de las partículas.
boundary = patches.Circle((0, 0), radius=R, facecolor='none', edgecolor='#555555', linewidth=2, zorder=1)
ax.add_patch(boundary)

# Dibujar las partículas usando un scatter plot
# 's' es el tamaño del marcador (lo ajustamos para que se vea bien)
# 'c' es el color
# 'zorder=2' para que aparezcan por encima del círculo
ax.scatter(x_coords, y_coords, s=25, c='yellow', zorder=2)

# --- 3. Ajustar la apariencia de la gráfica ---
ax.set_title("Visualización de Posiciones Finales de la Simulación", fontsize=16)
ax.set_xlabel("Coordenada X")
ax.set_ylabel("Coordenada Y")

# Establecer los límites del gráfico para que el círculo no se corte
# y haya un pequeño margen
margin = 50
ax.set_xlim(-R - margin, R + margin)
ax.set_ylim(-R - margin, R + margin)

# Es CRUCIAL establecer el aspecto a 'equal' para que el círculo
# no se vea como una elipse si la ventana no es cuadrada.
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', color='gray', alpha=0.3)

# --- 4. Mostrar la gráfica ---
# plt.show()
plt.savefig(r'imagenes/resultado_final.png')
# print(parametros)