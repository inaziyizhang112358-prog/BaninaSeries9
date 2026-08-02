import numpy as np
import matplotlib.pyplot as plt

# --- 1. DETECTING EXOPLANET CANDIDATES (SENSING ARRAYS) ---
# Simulate raw infrared transit photodiode voltages over a 48-hour scanning window.
# We look for a dips in stellar intensity corresponding to orbiting planets.
scan_hours = np.linspace(0, 48, 2000)
base_flux = 1.0 + np.random.normal(0, 0.0002, len(scan_hours))  # Sensor noise floor

# Simulate a planet transiting the star between hours 18 and 26
transit_window = (scan_hours >= 18) & (scan_hours <= 26)
base_flux[transit_window] -= 0.015  # 1.5% drop in starlight intensity

# --- 2. LASER-TELEMETRY PROPAGATION BACK TO EARTH ---
# The laser must cross exactly 1 light-year. We calculate beam divergence over this distance.
# Wave optics formula for beam diameter: D_final = D_initial + 2.44 * (wavelength * distance / D_initial)
wavelength = 1550e-9      # 1550 nm near-infrared laser (m)
distance_ly = 9.461e15    # 1 Light-Year (m)
d_aperture = 0.5          # Initial laser optics telescope diameter (m)

d_final = d_aperture + 2.44 * (wavelength * distance_ly / d_aperture)
beam_area_earth = np.pi * (d_final / 2)**2

# Link Budget: Calculate received power on Earth assuming a 100-Watt transmitter and a 10m receiver dish
p_transmit = 100.0        # Watts
r_earth_dish = 5.0        # 10m diameter telescope radius on Earth (m)
area_earth_dish = np.pi * (r_earth_dish**2)

p_received = p_transmit * (area_earth_dish / beam_area_earth)

print("--- EXOPLANET SENSOR SCAN MATRIX ---")
print(f"Mean Stellar Flux: {np.mean(base_flux):.4f}")
print(f"Maximum Target Transit Dip: {np.min(base_flux) - 1.0:.2%}")
print("Status: Planet candidate identified. Transit profile logged.")

print("\n--- DEEP-SPACE TELEMETRY LINK BUDGET ---")
print(f"Initial Laser Beam Diameter : {d_aperture} meters")
print(f"Beam Spot Diameter at Earth : {d_final / 1e3:.2f} kilometers")
print(f"Total Beam Area at Earth    : {beam_area_earth:.3e} square meters")
print(f"Received Signal Power       : {p_received:.6e} Watts")
print(f"Time-of-Flight to Earth     : 1.00 Years (365.25 days)")

# Plotting the exoplanet transit detection curve
plt.figure(figsize=(9, 5))
plt.plot(scan_hours, base_flux, color='navy', alpha=0.7, label="Stellar Flux Signature")
plt.title("Automated Destination Survey: Exoplanet Transit Detection")
plt.xlabel("Scanning Time Duration (Hours)")
plt.ylabel("Normalized Light Intensity")
plt.axvspan(18, 26, color='green', alpha=0.1, label="Planet Transit Window")
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend()
plt.show()
