# -*- coding: utf-8 -*-
"""Proyecto Integrador.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IXq3dWAdZuXDPYxY_qovqx_zhJpOQoE0

PROYECTO DE FRACCIONAMIENTO DE LA AVENIDA NIÑOS HERORES
"""

from google.colab import drive
drive.mount('/content/drive')

from google.colab import drive
import folium

# PROYECTO DE FRACCIONAMIENTO DE LA AVENIDA NIÑOS HERORES
drive.mount('/content/drive')

# Ruta al archivo shape de Colima (ajusta la ruta según tu ubicación en Google Drive)
colima_shapefile = "/content/drive/MyDrive/Argis/Buffer de 50m_Avenida Niños Heores.shp"  # Reemplaza con la ruta correcta
ruta_archivo2 = "/content/drive/MyDrive/Buffer de 50m_Avenida Niños HeoresCopy.shp"

# Crear un mapa centrado en Colima
m = folium.Map(location=[19.24, -103.72], zoom_start=9) # Coordenadas aproximadas de Colima

# Agregar el archivo shape de Colima al mapa (usando GeoJson)
# Si el archivo shapefile no está en GeoJSON, necesitas convertirlo
# Puedes usar herramientas como QGIS o GDAL/OGR para la conversión.

try:
  folium.GeoJson(colima_shapefile, name="Colima").add_to(m)
except Exception as e:
  print(f"Error al cargar el archivo shape de Colima: {e}")
  print("Asegúrate de que la ruta del archivo es correcta y que el archivo es un shapefile válido o un GeoJSON.")



# Mostrar el mapa
m

# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear malla simplificada
x = np.linspace(0, 100, 100)  # Longitud (menos puntos para mayor velocidad)
y = np.linspace(0, 50, 50)   # Ancho
x, y = np.meshgrid(x, y)

# Relieve inicial
z_initial = np.zeros_like(x)
channel_depth = 2  # Profundidad de los canales en metros
z_initial[:, :10] = -channel_depth  # Canal izquierdo
z_initial[:, -10:] = -channel_depth  # Canal derecho

# Relieve final con carretera elevada
z_final = z_initial.copy()
z_final[:, 10:30] = 1  # Carretera elevada en el centro

# Configurar la figura
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Función para actualizar la animación
def update(frame):
    ax.clear()
    ax.set_title("Transformación: Avenida con canales", fontsize=12)
    ax.set_xlabel("Longitud (m)")
    ax.set_ylabel("Ancho (m)")
    ax.set_zlabel("Altura (m)")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.set_zlim(-3, 2)

    # Interpolación entre estado inicial y final
    progress = frame / 50  # Menos cuadros para rapidez
    z_current = z_initial * (1 - progress) + z_final * progress

    # Dibujar superficie
    ax.plot_surface(x, y, z_current, cmap="terrain", edgecolor="none")

# Crear animación
anim = FuncAnimation(fig, update, frames=51, interval=100)

# Mostrar animación
from IPython.display import HTML
HTML(anim.to_jshtml())

# Definir dimensiones básicas del canal
channel_width = 10  # Ancho de cada canal (en metros)
channel_depth = 2   # Profundidad (en metros)
channel_length = 100  # Longitud del canal (en metros)

# Calcular volumen del canal (asumimos sección rectangular)
canal_area = channel_width * channel_depth  # Área en m²
volume_per_canal = canal_area * channel_length  # Volumen en m³
total_volume = 2 * volume_per_canal  # Volumen de ambos canales

print(f"El volumen máximo de agua por canal es: {volume_per_canal:.2f} m³")
print(f"El volumen total para los dos canales es: {total_volume:.2f} m³")