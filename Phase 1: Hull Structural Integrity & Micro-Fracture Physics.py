import numpy as np

# --- STRUCTURAL CONSTANTS ---
V_COAST = 0.9 * 299792458  # 90% speed of light (m/s)
M_HYDROGEN = 1.673e-27      # Hydrogen mass (kg)
BYPASS_RATIO = 1e-5         # 0.001% leakage through the deflection shield
TOTAL_ATOMS_ENCOUNTERED = 2.158e27 # Equivalent to the 3.61 kg swept gas mass
COPPER_LAT_ENERGY = 3.5e-19 # Energy to induce a single lattice vacancy (Joules)

# Energy deposited per leakage atom
gamma = 1.0 / np.sqrt(1 - (V_COAST**2 / 299792458**2))
ke_per_atom = (gamma - 1) * M_HYDROGEN * (299792458**2)

# Total defects generated over 1 Light-Year
leaked_atoms = TOTAL_ATOMS_ENCOUNTERED * BYPASS_RATIO
total_lattice_vacancies = (leaked_atoms * ke_per_atom) / COPPER_LAT_ENERGY

print(f"Energy per Particle Strike: {ke_per_atom:.4e} Joules")
print(f"Micro-Fracture Vacancies  : {total_lattice_vacancies:.4e} atomic dislocations")
