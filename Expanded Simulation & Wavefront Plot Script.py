import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTS & SIMULATION PARAMETERS ---
C = 299792458        # Speed of light (m/s)
G = 6.67430e-11      # Gravitational constant (m^3/kg*s^2)
MASS = 22 * 0.453592 # Hull Mass (~9.98 kg)
DISTANCE = 9.461e15  # 1 Light-Year (m)
R_BUBBLE = 10.0      # Distortion boundary radius (m)

print("--- REVISED PARAMETERS: ANTIMATTER & DARK ENERGY CRITERIA ---")
print("1. Physics Rule: Antimatter possesses normal, positive gravitational mass.")
print("2. Dynamic Offset: Dark Energy fields inject negative vacuum pressure.")

# --- PHYSICS CALCULATIONS ---
# Base Einstein field warp cost
E_warp_raw = (C**4 / G) * R_BUBBLE 

# Dark energy field density injection (Joules/m^3) to mitigate local vacuum curvature stress
dark_energy_density = 1.35e43  # Targeted negative pressure within warp bubble volume
bubble_volume = (4/3) * np.pi * (R_BUBBLE**3)
E_dark_energy_offset = dark_energy_density * bubble_volume

# Net energy required after negative pressure cancellation
E_net_warp = max(0.0, E_warp_raw - E_dark_energy_offset)

# --- TIME-EVOLVING WAVEFRONT SIMULATION & PLOT ---
time_steps = 5
space_points = 500
x = np.linspace(0, DISTANCE, space_points)
t_array = np.linspace(0, 1.0, time_steps) # Normalized time progression

plt.figure(figsize=(10, 6))

for i, t in enumerate(t_array):
    # Quadratic trajectory foundation combined with a moving wave packet
    wave_center = t * DISTANCE
    sigma = DISTANCE * 0.1 # Wave width parameter
    
    # Space-time metric wave profile blending quadratic boundaries with time-evolution
    quadratic_envelope = -4 / (DISTANCE**2) * x * (x - DISTANCE)
    wave_packet = np.exp(-((x - wave_center) ** 2) / (2 * sigma ** 2))
    spacetime_curvature = quadratic_envelope * wave_packet
    
    plt.plot(x / 9.461e15, spacetime_curvature, label=f'Time T + {t:.1f} yr')

plt.title("Spacetime Wave Profile Evolution Over Time (1 Light-Year Path)")
plt.xlabel("Distance (Light-Years)")
plt.ylabel("Metric Distortion Amplitude ($G_{\mu\nu}$)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()

print("\n--- METRIC ENERGY ANALYSIS SUMMARY ---")
print(f"Raw Einstein Field Wave Energy : {E_warp_raw:.6e} Joules")
print(f"Dark Energy Negative Pressure Offset: {E_dark_energy_offset:.6e} Joules")
print(f"Net Energy Required After Offset    : {E_net_warp:.6e} Joules")
