def ISA(altitud, temperatura):
    """
    Calcula la densidad del aire y la presión estática según la Atmósfera Estándar Internacional (ISA).

    Args:
        altitud: Altitud en metros.
        temperatura: Temperatura en grados Celsius.

    Returns:
        Una tupla que contiene la densidad del aire en kg/m^3 y la presión estática en pascales.
    """

    # Constantes de la ISA
    temperatura_0 = 15.0  # Temperatura al nivel del mar en grados Celsius
    presion_0 = 101325.0  # Presión al nivel del mar en pascales
    gradiente_temperatura = -0.0065  # Gradiente de temperatura en °C/m
    R = 287.05  # Constante de los gases ideales para el aire en J/(kg·K)
    g = 9.80665  # Aceleración de la gravedad en m/s^2

    # Capa de la troposfera (hasta 11,000 metros)
    if altitud <= 11000:
        temperatura_isa = temperatura_0 + gradiente_temperatura * altitud
        presion_isa = presion_0 * (1 + (gradiente_temperatura * altitud) / temperatura_0) ** (-g / (R * gradiente_temperatura))
    # Capa de la tropopausa (de 11,000 a 20,000 metros)
    elif altitud <= 20000:
        temperatura_isa = -56.5  # Temperatura constante en la tropopausa
        presion_isa = 22632.1 * np.exp(-g / (R * temperatura_isa) * (altitud - 11000))

    # Capas superiores (no implementadas en este ejemplo)
    else:
        raise NotImplementedError("Cálculo para altitudes superiores a 20,000 metros no implementado.")

    # Calcular la densidad del aire
    densidad = presion_isa / (R * (temperatura_isa + 273.15))  # Convertir temperatura a Kelvin
    return densidad, presion_isa