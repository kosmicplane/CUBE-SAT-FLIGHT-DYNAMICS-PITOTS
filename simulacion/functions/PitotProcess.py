from functions.Ce_b import C_e_b, np
def PitotProcess(pitots, rho, euler_angles, imu_velocity):
    """_summary_

    Args:
        pitots (list): presion en Pa indicada por los pitots [p1,p2,p3,p4]
        pressure (float): presion indicada por el barometro
        temperature (float): temperatura indicada por el termometro en celsius
        rho (float): densidad del aire en kg/m^3
        psi (list): angulos de euler entregados por la imu

    Returns:
        list: lista compuesta por los dos vectores de velocidad de la pareja de pitots
    """
    #rho = (pressure*0.02897)/(8.314472*(temperature+273.15)) #Se calcula la densidad del aire con ecuación de gases ideales rho = PM/RT
    velocity = list(map(lambda x: ((2*abs(x)/rho)**0.5), pitots))
    velocity_Couple1 = velocity[0] - velocity[2] # En eje X de IMU
    velocity_Couple2 = velocity[1] - velocity[3] # En eje Y de IMU
    wind_velocity_pitots_body = np.array([velocity_Couple1, velocity_Couple2, 0]) # Crea en X la primera pareja de pitots y en Y la segunda pareja de pitots
    wind_velocity_pitots_earth = C_e_b(euler_angles, wind_velocity_pitots_body) # Transforma la velocidad de pitots a sistema de referencia de la tierra
    #velocity_Couple2 = C_e_b(euler_angles, velocity_Couple2)
    #return [velocity_Couple1,velocity_Couple2]
    imu_velocity_earth = C_e_b(euler_angles, imu_velocity) # Transforma la velocidad de la IMU a sistema de referencia de la tierra
    wind_velocity_NED = wind_velocity_pitots_earth - imu_velocity_earth # Calcula la velocidad del viento en el sistema de tierra
    return wind_velocity_NED
    
    #EN ESTA FUNCION "PitotProcess" SE DEBE REVISAR LAS PAREJAS DE PITOT. ESTAS PRIMERO DEBERIAN RESTARSE Y LUEGO SI TRANSFORMARSE