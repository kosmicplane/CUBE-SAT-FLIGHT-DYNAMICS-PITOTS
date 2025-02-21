import numpy as np
def V_Wind(couples, V_GPS, gps_w, V_IMU, imu_w):
    """Función usada para calcular la velocidad del viento."""
    
    # Convertir listas a arrays de numpy
    V_GPS = np.array(V_GPS)
    V_IMU = np.array(V_IMU)
    couples = np.array(couples)
    
    # Evitar división por cero
    if gps_w + imu_w == 0:
        stm = np.zeros(3)
    else:
        stm = ((V_GPS * gps_w) + (V_IMU * imu_w)) / (gps_w + imu_w)
    
    # Verificar dimensiones antes de restar
    if couples.shape[0] < 2:
        raise ValueError("El argumento 'couples' debe contener al menos dos elementos.")

    # Calcular el viento
    v_wind = stm - couples[0] - couples[1]
    
    return v_wind
