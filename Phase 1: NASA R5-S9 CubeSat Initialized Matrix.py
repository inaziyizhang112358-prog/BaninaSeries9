import numpy as np

# --- CUBESAT CONSTANTS & SYSTEM INPUTS ---
C = 299792458
MASS_CUBESAT = 10.0  # 22 lbs scaled to exactly 10 kg (~6U CubeSat framework)
LOW_EARTH_ORBIT_ALT = 400000  # 400 km orbital altitude (meters)
ORBITAL_VELOCITY = 7670.0      # Standard LEO orbital velocity (m/s)

# --- FLIGHT CHECKOUT DATA SYSTEMS ---
print("--- NASA R5-S9 AUTONOMOUS CUBESAT PROTOCOLS ---")
telemetry_status = {
    "Battery Bus Voltage (V)": 12.1,
    "Optical Payload Temp (K)": 291.5,
    "ADCS Magnetic Torquers ": "STABLE / LOCKED",
    "RCS Cold-Gas Pressure  ": "OPTIMAL"
}
for key, value in telemetry_status.items():
    print(f"  {key}: {value}")

# --- ORBITAL RECONNAISSANCE PROJECTION ---
# Calculate the kinetic energy of a 22-lb satellite cruising in Low Earth Orbit
E_kinetic_leo = 0.5 * MASS_CUBESAT * (ORBITAL_VELOCITY**2)

print("\n--- ORBITAL BASELINE READOUT ---")
print(f"Deployment Classification: 6U Nanosatellite Profile")
print(f"Operational Mass Baseline: {MASS_CUBESAT:.2f} kg")
print(f"Standard LEO Kinetic Energy: {E_kinetic_leo:.6e} Joules")
