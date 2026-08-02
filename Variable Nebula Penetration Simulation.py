import numpy as np
import matplotlib.pyplot as plt

# Re-establishing structural arrays for path density
distance = 9.461e15 # 1 Light-Year
steps = 1000
x = np.linspace(0, distance, steps)

# Nebula gas density map (atoms per cubic meter) showing peak cloud boundary penetration
nebula_profile = 1e6 + 1e9 * np.sin(np.pi * x / distance)**2

plt.figure(figsize=(9, 5))
plt.plot(x / 9.461e15, nebula_profile, color='purple', linewidth=2, label="ISM Gas Density")
plt.title("Interstellar Gas Density Along 1 Light-Year Tunnel Vector")
plt.xlabel("Distance Travelled (Light-Years)")
plt.ylabel("Particle Concentration ($\text{atoms/m}^3$)")
plt.grid(True, linestyle=":", alpha=0.5)
plt.fill_between(x / 9.461e15, nebula_profile, color='purple', alpha=0.15)
plt.legend()
plt.show()
