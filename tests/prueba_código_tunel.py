import serial, time
import pandas as pd
from IPython.display import clear_output
import numpy as np
from datetime import datetime  # Importar para manejar tiempos

# Configuración del puerto serial
puerto = 'COM7'  # Cambia por el puerto que estés usando
baudios = 9600  # Ajusta la velocidad en baudios según tu dispositivo
timeout = 1  # Tiempo de espera en segundos
ser = serial.Serial(puerto, baudios, timeout=timeout)

# Definir las columnas
column_names = ["Pitot_1", "Pitot_2", "Pitot_3", "Pitot_4", "Timestamp"]  # Añadida columna para la hora

# Crear un DataFrame vacío
datos = pd.DataFrame(columns=column_names)

try:
    while True:
        # Leer datos del puerto serial
        datos_linea = ser.readline().decode('utf-8').strip()  # Decodifica y elimina espacios

        # Convertir datos a lista
        datos_lista = datos_linea.split(',')  # Separa los datos por comas (ajustar según el separador)

        # Verificar si el número de valores coincide con las columnas sin incluir el tiempo
        if len(datos_lista) == 1:
            continue

        if len(datos_lista) != len(column_names) - 1:  # Excluir la columna de tiempo para la comparación
            print(f"Warning: Received {len(datos_lista)} values, expected {len(column_names) - 1}")
            continue  # Omitir esta iteración si la longitud de datos no coincide

        # Añadir marca de tiempo a los datos
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Formato de tiempo legible
        datos_lista.append(timestamp)

        # Crear una nueva fila como un DataFrame
        nueva_fila = pd.DataFrame([datos_lista], columns=column_names)

        # Concatenar la nueva fila al DataFrame principal
        datos = pd.concat([datos, nueva_fila], ignore_index=True)

        # Convertir las columnas numéricas a tipo float
        datos[["Pitot_1", "Pitot_2", "Pitot_3", "Pitot_4"]] = datos[["Pitot_1", "Pitot_2", "Pitot_3", "Pitot_4"]].astype(float)

        # Mostrar la última fila registrada
        print(datos.iloc[-1])
        clear_output(wait=True)
except KeyboardInterrupt:
    # Cerrar el puerto serial
    ser.close()
    print('Lectura de datos finalizada.')

# Guardar el DataFrame en un archivo Excel con la fecha y hora incluida en el nombre
fecha_actual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f'prueba_tunel_{fecha_actual}.xlsx'
datos.to_excel(filename, sheet_name='Tunnel Data', index=False)  # Opcional: especificar nombre de la hoja

print(f'DataFrame saved to Excel file: {filename}')

