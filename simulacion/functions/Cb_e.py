import numpy as np
def C_b_e(psi, v):
    """
    Applies the Euler angle transformation to a vector 'v' using the angles in 'psi'.

    Args:
        psi: A 3-element vector containing the Euler angles (phi, theta, psi) in radians.
        v: A 3-element vector to be transformed in earth axis frame system.

    Returns:
        The transformed vector.
    """
    # Extract Euler angles
    phi, theta, psi = psi

    # Compute sines and cosines
    c_phi, s_phi = np.cos(phi), np.sin(phi)
    c_theta, s_theta = np.cos(theta), np.sin(theta)
    c_psi, s_psi = np.cos(psi), np.sin(psi)

    # Construct the direction cosine matrix
    C_be = np.array([
        [c_theta * c_psi, c_theta * s_psi, -s_theta],
        [-c_phi * s_psi + s_phi * s_theta * c_psi, c_phi * c_psi + s_phi * s_theta * s_psi, s_phi * c_theta],
        [s_phi * s_psi + c_phi * s_theta * c_psi, -s_phi * c_psi + c_phi * s_theta * s_psi, c_phi * c_theta]
    ])

    # Perform the transformation
    transformed_v = C_be @ v

    return transformed_v


