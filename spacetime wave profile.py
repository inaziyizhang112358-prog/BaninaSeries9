import numpy as np

# Constants
c = 3e8  # m/s
G = 6.674e-11  # m^3 kg^-1 s^-2
M_spaceship = 22 * 0.453592  # 22 lbs in kg (~10 kg)
distance_ly = 1
distance_meters = distance_ly * 9.461e15

# Linear kinetic energy to travel 1 ly in 1 year (v = c)
# For a rough relativistic kinetic energy at v=0.9c: gamma = 1/sqrt(1-0.81) = 1/0.435 = 2.29
gamma = 1.0 / np.sqrt(1 - 0.9**2)
E_linear = (gamma - 1) * M_spaceship * (c**2)

# Spacetime warp energy estimation (Alcubierre / metric distortion style)
# Mass-energy required to warp a region of size R=10m over a distance of 1 ly
R_bubble = 10.0  # meters
# Typical Alcubierre metric energy estimate can be negative/positive but scale is roughly E ~ - (c^4 * R^2 * v^2) / (G) for high speeds
# For a generic metric distortion to cross 1 ly, scale is proportional to c^4 / G * spatial volume or distance
E_warp = (c**4) / G * R_bubble  # Minimal scale for a localized distortion

print(f"M_spaceship: {M_spaceship} kg")
print(f"E_linear: {E_linear:.3e} J")
print(f"E_warp: {E_warp:.3e} J")
