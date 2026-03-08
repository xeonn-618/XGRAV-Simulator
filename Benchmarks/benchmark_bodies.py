import time
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))

# Set python directory to root project folder to import XGRAV
if ROOT_DIR not in sys.path: 
    sys.path.append(ROOT_DIR)

from XGRAV.bodies import Body
from XGRAV.simulator import Simulation, runSimulation, save_data_binary
from XGRAV.constants import *
from XGRAV.animate import run, run_sidebyside

# ~~~~~~~~~~~~ Define Benchmark Parameters ~~~~~~~~~~~~~
n = 200
n_bodies_list = [x for x in range(1,n,5)]  # The "n" values to test
cpu_times = []

# ~~~~~~~~ PARAMETERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~
physics_dt = SECONDS_PER_DAY
total_sim_years = 1 # Short Duration to run it fast
anim_length_sec = 5  # Just a few frames
video_fps = 30 
output_path = os.path.join(ROOT_DIR, 'Benchmarks/Results/')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Init Animation
frames_to_save = anim_length_sec * video_fps
total_sim_time_sec = total_sim_years * SECONDS_PER_YEAR
time_per_frame_sec = total_sim_time_sec / frames_to_save
steps_per_frame = int(time_per_frame_sec / physics_dt)

# Run the Benchmark Loop
for n in n_bodies_list:
    print(f"--- Benchmarking for n = {n} bodies ---")
    
    # Init Simulation for n bodies
    sim = Simulation()
    sim.add_body(Body('Cluster Core', 1000 * SUN_MASS, [0,0,0], [0,0,0]))
    for i in range(n - 1): # Add (n-1) random stars
        pos = (np.random.rand(3) - 0.5) * 50 * AU
        vel = (np.random.rand(3) - 0.5) * 5e3
        mass = np.random.uniform(JUPITER_MASS, SUN_MASS)
        sim.add_body(Body(f'Star-{i}', mass, pos, vel))

    # Time 
    start_cpu = time.time()
    runSimulation(sim, n, frames_to_save, physics_dt, steps_per_frame)
    end_cpu = time.time()
    cpu_time = end_cpu - start_cpu
    cpu_times.append(cpu_time)
    print(f"CPU Time: {cpu_time:.2f} seconds")

# --- 4. Plot the Results ---
plt.figure(figsize=(10, 6))
plt.plot(n_bodies_list, cpu_times, label='CPU (Single-Core)', marker='o', c='blue')
plt.xlabel('Number of Bodies (n)', fontsize=14)
plt.ylabel('Time Taken (seconds)', fontsize=14)
plt.title('CPU Time Scaling (Time vs. N-Bodies)', fontsize=16)
plt.legend()
plt.grid(True, linestyle=':')
plt.savefig(f'{output_path}{len(n_bodies_list)}_bodies.png')
print(f'Figure saved to',f'{output_path}/{len(n_bodies_list)}_bodies.png')
plt.show()