# --- 5-YEAR ORBITAL DECAY MODEL ---
years_timeline = np.linspace(0, 5, 1000)
# Base decay rate of ~15 km per year modulated by the solar activity cycle
altitude_decay_profile = 400.0 - 15.0 * years_timeline - 5.0 * np.sin(2 * np.pi * years_timeline / 11)**2

print("\n--- THERMOSPHERIC DRAG METRICS ---")
print(f"Projected Altitude at Year 5: {altitude_decay_profile[-1]:.2f} km")
if altitude_decay_profile[-1] > 300:
    print("Orbital Status: Safe. Spacecraft remains well above reentry burn-up threshold.")
