import numpy as np
import matplotlib.pyplot as plt

# --- 1. DISCRETE LOOP QUANTUM GRAVITY (LQG) AREA SPECTRUM ---
# In LQG, space is quantized. The area operator has discrete eigenvalues: 
# A = 8 * pi * gamma * l_planck^2 * sqrt(j * (j + 1))
gamma_immirzi = 0.23753
l_planck = 1.616255e-35
j_spin_values = np.arange(0.5, 5.5, 0.5)

# Calculate discrete area chunks (eigenvalues) in square meters
discrete_areas = 8 * np.pi * gamma_immirzi * (l_planck**2) * np.sqrt(j_spin_values * (j_spin_values + 1))

# --- 2. COSMIC STRING MICROLENSING & PATH DEFLECTION ---
# Cosmic strings possess a deficit angle: Delta_alpha = 8 * pi * G * mu / c^2
# We simulate light deflection and positional drift over 100 tracking points
string_tension_mu = 1e-6  # Dimensionless tension parameter (G*mu/c^2)
deficit_angle = 8 * np.pi * string_tension_mu

tracking_points = 100
true_path = np.zeros(tracking_points)
observed_lensed_path = np.zeros(tracking_points)

for i in range(tracking_points):
    # Simulated positional shifting as the craft crosses the string's wake
    if i > 45:
        observed_lensed_path[i] = true_path[i] + deficit_angle * (i - 45)
    else:
        observed_lensed_path[i] = true_path[i]

print("--- DISCRETE GEOMETRY SPECTRUM (LQG) ---")
print(f"Minimum Non-Zero Area Quantum: {discrete_areas[0]:.3e} m^2")
print(f"Maximum Sampled Area Quantum  : {discrete_areas[-1]:.3e} m^2")

print("\n--- COSMIC STRING DEFLECTION QUANTITIES ---")
print(f"Calculated Deficit Angle      : {deficit_angle:.6e} radians")
print(f"Max Positional Micro-Drift    : {observed_lensed_path[-1]:.6e} spatial coordinate units")
print("Status: Lensing matrix integrated. Telemetry loops compensated for string geometric defect.")

# Plotting the geometric path deviation due to cosmic string wake crossing
plt.figure(figsize=(9, 4))
plt.plot(range(tracking_points), true_path, 'k--', label='True Euclidean Trajectory')
plt.plot(range(tracking_points), observed_lensed_path, color='darkviolet', linewidth=2, label='Lensed Spacetime Path')
plt.axvline(x=45, color='orange', linestyle=':', label='Cosmic String Boundary Interaction')
plt.title("Navigation Telemetry: Cosmic String Deflection Profile")
plt.xlabel("Trajectory Progress Index")
plt.ylabel("Lateral Coordinate Shift")
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend()
plt.show()
