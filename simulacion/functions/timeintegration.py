from .Mean import mean, np
def timeintegration(dot,t):
    """
    Funcion usada para hacer integracion cuando se tienen valores de las derivadas
    
    arg:
    dot (numpy array): valores de las derivadas
    t (float): tiempo
    """
    dot,t = np.array(dot),np.array(t)
    dt = np.diff(t)
    integrated = np.cumsum((dot[:-1] + dot[1:]) / 2 * dt)
    integrated = np.insert(integrated, 0, 0)
    return integrated