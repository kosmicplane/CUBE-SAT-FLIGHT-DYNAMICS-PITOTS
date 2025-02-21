import numpy as np
def Psi_dot(Psi,Omegab):
    """
    This function transforms angular rates expressed in the Euler angle frame (roll rate, pitch rate, yaw rate) to angul
    ar rates expressed in the body frame of the aircraft (p, q, r). It achieves this transformation using a matrix that
    depends on the current attitude (Euler angles) of the aircraft.
    
    Args:
        psi: A 3-element vector containing the Euler angles (phi, theta, psi) in radians.
        Omegab: Angular velocity in body frame axis.

    Returns:
        The Psidot vector wich contains the angular speed in eart frame system.
    """
    phi, theta, psi = Psi
    c_phi, s_phi = np.cos(phi), np.sin(phi)
    c_theta, s_theta = np.cos(theta), np.sin(theta)
    H = np.array([
        [1, np.tan(theta) * s_phi, np.tan(theta) * c_phi],
        [0, c_phi, -s_phi],
        [0, s_phi / c_theta, c_phi / c_theta]
    ])
    psi_dot = H @ Omegab
    return psi_dot