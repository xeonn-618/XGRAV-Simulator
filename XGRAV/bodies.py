import numpy as np
from XGRAV.constants import G

class Body():
    def __init__(self, name, mass, pos_vec, vel_vec):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos_vec, dtype=np.float64)
        self.vel = np.array(vel_vec, dtype=np.float64)
        self.force = np.zeros(3, dtype=np.float64) # set force to 0
    
    def force_from(self,B):
        '''Calculatae the force on body self from body B'''
        r_vec = B.pos - self.pos
        
        # add an epsilon value to prevent division by zerp
        epsilon = 1e-6 
        r_mag = np.linalg.norm(r_vec) + epsilon

        r_cap = r_vec/r_mag

        force_mag = G*self.mass*B.mass/r_mag**2
        
        force_vec = force_mag * r_cap

        return force_vec
    
    def updateSelf(self, dt):

        # calculate acceleration
        acceleration = self.force / self.mass

        # update velocity
        self.vel += acceleration * dt

        # update position
        self.pos += self.vel * dt

        # reset force to 0 for next step
        self.force = np.zeros(3, dtype=np.float64)