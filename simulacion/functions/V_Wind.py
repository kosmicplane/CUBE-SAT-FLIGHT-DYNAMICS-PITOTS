def V_Wind(couples,V_GPS, gps_w, V_IMU, imu_w):
    """funcion usada para calcular la velocidad dle viento

    Args:
        couples (list): lista de compuesta de dos parejas de pitots
        V_GPS (list): lista compuesta de la velocidad del cg segun gps
        gps_w (float): peso del gps en las mediciones (0-1)
        V_IMU (list): lista compuesta de la velocidad de la imu segun el gps 
        imu_w (float): peso de la imu en las mediciones (0-1)

    Returns:
        list: un vector compuesto por las componentes de velocidad del aire
    """
    stm = ((V_GPS*gps_w)+(V_IMU*imu_w))/(gps_w+imu_w)
    v_wind = [couples-couples[0],couples[1]]
    return v_wind