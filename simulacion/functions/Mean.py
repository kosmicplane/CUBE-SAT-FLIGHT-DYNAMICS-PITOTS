import numpy as np
def mean(data):
   """
    Applies the Euler angle transformation to a vector 'v' using the angles in 'psi'.

    Args:
        data: vector with the sample group vectors, format -> [vector1,vector2,vector3].

    Returns:
        The mean value of each component of the vector.
    """
   arr = np.array(data)
   # Calcular el promedio de cada componente (a lo largo de las filas)
   v_mean = np.mean(arr, axis=0)
   return v_mean