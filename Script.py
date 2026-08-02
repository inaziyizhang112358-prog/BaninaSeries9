import numpy as np

# --- CONSTANTS & SIMULATION PARAMETERS ---
C = 299792458        # Speed of light (m/s)
G = 6.67430e-11      # Gravitational constant (m^3/kg*s^2)
MASS = 22 * 0.453592 # 22 lbs converted to kg (~9.98 kg)
DISTANCE = 9.461e15  # 1 Light-Year in meters

print("--- NASA ISS/ORBITAL LAUNCH PROCEDURES ---")
procedures = [
    "1. Verify microgravity orientation and payload structural integrity.",
    "2. Clear orbit pathway via NASA Conjunction Assessment Risk Analysis (CARA).",
    "3. Command cold-gas RCS thrusters for attitude alignment to vector Alpha.",
    "4. Initiate secondary stage separation from orbital deployment platform.",
    "5. Confirm Go/No-Go window for main engine ignition sequence."
]
for step in procedures:
    print(step)

# --- ENERGY CALCULATIONS ---
# 1. Straight Line Relativistic Kinetic Energy at 0.9c
v = 0.9 * C
gamma = 1.0 / np.sqrt(1 - (v**2 / C**2))
E_linear = (gamma - 1) * MASS * (C**2)

# 2. Einstein Field Equations Metric Distortion (T00 Component Approximation)
# Curving space into a localized wavelength requires modifying the metric tensor G_uv.
# Energy density scales heavily with the spatial gradient: T_00 ~ (c^4 / 8*pi*G) * G_00
R_bubble = 10.0 # Metric perturbation boundary radius around the small craft
E_warp = (C**4 / G) * R_bubble 

# 3. Quadratic Trajectory Optimization
# Minimizing the peak distortion spike using a smooth parabolic metric amplitude
x_steps = np.linspace(0, DISTANCE, 1000)
# Quadratic curve mapping the optimal distortion shape: y = ax^2 + bx
a_opt = -4 / (DISTANCE**2) 
quadratic_wave_profile = a_opt * x_steps * (x_steps - DISTANCE)

print("\n--- TRIANGULATION & ENERGY DENSITY ANALYSIS ---")
print(f"Target Distance: {DISTANCE:.3e} meters (1.0 ly)")
print(f"Spaceship Mass: {MASS:.2f} kg")
print(f"Linear Trajectory Energy (0.9c kinetic): {E_linear:.6e} Joules")
print(f"Einstein Wave Metric Energy Required : {E_warp:.6e} Joules")
print(f"Quadratic Path Peak Curvature Amplitude: {np.max(quadratic_wave_profile):.4f}")
