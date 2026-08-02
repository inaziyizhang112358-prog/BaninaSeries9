import numpy as np

# --- CONSTANTS & SYSTEM INPUTS ---
C = 299792458        # Speed of light (m/s)
G = 6.67430e-11      # Gravitational constant (m^3/kg*s^2)
M_SHIP = 22 * 0.453592  # Hull mass (~9.98 kg)
DISTANCE = 9.461e15  # 1 Light-Year (m)
STEFAN_BOLTZMANN = 5.670374e-8

# --- STOCHASTIC RADIUS OPTIMIZATION (0.9 STD DEV RISK) ---
# Sample possible bubble radii centered around 12 meters with 2m uncertainty
r_samples = np.random.normal(loc=12.0, scale=2.0, size=10000)
# Enforce a 0.9 standard deviation safety margin against high-risk compaction
R_opt = np.percentile(r_samples, 100 - (0.9 * 34.1)) 

# --- ENERGY AND COLLAPSE VERIFICATION ---
# Raw metric warping energy scale
E_warp = (C**4 / G) * R_opt 
# Mass equivalent of the warp field energy to check for black hole conditions
M_field = E_warp / (C**2)
R_schwarzschild = (2 * G * M_field) / (C**2)

# Safety Check: The physical radius R must exceed the Schwarzschild radius to prevent black holes
black_hole_risk = R_schwarzschild >= R_opt
metric_stability_factor = R_opt / max(R_schwarzschild, 1e-9)

# --- 1. INTERNAL GRAVITY DAMPENER CALCULATIONS ---
# Dampeners neutralize the local Riemann tidal forces across a 2-meter hull
hull_length = 2.0
tidal_accel = (G * E_warp * hull_length) / (R_opt**3 * C**2)
g_forces = tidal_accel / 9.81
# Energy required to generate a localized counter-gravitational field inside the hull
E_dampeners = 0.5 * M_SHIP * (tidal_accel * hull_length)

# --- 2. THERMAL RADIATION SIGNATURE FROM EXHAUST ---
# Antimatter consumption scales up to power the internal structural dampeners
drag_efficiency = 1e-5
E_propulsion = (E_warp + E_dampeners) * drag_efficiency
m_fuel_total = E_propulsion / (C**2)
transit_time = 365 * 24 * 3600
burn_rate_kg_s = m_fuel_total / transit_time

# Radiated thermal exhaust power from the antimatter annihilation nozzle
exhaust_thermal_power_watts = E_propulsion / transit_time
# Temperature calculation assuming a radiator shield area surface of 150 m^2
radiator_area = 150.0
exhaust_temp_kelvin = (exhaust_thermal_power_watts / (STEFAN_BOLTZMANN * radiator_area))**(1/4)

print("--- STOCHASTIC OPTIMIZATION SUMMARY (0.9 SIGMA RISK) ---")
print(f"Optimized Bubble Radius (R): {R_opt:.4f} meters")
print(f"Field Schwarzschild Radius : {R_schwarzschild:.4f} meters")
print(f"Black Hole Formation Risk  : {'CRITICAL FAILURE' if black_hole_risk else 'SAFE / NO COLLAPSE'}")
print(f"Metric Stability Margin    : {metric_stability_factor:.2f}x above event horizon threshold")

print("\n--- SYSTEM ENERGY REQUIREMENTS ---")
print(f"Total Spacetime Warp Energy: {E_warp:.6e} Joules")
print(f"Gravity Dampener Energy    : {E_dampeners:.6e} Joules")
print(f"Net Mission Energy Budget  : {E_warp + E_dampeners:.6e} Joules")

print("\n--- EXHAUST & THERMAL SIGNATURE ---")
print(f"Antimatter Burn Rate       : {burn_rate_kg_s * 1000:.6f} grams/second")
print(f"Exhaust Thermal Output     : {exhaust_thermal_power_watts:.3e} Watts")
print(f"Radiator Temperature       : {exhaust_temp_kelvin:.2f} Kelvin")
