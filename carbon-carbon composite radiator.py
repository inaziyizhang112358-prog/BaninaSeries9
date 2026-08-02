import numpy as np

# --- CONSTANTS & FIXED PARAMETERS ---
C = 299792458               # Speed of light (m/s)
STEFAN_BOLTZMANN = 5.670374e-8
M_HYDROGEN = 1.6737236e-27  # Mass of a single hydrogen atom (kg)

# Inputs from previous optimization
R_BUBBLE = 12.04            # Optimized bubble radius (m)
DISTANCE = 9.461e15         # 1 Light-Year (m)
EXHAUST_POWER = 3.993e29    # Exhaust thermal output (Watts)
TRANSIT_TIME = 365 * 24 * 3600

print("--- ADVANCED SUBSYSTEM UPGRADES ---")
print("1. Radiator: Carbon-Carbon Composite Matrix (Max structural temp ~3300K).")
print("2. Deflection: Lorentz-Force Ionization Shield for interstellar media.")

# --- 1. RADIATOR SURFACE AREA OPTIMIZATION ---
# Standard carbon-carbon emissivity is roughly 0.85
emissivity_carbon = 0.85
max_safe_temp = 3200.0  # Kelvin (with a safety buffer below sublimation)

# Calculate the minimum surface area needed to dissipate the exhaust power safely
min_radiator_area = EXHAUST_POWER / (emissivity_carbon * STEFAN_BOLTZMANN * (max_safe_temp**4))

# --- 2. INTERSTELLAR GAS CLOUD DEFLECTION ---
# Average density of interstellar medium (ISM) is roughly 1 atom per cubic centimeter
ism_density_atoms_m3 = 1e6 
total_volume_swept = np.pi * (R_BUBBLE**2) * DISTANCE
total_hydrogen_atoms = ism_density_atoms_m3 * total_volume_swept
total_gas_mass_kg = total_hydrogen_atoms * M_HYDROGEN

# Kinetic energy required to ionize and deflect this gas mass outward at a vector perpendicular to travel
deflection_velocity = 50000.0  # m/s away from hull vector
E_deflection_fields = 0.5 * total_gas_mass_kg * (deflection_velocity**2)
deflection_power_watts = E_deflection_fields / TRANSIT_TIME

print("\n--- THERMAL MANAGEMENT ANALYTICS ---")
print(f"Required Radiator Surface Area : {min_radiator_area:.3e} square meters")
print(f"Material Melting / Fail Limit  : {max_safe_temp} K")
if min_radiator_area > 1e6:
    print("CRITICAL: Radiator size exceeds structural feasibility. Secondary cooling loop required.")

print("\n--- INTERSTELLAR SHIELDING CALCULATIONS ---")
print(f"Total ISM Gas Mass Encountered : {total_gas_mass_kg:.6f} kg")
print(f"Active Deflection Field Energy : {E_deflection_fields:.6e} Joules")
print(f"Continuous Shield Power Draw   : {deflection_power_watts:.6f} Watts")
