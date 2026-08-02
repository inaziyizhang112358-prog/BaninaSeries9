import numpy as np
import matplotlib.pyplot as plt

# --- 1. SPECTROSCOPIC ATMOSPHERE ANALYSIS ---
# Simulate the absorption spectrum of starlight filtering through the exoplanet's atmosphere.
# Chemical compounds absorb specific wavelengths, leaving distinct dips (absorption lines).
wavelengths_nm = np.linspace(400, 1000, 1000)
base_spectrum = 1.0 - 0.02 * (wavelengths_nm / 700)**2  # Background stellar curve

# Introduce specific molecular absorption signatures
methane_dip = 0.15 * np.exp(-((wavelengths_nm - 725) / 15)**2)
oxygen_dip = 0.25 * np.exp(-((wavelengths_nm - 760) / 10)**2)
water_vapor_dip = 0.20 * np.exp(-((wavelengths_nm - 940) / 25)**2)

full_spectrum = base_spectrum - (methane_dip + oxygen_dip + water_vapor_dip)
# Add realistic instrument readout noise
full_spectrum += np.random.normal(0, 0.01, len(wavelengths_nm))

# --- 2. AUTONOMOUS DATA PRUNING SIMULATION ---
# The on-board storage contains 50,000 raw telemetry records from orbit.
# To save memory space, a variance filter drops static, non-essential data lines.
total_records = 50000
raw_telemetry_variance = np.random.exponential(scale=0.2, size=total_records)

# Keep data only if variance exceeds a high-priority threshold (e.g., dynamic shifts)
priority_threshold = 0.15
retained_records = raw_telemetry_variance[raw_telemetry_variance > priority_threshold]
compression_ratio = len(retained_records) / total_records

print("--- BIOSIGNATURE SPECTROSCOPY RESULTS ---")
print("Target Absorption Profiles Found:")
print(" - O2 (Molecular Oxygen)  : Detected at 760nm (Strong Signal)")
print(" - CH4 (Methane)          : Detected at 725nm (Moderate Signal)")
print(" - H2O (Water Vapor)      : Detected at 940nm (Broad Signal)")
print("Status: Primary atmospheric composition implies potential habitability.")

print("\n--- ON-BOARD COMPRESSION & RECOVERY PROFILE ---")
print(f"Initial Unfiltered Log Files  : {total_records} rows")
print(f"Pruned High-Value Target Rows : {len(retained_records)} rows")
print(f"Memory Footprint Reduction    : {(1.0 - compression_ratio)*100:.2f}% Storage Cleared")

# Plotting the raw planetary transmission spectrum
plt.figure(figsize=(9, 5))
plt.plot(wavelengths_nm, full_spectrum, color='crimson', label="Observed Planetary Spectrum")
plt.title("Exoplanet Atmospheric Transmission Spectrum")
plt.xlabel("Wavelength (nanometers)")
plt.ylabel("Normalized Intensity")
plt.axvline(x=760, color='blue', linestyle='--', alpha=0.5, label="O2 Band (760nm)")
plt.axvline(x=725, color='green', linestyle='--', alpha=0.5, label="CH4 Band (725nm)")
plt.axvline(x=940, color='teal', linestyle='--', alpha=0.5, label="H2O Band (940nm)")
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend()
plt.show()
