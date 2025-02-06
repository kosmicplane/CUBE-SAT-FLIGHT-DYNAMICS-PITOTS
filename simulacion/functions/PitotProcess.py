from functions.Ce_b import C_e_b, np
def PitotProcess(pitots, pressure, temperature,psi):
    """_summary_

    Args:
        pitots (list): presion en Pa indicada por los pitots [p1,p2,p3,p4]
        pressure (float): presion indicada por el barometro
        temperature (float): temperatura indicada por el termometro en celsius
        psi (list): angulos de euler entregados por la imu

    Returns:
        list: lista compuesta por los dos vectores de velocidad de la pareja de pitots
    """
    rho = (pressure*0.02897)/(8.314472*(temperature+273.15)) #Se calcula la densidad del aire con ecuación de gases ideales rho = PM/RT
    velocity = list(map(lambda x: ((2*abs(x)/rho)**0.5), pitots)) # Se aplica la ecuacion de Bernoulli
    velocity_Couple1 = [velocity[0],velocity[1],0]  #desconocemos la componente en z de corrientes en 0, por ahora se asumira en 0 y se evaluara su impacto
    velocity_Couple2 = [velocity[2],velocity[3],0] #desconocemos la componente en z de corrientes en 0, por ahora se asumira en 0 y se evaluara su impacto
    velocity_Couple1, velocity_Couple2 = C_e_b(psi, velocity_Couple1), C_e_b(psi, velocity_Couple2)
    return [velocity_Couple1,velocity_Couple2]
    
    #EN ESTA FUNCION "PitotProcess" SE DEBE REVISAR LAS PAREJAS DE PITOT. ESTAS PRIMERO DEBERIAN RESTARSE Y LUEGO SI TRANSFORMARSE