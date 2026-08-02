import numpy as np
import matplotlib.pyplot as plt

# --- 1. AUTOMATED PLANETARY ORBITAL INSERTION (DELTA-V) ---
# Parameters for the discovered exoplanet
G = 6.67430e-11
M_PLANET = 5.972e24      # Earth-mass analog (kg)
R_PLANET = 6371000       # Planet radius (m)
ALTITUDE_TARGET = 400000 # Target orbit altitude (400 km)

R_ORBIT = R_PLANET + ALTITUDE_TARGET
V_APPROACH = 25000.0     # Hyperbolic approach velocity relative to planet (m/s)

# Calculate required insertion burn (Delta-V) to enter a circular orbit
v_circular = np.sqrt((G * M_PLANET) / R_ORBIT)
v_perigee = np.sqrt(V_APPROACH**2 + (2 * G * M_PLANET / R_ORBIT))
delta_v_burn = v_perigee - v_circular

# --- 2. SOLAR CELL ARRAY DEPLOYMENT MATRIX ---
# Deploying a 10x10 modular solar cell panel matrix to face the new star.
# We map the structural cell efficiency profile across the grid array.
grid_size = 10
np.random.seed(101)
# Base cell efficiency centered at 28% with slight manufacturing/transit variances
solar_grid_efficiency = np.random.normal(loc=0.28, scale=0.01, size=(grid_size, grid_size))

print("--- PLANETARY CAPTURE MANEUVER ---")
print(f"Hyperbolic Velocity on Approach : {V_APPROACH:.2f} m/s")
print(f"Target Stable Orbit Velocity    : {v_circular:.2f} m/s")
print(f"Required Retro-Fire Burn Delta-V: {delta_v_burn:.2f} m/s")
print("Status: Orbital insertion engine burn executed successfully. Craft captured.")

print("\n--- SOLAR ARRAY INVENTORY ---")
print(f"Total Deployed Solar Elements  : {grid_size * grid_size} modules")
print(f"Average Matrix Efficiency Component: {np.mean(solar_grid_efficiency)*100:.2f}%")

# Visualize the deployed solar grid structural health map
plt.figure(figsize=(7, 6))
plt.imshow(solar_grid_efficiency * 100, cmap='YlOrRd', interpolation='nearest')
plt.colorbar(label='Module Conversion Efficiency (%)')
plt.title("Solar Cell Grid Deployment & Health Topology")
plt.xlabel("X-Axis Module Index")
plt.ylabel("Y-Axis Module Index")
plt.show()
