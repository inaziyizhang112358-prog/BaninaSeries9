import numpy as np

transit_distance = 9.461e15 # meters
v_relative = 0.9 * 299792458

# Chronological calculations
external_duration_seconds = transit_distance / v_relative
internal_proper_seconds = external_duration_seconds * np.sqrt(1 - 0.9**2)

print(f"External Station Time Elapsed : {external_duration_seconds / (3600*24*365):.4f} Years")
print(f"Internal Craft Clock Elapsed  : {internal_proper_seconds / (3600*24*365):.4f} Years")
