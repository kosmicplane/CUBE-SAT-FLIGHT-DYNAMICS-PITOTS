from scipy.signal import butter, filtfilt

def filtrar_datos_vertical(new, data_history, fs=400000, fc=10000, order=10):
    """
    Filtra los datos de sensores en tiempo real utilizando un filtro Butterworth.
    El desplazamiento de los datos históricos se realiza hacia abajo.
    
    Parámetros:
    - new: Lista con los nuevos datos de sensores.
    - data_history: DataFrame con el historial de datos de los sensores.
    - fs: Frecuencia de muestreo en Hz (default: 400000).
    - fc: Frecuencia de corte del filtro en Hz (default: 10000).
    - order: Orden del filtro Butterworth (default: 10).

    Retorna:
    - filtered_values: Lista de valores filtrados para cada sensor.
    """
    # Parámetros del filtro Butterworth
    nyquist = 0.5 * fs
    normal_cutoff = fc / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    
    # Lista para almacenar los valores filtrados
    filtered_values = []
    
    for i, dato in enumerate(new):
        # Desplazar el historial hacia abajo y agregar el nuevo dato en la primera posición
        data_history.iloc[1:, i] = data_history.iloc[:-1, i].values  # Desplazar hacia abajo
        data_history.iloc[0, i] = dato  # Insertar el nuevo dato en la primera fila
        
        # Filtrar el historial completo del sensor y obtener el último valor filtrado
        filtered_value = filtfilt(b, a, data_history.iloc[:, i].values)[-1]
        filtered_values.append(filtered_value)
    
    return filtered_values, data_history