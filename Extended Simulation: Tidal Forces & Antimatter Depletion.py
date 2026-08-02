import numpy as np

# --- CONSTANTS & SYSTEM INPUTS ---
C = 299792458        # Speed of light (m/s)
G = 6.67430e-11      # Gravitational constant (m^3/kg*s^2)
MASS_SHIP = 22 * 0.453592 # Ship mass (~9.98 kg)
DISTANCE = 9.461e15  # 1 Light-Year (m)
R_BUBBLE = 10.0      # Distortion radius (m)
E_NET_WARP = 1.21e45 # Net warp energy from previous metric state
HULL_LENGTH = 2.0    # Length of the spaceship hull inside the bubble (m)

# 1. TIDAL FORCE ANALYSIS (RIEMANN CURVATURE GRADIENT)
# Tidal acceleration across the ship hull is proportional to d^2(Metric)/dx^2
# For a localized bubble, the structural stress depends on the change in curvature across the hull length.
curvature_gradient = E_NET_WARP / (R_BUBBLE**3)
tidal_acceleration = (G * curvature_gradient * HULL_LENGTH) / (C**2)
g_forces = tidal_acceleration / 9.81

# 2. ANTIMATTER THRUSTER DEPLETION RATE
# To maintain a straight line off the curved spacetime wavelengths, the thrusters must
# continuously balance residual metric shear. We assume a 0.001% residual drag coupling.
drag_efficiency_factor = 1e-5
total_propulsion_energy = E_NET_WARP * drag_efficiency_factor

# Total antimatter-matter fuel mass required via E = m*c^2 (Divided by 2 for pure antimatter fraction)
total_fuel_mass_kg = total_propulsion_energy / (C**2)
antimatter_fuel_kg = total_fuel_mass_kg / 2.0

# Depletion rate assuming a 1-year transit time in the target frame (31,536,000 seconds)
transit_time_sec = 365 * 24 * 3600
burn_rate_g_per_sec = (antimatter_fuel_kg * 1000) / transit_time_sec

print("--- INTERNAL TIDAL FORCE ANALYSIS ---")
print(f"Tidal Acceleration Across Hull: {tidal_acceleration:.3e} m/s^2")
print(f"Structural Load Factor        : {g_forces:.3e} Gs")
if g_forces > 10:
    print("WARNING: Tidal forces exceed human/structural limits. Internal gravity dampening required.")

print("\n--- ANTIMATTER PROPULSION & DEPLETION PROFILE ---")
print(f"Total Antimatter Fuel Needed  : {antimatter_fuel_kg:.3e} kg")
print(f"Continuous Fuel Burn Rate     : {burn_rate_g_per_sec:.6f} grams/second")
