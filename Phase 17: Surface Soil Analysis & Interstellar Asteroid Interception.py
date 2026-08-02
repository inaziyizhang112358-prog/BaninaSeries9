import numpy as np
import matplotlib.pyplot as plt

# --- 1. MICRO-LANDER SURFACE SOIL SPECTROMETRY ---
# X-ray fluorescence simulation of surface soil samples to determine chemical abundance.
elements = ['Silicon', 'Iron', 'Magnesium', 'Calcium', 'Carbon', 'Sulfur', 'Other Oxide']
abundances_percent = [42.1, 18.4, 15.2, 10.5, 6.8, 4.1, 2.9]

# --- 2. INTERSTELLAR ASTEROID INTERCEPTION TRAJECTORY ---
# A high-eccentricity hyperbolic interloper enters the inner system at 45,000 m/s.
# We map the optimal flyby distance relative to interceptor sensor ranges.
closest_approach_au = np.linspace(0.1, 5.0, 500)
# Signal-to-noise ratio (SNR) decreases via the inverse square law of distance: SNR ~ 1 / R^2
sensor_wavelength = 850e-9 # Near IR tracking laser
target_albedo = 0.04       # Low-reflectivity dark carbonaceous asteroid
snr_profile = (150.0 / closest_approach_au**2) + np.random.normal(0, 0.5, len(closest_approach_au))

print("--- EXOPLANET GEOLOGICAL PROFILE ---")
for el, pct in zip(elements, abundances_percent):
    print(f" - {el:<15}: {pct:>5.1f}% abundance")
print("Status: Soil mineral matrix confirms silicates and heavy iron oxides. High basaltic match.")

print("\n--- INTERSTELLAR FLYBY INTERCEPTION MATRIX ---")
optimal_idx = np.where(snr_profile > 20.0)[0][-1]
print(f"Asteroid Entry Velocity   : 45,000.00 m/s")
print(f"Optimal Sensor Tracking Closeness: {closest_approach_au[optimal_idx]:.2f} AU")
print(f"Peak Data Transfer SNR Max       : {np.max(snr_profile):.2f}")
print("Status: Flyby telemetry vectors locked. Main observer chassis secondary instruments primed.")

# Plotting the Interception Sensor Signal Degradation
plt.figure(figsize=(9, 5))
plt.plot(closest_approach_au, snr_profile, color='crimson', label='Optical Tracking SNR')
plt.axhline(y=20, color='darkgray', linestyle='--', label='Minimum Data Sync Threshold (20 dB)')
plt.title("Interstellar Asteroid Intercept: Optical Tracker Signal Performance")
plt.xlabel("Closest Approach Distance (Astronomical Units)")
plt.ylabel("Signal-to-Noise Ratio (dB)")
plt.xlim(0.1, 4.0)
plt.ylim(0, 160)
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend()
plt.show()
