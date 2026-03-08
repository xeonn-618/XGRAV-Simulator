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
total_sim_years = 15 # Simulation duration
anim_length_sec = 15 # Saved Animation duration in sec
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    # Define the bodies
    b_star = Body('Red Giant', 2 * SUN_MASS, 
                [0, 0, 0], 
                [0, 0, 0])


    b_hot_jupiter = Body('Inferno', JUPITER_MASS, 
                        [0.5*AU, 0, 0.2*AU],       
                        [0, 6.0e4, 0.5e4])        


    b_gas_giant = Body('Goliath', 8 * JUPITER_MASS, 
                    [10*AU, 5*AU, 0],          
                    [-0.5e4, 1.5e4, -0.2e4])   


    b_rogue = Body('Rogue', 3 * EARTH_MASS, 
                [0, 15*AU, 20*AU],        
                [0, -1.5e4, -2.0e4])      

    # Create the sim and body objects
    sim = Simulation()
    sim.add_body(b_star)
    sim.add_body(b_hot_jupiter)
    sim.add_body(b_gas_giant)
    sim.add_body(b_rogue)

    nbodies = 4
    bodies = [b_star, b_hot_jupiter, b_gas_giant, b_rogue]
    body_names = []
    for b in bodies:
        body_names.append(b.name)

    # Init Animation
    frames_to_save = anim_length_sec * fps
    total_sim_time_sec = total_sim_years*SECONDS_PER_YEAR
    time_per_frame_sec = total_sim_time_sec / frames_to_save
    steps_per_frame = int(time_per_frame_sec/ physics_dt)

    # Run the simulationa and return the computed matrix
    data = runSimulation(sim,nbodies=nbodies,nframes=frames_to_save,
                        dt=physics_dt, steps_per_frame=steps_per_frame)

    run_sidebyside(data=data, labels=body_names, center=0, fps=fps,frame_time=physics_dt*steps_per_frame,zoom=2,save='chaos_sbs.mp4',)

if __name__ == '__main__':
    main()