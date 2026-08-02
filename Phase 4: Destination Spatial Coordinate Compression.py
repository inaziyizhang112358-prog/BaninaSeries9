import numpy as np
import matplotlib.pyplot as plt

# Distance array approaching the destination point (last 10,000 meters)
x_approach = np.linspace(-10000, 0, 1000)

# The spatial metric component g_xx undergoes a severe spike as the wave uncurves
# We approximate the coordinate compression gradient at the sudden boundary exit
g_xx_compression = 1.0 + (1.21e45 / 1e45) * np.exp(-x_approach**2 / (2 * 1500**2))

plt.figure(figsize=(9, 5))
plt.plot(x_approach, g_xx_compression, color='darkred', linewidth=2, label="Spatial Metric Tensor ($g_{xx}$)")
plt.title("Forward Metric Compression Profile During Tunnel Exit Phase")
plt.xlabel("Distance to Target Destination (Meters)")
plt.ylabel("Compression Scale ($g_{xx}$ Factor)")
plt.grid(True, linestyle=":", alpha=0.5)
plt.axvline(x=0, color='black', linestyle='--', label="Decoupling Point")
plt.legend()
plt.show()
