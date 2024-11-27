# programacion2_24
Repo de proyectos de la materia de programación 2
import numpy as np

def evaluar_pendiente(coordenadas):
    """
    Evalúa las pendientes de una curva a partir de datos topográficos.
    Parámetros:
    - coordenadas: Lista de puntos (x, y, z) representando la curva.

    Retorna:
    - Informe sobre las pendientes y áreas problemáticas.
    """
    pendientes = []
    problemas = []

    for i in range(len(coordenadas) - 1):
        x1, y1, z1 = coordenadas[i]
        x2, y2, z2 = coordenadas[i + 1]

        distancia = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        pendiente = (z2 - z1) / distancia if distancia != 0 else 0
        pendientes.append(pendiente)

        if pendiente < 0.02:  # Umbral para pendientes mínimas (2%)
            problemas.append((i, pendiente))

    return pendientes, problemas

def sugerir_soluciones(problemas):
    """
    Propone soluciones según las áreas problemáticas detectadas.
    """
    soluciones = []
    for idx, pendiente in problemas:
        if pendiente <= 0:
            soluciones.append(f"En el segmento {idx}: nivelar el terreno.")
        else:
            soluciones.append(f"En el segmento {idx}: aumentar pendiente.")
    return soluciones

# Ejemplo de datos topográficos (coordenadas x, y, z)
datos_topográficos = [
    (0, 0, 100), (10, 0, 99.8), (20, 0, 99.5), (30, 0, 99.2), (40, 0, 99)
]

pendientes, problemas = evaluar_pendiente(datos_topográficos)
soluciones = sugerir_soluciones(problemas)

# Imprimir resultados
print("Pendientes de la curva:", pendientes)
if problemas:
    print("\nProblemas detectados:")
    for idx, pendiente in problemas:
        print(f" - Segmento {idx}: pendiente {pendiente:.4f}")

    print("\nSoluciones sugeridas:")
    for solucion in soluciones:
        print(" -", solucion)
else:
    print("\nNo se detectaron problemas de pendiente.")
