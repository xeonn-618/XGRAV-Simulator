import numpy as np
import time

class Simulation():
    def __init__(self):
        self.bodies = []
        self.time = 0.0

    def add_body(self, body):
        '''Adds a body to the simulation'''
        self.bodies.append(body)
    
    def run_step(self, dt):

        # Calculatae force on each body due to other bodies
        for body_a in self.bodies:
            for body_b in self.bodies:

                # Dont compare a body by itself!
                if body_a == body_b: continue
                
                # Calculate force on body A due to body B
                force_vec = body_a.force_from(body_b)

                # Add force vector to body A's state
                body_a.force += force_vec


        for body in self.bodies:
            body.updateSelf(dt)

        # Update time of simulation
        # print(f"Simulation time {self.time}") # debug
        self.time += dt


def runSimulation(sim, nbodies, nframes, dt, steps_per_frame):

    # Create a zero array of required size to store positon data for each body and each frame
    data = np.zeros((nframes, nbodies, 3), dtype=np.float64)

    total_steps = nframes * steps_per_frame

    time_start = time.time()
    print(f"Running simulation for {total_steps} total steps...")
    print(f"Performing {nbodies*(nbodies-1)*total_steps} calculations...")

    data_index = 0

    # Run the simulation frame by frame for each step
    # but only save every 'steps_per_frame' steps
    for step in range(total_steps):

        # Check if this is the frame we are supposed to save
        if step % steps_per_frame == 0:
            # Get current position of each body
            current_pos = np.array([body.pos for body in sim.bodies])
            data[data_index] = current_pos
            data_index += 1

        # Advance the step forward
        sim.run_step(dt)
    
    time_stop = time.time()
    print(f"Finished simulation in {time_stop-time_start:.2f} seconds")
    return data

def save_data_binary(data, filename, path=''):
    np.save(path+filename, data)
    print(f"File succesfully saved to {path+filename}")

def load_data_binary(filepath):
    data = np.load(filepath)
    return data
