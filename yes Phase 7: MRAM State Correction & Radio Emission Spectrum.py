import numpy as np
import matplotlib.pyplot as plt

# --- 1. MRAM ECC TRIANGULATION SIMULATION ---
# Simulate 100,000 memory cells subjected to intense gamma ionization shifts.
# We apply a triple-modular redundancy (TMR) voting logic to correct bit flips.
np.random.seed(42)
total_bits = 100000
radiation_error_rate = 0.05  # 5% raw bit-flip probability from gamma flux

# Generate three redundant memory banks
bank1 = np.zeros(total_bits, dtype=int)
bank2 = np.zeros(total_bits, dtype=int)
bank3 = np.zeros(total_bits, dtype=int)

# Simulate independent radiation strikes causing random bit flips (0 -> 1)
bank1[np.random.rand(total_bits) < radiation_error_rate] = 1
bank2[np.random.rand(total_bits) < radiation_error_rate] = 1
bank3[np.random.rand(total_bits) < radiation_error_rate] = 1

# TMR Voting Logic: if two or more banks agree the bit flipped, it registers an uncorrected error
corrupted_bits_unprotected = np.sum(bank1)
majority_vote = ((bank1 + bank2 + bank3) >= 2).astype(int)
uncorrected_errors = np.sum(majority_vote)

print("--- RECOVERY MATRIX & COMPUTATIONAL RECOVERY ---")
print(f"Unprotected Memory Corrupted Bits: {corrupted_bits_unprotected} / {total_bits}")
print(f"Post-TMR Hardened Corrected Errors: {uncorrected_errors} / {total_bits}")
print(f"Data Recovery Success Rate       : {((total_bits - uncorrected_errors)/total_bits)*100:.4f}%")

# --- 2. SYNCHROTRON RADIO EMISSION SPECTRUM ---
# As the plasma shield deflects the exit radiation, it sheds excess energy as a 
# radio-frequency signature. We map the intensity across the gigahertz spectrum.
frequencies_ghz = np.linspace(0.1, 100, 1000)
# Synchrotron emission power law curve peaked at critical frequency v_c
critical_frequency = 15.0  # GHz
intensity = (frequencies_ghz / critical_frequency)**(1/3) * np.exp(-frequencies_ghz / critical_frequency)

plt.figure(figsize=(9, 5))
plt.plot(frequencies_ghz, intensity, color='darkorange', linewidth=2, label="Synchrotron RF Flux")
plt.fill_between(frequencies_ghz, intensity, color='orange', alpha=0.2)
plt.title("Plasma Shield Synchrotron Radio Emission Spectrum During Deceleration")
plt.xlabel("Frequency (GHz)")
plt.ylabel("Relative Flux Density ($S_\nu$)")
plt.axvline(x=critical_frequency, color='blue', linestyle=':', label="Critical Peak Frequency")
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend()
plt.show()
