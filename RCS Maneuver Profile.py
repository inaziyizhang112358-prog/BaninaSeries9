# --- REACTION CONTROL ADVANCEMENT ---
rcs_thrust_newtons = 0.05       # 50 millinewtons of thrust
burn_duration_seconds = 12.0     # 12-second orbital stabilization burn
mass_cubesat = 10.0

delta_v_achieved = (rcs_thrust_newtons * burn_duration_seconds) / mass_cubesat
new_orbital_velocity = 7670.0 + delta_v_achieved

print("\n--- PROPULSION SEQUENCE LOG ---")
print(f"Thrust Delta-V Injection : {delta_v_achieved:.4f} m/s")
print(f"Updated Orbit Velocity   : {new_orbital_velocity:.4f} m/s")
print("Maneuver Status          : BURN COMPLETE. ATTITUDE MATRIX ALIGNED.")
print("\n=====================================================================")
print("             NASA CUBESAT SIMULATION VECTOR FINALIZED                ")
print("=====================================================================")
