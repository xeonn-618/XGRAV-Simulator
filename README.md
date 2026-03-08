# N-Body Simulator

### XGRAV Module
Custom made python module for simulating and animating n-celestial bodies.

- `simulator.py` : Simulator class, maintains the universe and holds bodies. Calculates newtonian forces between each body in each step and updates each body. Runs the simulation and returns a matrix of the calculated data. Can be saved to run the animation later.

- `bodies.py` : Bodies class, holds the information of the body such as title, position vector, velocity vector and mass.

- `constants.py` : Holds universal constants, positions, velocities and masses of known bodies.

- `animate.py` : Runs the animation from the simulated data.
    - `run(data, labels, frame_time, fps=30, limtype='square', zoom=1.0, save='')` : Renders a single 3D animation of the simulation. Bodies are drawn as coloured scatter points with trailing orbital paths. The plot bounds are either kept square (equal on all axes, useful for near-circular orbits) or fit tightly to the data depending on `limtype`. `zoom` scales the bounds. Pass a filename to `save` to export the animation to the `Animations/` folder.
    - `run_sidebyside(data, labels, frame_time, fps=30, center=0, limtype='square', zoom=1.0, save='')` : Renders two 3D panels side-by-side. The left panel shows the full extent of the simulation, while the right panel is zoomed in by the `zoom` factor, both centred on the body at index `center`. The zoom level is displayed in the corner of the right panel. Both views track the chosen body throughout the animation. Like `run()`, passing a filename to `save` exports the result.
    - NOTE: Saving the animation may take some time, consider choosing shorter save durations and/or lower frame rate.

### Running a Simulation

The `Simulation` class from `simulator.py` manages the universe and advances it step by step.

**Setup & adding bodies:**
```python
from XGRAV.simulator import Simulation

sim = Simulation()
sim.add_body(earth)   # add as many Body objects as needed
sim.add_body(sun)
```

**Running — `runSimulation(sim, nbodies, nframes, dt, steps_per_frame)`:**

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `sim` | `Simulation` | — | The `Simulation` instance containing all bodies |
| `nbodies` | `int` | — | Number of bodies in the simulation |
| `nframes` | `int` | — | Number of frames to record (= length of the animation) |
| `dt` | `float` | s | Physics timestep;  smaller = more accurate |
| `steps_per_frame` | `int` | — | How often a frame is saved; calculations remain accurate. |

Returns a NumPy array of shape `(nframes, nbodies, 3)` containing the XYZ position of every body at every frame.

```python
from XGRAV.simulator import runSimulation

data = runSimulation(sim, nbodies=2, nframes=365, dt=3600, steps_per_frame=24)
# 8760 total steps (365 × 24), 1 frame saved every 24 steps, 1-hour timestep → ~1 simulated year
```

**Saving & loading data:**

| Function | Description |
|----------|-------------|
| `save_data_binary(data, filename, path='')` | Saves the position array to a `.npy` file for later playback |
| `load_data_binary(filepath)` | Loads a previously saved `.npy` file and returns the data array |

### Adding Bodies

Bodies are created using the `Body` class from `bodies.py`:

```python
Body(name, mass, pos_vec, vel_vec)
```

| Parameter | Type | Unit | Description |
|-----------|------|------|-------------|
| `name` | `str` | — | Label for the body (used in the animation legend) |
| `mass` | `float` | kg | Mass of the body |
| `pos_vec` | `[x, y, z]` | m | Initial position vector in 3D space |
| `vel_vec` | `[vx, vy, vz]` | m/s | Initial velocity vector in 3D space |

**Example:**
```python
from XGRAV.bodies import Body

earth = Body(
    name    = "Earth",
    mass    = 5.972e24,      # kg
    pos_vec = [1.496e11, 0, 0],   # m  (1 AU from origin)
    vel_vec = [0, 29_780, 0]      # m/s (orbital velocity)
)
```

Add bodies to the simulation by passing them to the `Simulator`.

### Examples

1) Solar System
2) Halley's Comet
3) Chaos System

### Benchmarks

Test the performance of the CPU on running the simulations. The algorithm scales $O(n^2)$ as verified in the benchmark results.

Time scales linearly with duration of simulation as evident in the benchmark.


