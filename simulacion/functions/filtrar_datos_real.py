def filtrar_datos(nuevos_datos, data_history):
    """
    Filtra los datos de sensores en tiempo real utilizando un filtro Butterworth.
    
    Parámetros:
    - nuevos_datos: Lista de valores actuales de los sensores
    - fs: Frecuencia de muestreo en Hz
    - fc: Frecuencia de corte del filtro en Hz
    - order: Orden del filtro Butterworth
    - data_history: Matriz de historial de datos para los sensores
    
    Retorna:
    - filtered_values: Lista de valores filtrados para los sensores.
    """

    from scipy.signal import butter, filtfilt
    
    # Parámetros del filtro
    fs = 400000    # Frecuencia de muestreo
    fc = 10000     # Frecuencia de corte
    order = 10     # Orden del filtro
    
    # Parámetros del filtro Butterworth
    nyquist = 0.5 * fs
    normal_cutoff = fc / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    
    # Filtrar cada sensor y actualizar su historial
    filtered_values = []
    for i, dato in enumerate(nuevos_datos):
        # Desplazar el historial a la izquierda y agregar el nuevo valor al final
        print (i,dato)
        data_history[i, :-1] = data_history[i, 1:]  # Desplazar a la izquierda
        data_history[i, -1] = dato                   # Insertar el nuevo dato al final

        # Filtrar el historial completo del sensor y obtener el último valor filtrado
        filtered_value = filtfilt(b, a, data_history[i, :])[-1]
        filtered_values.append(filtered_value)
    
    return filtered_value