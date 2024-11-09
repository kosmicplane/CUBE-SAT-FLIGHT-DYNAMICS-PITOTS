import numpy as np

def func_auto(sensor_data):
    """
    Calculates the average of each sensor's readings.

    Parameters:
    sensor_data (dict): A dictionary with each sensor's readings.

    Returns:
    dict: A dictionary with the average for each sensor.
    """
    averages = {sensor: np.mean(readings) for sensor, readings in sensor_data.items()}
    return averages