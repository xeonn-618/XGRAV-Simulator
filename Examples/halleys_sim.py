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

# ~~~~~~~~ PARAMETERS ~~~~~~~~~~~~
physics_dt = SECONDS_PER_HOUR # Time Step Interval for Simulation Calculation
fps = 30 # Frame rate of saved animation
total_sim_years = 80 # Simulation duration
anim_length_sec = 15 # Saved Animation duration in sec
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    # Create simulation object 
    sim = Simulation()

    # Create bodies
    sun = Body('Sun', SUN_MASS, [0,0,0], [0,0,0])
    halley = Body("Halley's Comet", HALLEY_MASS, [HALLEY_APHELION_R,0,0], [0,HALLEY_APHELION_V,0])

    bodies = [sun,halley]
    body_names = []
    for b in bodies:
        body_names.append(b.name)
        sim.add_body(b)

    # Animation initilization 
    frames_to_save = anim_length_sec * fps
    total_sim_time_sec = total_sim_years*SECONDS_PER_YEAR
    time_per_frame_sec = total_sim_time_sec / frames_to_save
    steps_per_frame = int(time_per_frame_sec/ physics_dt)


    data = runSimulation(sim, len(bodies), nframes=frames_to_save, dt=physics_dt, steps_per_frame=steps_per_frame)

    # RUN SINGLE WINDOW PLAYBACK
    # run(data=data, labels=body_names, fps=fps,frame_time=physics_dt*steps_per_frame,zoom=1,save='halleys.mp4')

    # RUN SIDE BY SIDE PLAYBACK
    run_sidebyside(data=data, labels=body_names, center=1, fps=fps,frame_time=physics_dt*steps_per_frame,zoom=5,save='halleys_sbs.mp4',)

if __name__ == '__main__':
    main()