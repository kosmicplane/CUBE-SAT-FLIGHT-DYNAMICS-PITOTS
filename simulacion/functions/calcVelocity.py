from functions.timeintegration import timeintegration, np
def calcVelocity(dataset, dt=0.01):
    """
    Calcula las velocidades integrando la aceleración IMU y las agrega al dataset.
    
    Parámetros:
    - dataset: DataFrame con columnas 'lin_accel_x', 'lin_accel_y', 'lin_accel_z'
    - dt: paso de tiempo entre muestras (en segundos)

    Retorna:
    - dataset con nuevas columnas: 'vel_x', 'vel_y', 'vel_z'
    """
    # Crear eje temporal
    t = np.arange(0, len(dataset) * dt, dt)

    # Asegurar que tenga el mismo tamaño que el dataset
    if len(t) > len(dataset):
        t = t[:len(dataset)]

    # Integrar cada componente
    vel_x = timeintegration(dataset['lin_accel_x'].values, t)
    vel_y = timeintegration(dataset['lin_accel_y'].values, t)
    vel_z = timeintegration(dataset['lin_accel_z'].values, t)

    # Agregar al dataset
    dataset['vel_x'] = vel_x
    dataset['vel_y'] = vel_y
    dataset['vel_z'] = vel_z

    return dataset