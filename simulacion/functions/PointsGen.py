import numpy as np
import matplotlib.pyplot as plt

def generar_coordenadas_parapente(altura, n_puntos, tiempo_caida, r, velocidad_viento, area_paracaidas, area_lateral_objeto):
    """
    Genera coordenadas GPS para un objeto en parapente con descenso helicoidal, considerando la resistencia al aire y el viento.

    Args:
        altura (float): Altura inicial en metros.
        n_puntos (int): Número de puntos de datos a generar.
        tiempo_caida (float): Tiempo total de descenso en segundos.
        radio_helice (float): Radio de la hélice en metros.
        velocidad_viento (tuple): Tupla (x, y, z) con las componentes de la velocidad del viento en m/s.
        area_paracaidas (float): Área del paracaídas en metros cuadrados.
        area_lateral_objeto (float): Área lateral del objeto en metros cuadrados.

    Returns:
        list: Lista de tuplas (x, y, z) representando las coordenadas GPS.
    """
    
    # Calcular velocidad de descenso vertical
    v = altura / tiempo_caida

    # Calcular velocidad angular
    omega = 2 * np.pi / tiempo_caida

    # Generar puntos de datos en el tiempo
    t_values = np.linspace(0, tiempo_caida, n_puntos)

    # Calcular coordenadas x e y considerando el viento ECUACION DE TRAYECTORIA
    x = r * np.cos(omega * t_values) + velocidad_viento[0] * t_values
    y = r * np.sin(omega * t_values) + velocidad_viento[1] * t_values
 
    # Calcular la fuerza de arrastre
    densidad_aire = 1.225  # kg/m³
    coeficiente_arrastre = 1.75
    masa_objeto = 2  # kg (asumido)
    velocidad_vertical_relativa = v + velocidad_viento[2] 
    F_arrastre = 0.5 * densidad_aire * velocidad_vertical_relativa**2 * (area_paracaidas + area_lateral_objeto) * coeficiente_arrastre

    # Calcular la aceleración de arrastre
    a_arrastre = F_arrastre / masa_objeto

    # Calcular coordenada z considerando la resistencia al aire y el viento
    z = altura - velocidad_vertical_relativa * t_values + 0.5 * a_arrastre * t_values**2

    # Retornar coordenadas
    return [(x[i], y[i], z[i]) for i in range(n_puntos)]

# Llamar a la función con los argumentos proporcionados
coordenadas = generar_coordenadas_parapente(
    altura=3000,
    n_puntos=2000,
    tiempo_caida=100,
    r=5000,
    velocidad_viento=(15, 0, 0),
    area_paracaidas=2,
    area_lateral_objeto=0.03
)

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extraer las coordenadas x, y, z de la lista de tuplas
x = [coord[0] for coord in coordenadas]
y = [coord[1] for coord in coordenadas]
z = [coord[2] for coord in coordenadas]

# Graficar la trayectoria
ax.plot(x, y, z)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z (Altura)')

# Mostrar el gráfico
plt.show()