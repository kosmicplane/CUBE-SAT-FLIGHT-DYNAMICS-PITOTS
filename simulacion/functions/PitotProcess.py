from .Ce_b import C_e_b, np
def PitotProcess(pitots, pressure, temperature,psi):
    """_summary_

    Args:
        pitots (list): presion en Pa indicada por los pitots [p1,p2,p3,p4]
        pressure (float): presion indicada por el barometro
        temperature (float): temperatura indicada por el barometro
        psi (list): angulos de euler entregados por la imu

    Returns:
        list: lista compuesta por los dos vectores de velocidad de la pareja de pitots
    """
    rho = pressure/(287*(temperature+275))
    velocity = list(map(lambda x: ((2*(x-pressure)/rho)**0.5), pitots))
    velocity_Couple1 = [velocity[0],velocity[1],0]  #desconocemos la componente en z de corrientes en 0, por ahora se asumira en 0 y se evaluara su impacto
    velocity_Couple2 = [velocity[2],velocity[3],0] #desconocemos la componente en z de corrientes en 0, por ahora se asumira en 0 y se evaluara su impacto
    velocity_Couple1, velocity_Couple2 = C_e_b(psi, velocity_Couple1), C_e_b(psi, velocity_Couple2)
    return [velocity_Couple1,velocity_Couple2]
