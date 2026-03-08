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



# ~~~~~ PARAMETERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Set FPS
total_sim_years = 10 # Simulation duration in years
anim_length_sec = 10 # Animation duration in sec
fps = 60 # Animation Framerate
physics_dt = SECONDS_PER_HOUR # Simulation time-step value in seconds
output_path = os.path.join(ROOT_DIR, 'Data/') # Save to Data folder

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def main():
    # Initialize bodies
    b_sun = Body('Sun', SUN_MASS, [0, 0, 0], [0, 0, 0])
    b_mercury = Body('Mercury', MERCURY_MASS, [MERCURY_ORBIT_R, 0, 0], [0, MERCURY_ORBIT_V, 0])
    b_venus = Body('Venus', VENUS_MASS, [VENUS_ORBIT_R, 0, 0], [0, VENUS_ORBIT_V, 0])
    b_earth = Body('Earth', EARTH_MASS, [EARTH_ORBIT_R, 0, 1e4], [0,EARTH_ORBIT_V, 0])
    b_mars = Body('Mars', MARS_MASS, [MARS_ORBIT_R, 0, -5e10], [0,MARS_ORBIT_V, 0])
    b_saturn = Body('Saturn', SATURN_MASS, [SATURN_ORBIT_R, 0, 0], [0, SATURN_ORBIT_V, 0])
    b_jupiter = Body('Jupiter', JUPITER_MASS, [JUPITER_ORBIT_R, 0, 1e5], [0, JUPITER_ORBIT_V, 0])
    b_uranus = Body('Uranus', URANUS_MASS, [URANUS_ORBIT_R, 0, 0], [0, URANUS_ORBIT_V, 0])
    b_neptune = Body('Neptune', NEPTUNE_MASS, [NEPTUNE_ORBIT_R, 0, 0], [0, NEPTUNE_ORBIT_V, 0])

    planet_names = ['Sun','Mercury','Venus,','Earth','Mars','Saturn','Jupiter','Uranus','Neptune']

    sim = Simulation()
    sim.add_body(b_sun)
    sim.add_body(b_mercury)
    sim.add_body(b_venus)
    sim.add_body(b_earth)
    sim.add_body(b_mars)
    sim.add_body(b_saturn)
    sim.add_body(b_jupiter)
    sim.add_body(b_uranus)
    sim.add_body(b_neptune)

    # Set body count
    nbodies = len(planet_names)

    # -- animation initialization --
    frames_to_save = anim_length_sec * fps
    total_sim_time_sec = total_sim_years*SECONDS_PER_YEAR
    time_per_frame_sec = total_sim_time_sec / frames_to_save
    steps_per_frame = int(time_per_frame_sec/ physics_dt)

    # Run the simulation and return the computed matrix to data
    data = runSimulation(sim,nbodies=nbodies,
                        nframes=frames_to_save,
                        dt=physics_dt,
                        steps_per_frame=steps_per_frame)


    # Create Data folder if not existing already
    os.makedirs(output_path, exist_ok=True)

    # Save the computation data (Optional for later playback without calculating again)
    # save_data_binary(data, 'solar_system', output_path)

    # UNCOMMENT TO RUN THE SIMULATION | REMOVE THE SAVE PARAMETER IF IT TAKES TOO LONG TO SAVE

    # run(data,
    #     planet_names,
    #     frame_time=physics_dt*steps_per_frame,
    #     fps=fps,
    #     save='solar_system.mp4'
    #     )

    # UNCOMMENT TO RUN THE SIMULATION SIDE BY SIDE

    run_sidebyside(data, labels=planet_names, frame_time=physics_dt*steps_per_frame, fps=fps, center=0, limtype='square', zoom=5, save='solar_system_sbs.mp4')




if __name__ == '__main__':
    main()