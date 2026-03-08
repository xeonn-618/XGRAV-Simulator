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

# ~~~~~~~~~~~~~~~~~ Benchmark Parameters ~~~~~~~~~~~~~~~~~~~
years_list = [10,15,20,25,50,100,250,500,1000]  # The "work" values to test
cpu_times = []

# ~~~~~~~~~~~~~~~~~~ PARAMETERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
n_bodies = 3  # Keep 'n' constant
physics_dt = SECONDS_PER_DAY # sim time step
anim_length_sec = 5
video_fps = 30
output_path = os.path.join(ROOT_DIR, 'Benchmarks/Results/')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

frames_to_save = anim_length_sec * video_fps

# Setup a Constant Body Sim
sim = Simulation()
sim.add_body(Body('Cluster Core', 1000 * SUN_MASS, [0,0,0], [0,0,0]))
for i in range(n_bodies - 1):
    pos = (np.random.rand(3) - 0.5) * 50 * AU
    vel = (np.random.rand(3) - 0.5) * 5e3
    mass = np.random.uniform(JUPITER_MASS, SUN_MASS)
    sim.add_body(Body(f'Star-{i}', mass, pos, vel))

# Run the Benchmark Loop
for years in years_list:
    print(f"--- Benchmarking for {years} years ---")
    
    # Recalculate time parameters
    total_sim_years = years
    total_sim_time_sec = total_sim_years * SECONDS_PER_YEAR
    time_per_frame_sec = total_sim_time_sec / frames_to_save
    steps_per_frame = int(time_per_frame_sec / physics_dt)

    # Time 
    start_cpu = time.time()
    runSimulation(sim, n_bodies, frames_to_save, physics_dt, steps_per_frame)
    end_cpu = time.time()
    cpu_time = end_cpu - start_cpu
    cpu_times.append(cpu_time)
    print(f"CPU Time: {cpu_time:.2f} seconds")

# Plot the Results
plt.figure(figsize=(10, 6))
plt.plot(years_list, cpu_times, label='CPU (Single-Core)', marker='o', c='blue')
plt.xlabel('Total Simulation Time (Years)', fontsize=14)
plt.ylabel('Time Taken (seconds)', fontsize=14)
plt.title('CPU Time Scaling (Time vs. Workload)', fontsize=16)
plt.legend()
plt.grid(True, linestyle=':')
plt.savefig(f'{output_path}{years_list[-1]}_{n_bodies}_bodies.png')
print(f'Figure saved to',f'{output_path}{years_list[-1]}_{n_bodies}_bodies.png')
plt.show()
