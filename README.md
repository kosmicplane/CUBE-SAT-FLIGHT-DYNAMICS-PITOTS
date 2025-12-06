# Modelo-Matematico

Atipaná es un nanosatélite atmosférico pensado como "space port" para validar un sistema de cuatro sensores multipitot. Su objetivo es muestrear corrientes de viento y medir propiedades del aire (presión, humedad, temperatura) a distintas altitudes en un rango de 500 metros. El proyecto, desarrollado por estudiantes de la Universidad de Antioquia y la Universidad Pontificia Bolivariana, busca comprender la dinámica de las corrientes de aire, validar el diseño del sistema y, potencialmente, ampliar la misión para caracterizar la calidad del aire y explorar aplicaciones en energía eólica.

![image](https://github.com/user-attachments/assets/b5f616e5-621c-4c23-b7dd-434653c2727a)

## Contenido del repositorio

- `simulacion/`: Jupyter Notebooks y utilidades de simulación para procesar datos de vuelo y pruebas de túnel de viento.
  - `functions/`: Biblioteca de funciones para el procesamiento de los pitots y la navegación:
    - `PitotProcess.py`: calcula la velocidad del viento en el marco NED a partir de las lecturas de los cuatro pitots, la densidad del aire y los ángulos de Euler de la IMU.
    - `Ce_b.py` / `Cb_e.py`: matrices de transformación entre ejes cuerpo y sistema tierra para rotar vectores medidos.
    - `calcVelocity.py` y `timeintegration.py`: integran aceleraciones lineales de la IMU para estimar velocidades en cada eje.
    - `ISA.py`: densidad y presión atmosférica según el modelo ISA para ajustar los cálculos aerodinámicos a la altitud.
    - `func_auto_calib.py`: cálculo de promedios por sensor para facilitar la calibración automática.
    - Scripts adicionales (`V_Wind.py`, `PointsGen.py`, filtros de datos reales) para generación de trayectorias y depuración de series temporales.
  - `main.ipynb`, `proccesor.ipynb` y `create_fake_data.ipynb`: notebooks para probar el pipeline de simulación, generar datos sintéticos y validar el preprocesamiento.
- `Tests/`: recursos para adquisición y pruebas en túnel de viento.
  - `test_tunnel_code.py`: script de lectura serial (ej. `COM7`, 9600 baudios) que captura presiones de cuatro pitots, agrega marcas de tiempo y exporta los registros a Excel.
  - `functions_testing.ipynb` y `tunnel_sampling.ipynb`: notebooks de verificación de funciones y muestreo.
- Archivos de datos de ejemplo (`Prueba_recolectada.txt`, `datos_vuelo_200_filas.csv`, `prueba_tunel_*.xlsx`) para reproducir el análisis y ajustar filtros.

## Propósito y alcance

El repositorio sirve como base para el desarrollo del sistema de dinámica de vuelo de un satélite equipado con un arreglo multipitot de cuatro sensores. La combinación de utilidades de simulación y scripts de adquisición permite:

- Validar la arquitectura de sensores y algoritmos de fusión (transformaciones cuerpo–tierra y corrección con IMU).
- Probar en túnel de viento la respuesta de los pitots antes del vuelo y generar datasets calibrados.
- Estimar velocidades de viento relativas integrando datos de aceleración y densidad atmosférica.

## Requisitos sugeridos

- Python 3.10+ con `numpy`, `pandas`, `pyserial` y `ipython` para ejecutar los scripts y notebooks.
- Ambiente con puerto serial disponible para las pruebas de túnel (`test_tunnel_code.py`).

## Cómo empezar

1. Explora los datasets de ejemplo en `simulacion/` o ejecuta `create_fake_data.ipynb` para generar datos sintéticos.
2. Ajusta el puerto y baudios en `Tests/test_tunnel_code.py` y ejecuta el script para registrar nuevas pruebas de túnel de viento. Los datos se guardarán en un archivo Excel con marca de tiempo.
3. Usa `simulacion/main.ipynb` o `proccesor.ipynb` para procesar los datos registrados: integra aceleraciones IMU, convierte velocidades al marco NED y estima el campo de viento con el modelo ISA.

## Próximos pasos sugeridos

- Documentar los parámetros de montaje físico de los cuatro pitots para facilitar la calibración cruzada.
- Añadir pruebas unitarias para las transformaciones `C_e_b` y la integración de velocidades.
- Automatizar la generación de reportes de túnel de viento a partir de los archivos Excel exportados.
