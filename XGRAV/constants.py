# XGRAV/constants.py
# This file contains all physical, temporal, and astronomical constants
# for the XGRAV simulation package.

# All units are in the SI system:
# Mass: Kilograms (kg)
# Distance: Meters (m)
# Time: Seconds (s)
# Velocity: Meters per second (m/s)

# ----------------------------------------------------------------------
# >> FUNDAMENTAL PHYSICS
# ----------------------------------------------------------------------

G = 6.67430e-11  # m^3 kg^-1 s^-2 (The Gravitational Constant)

# ----------------------------------------------------------------------
# >> SCALE & TIME CONSTANTS
# ----------------------------------------------------------------------

# Astronomical Unit (mean distance from Earth to Sun)
AU = 1.495978707e11  # meters

# Time conversion units
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400        # This is a great default 'dt' for large orbits
SECONDS_PER_YEAR = 31557600    # (approx 365.25 days)

# ----------------------------------------------------------------------
# >> SOLAR SYSTEM BODY DATA
# ----------------------------------------------------------------------
# For planets, 'ORBIT_R' is the mean orbital radius (semi-major axis)
# and 'ORBIT_V' is the mean orbital velocity.
# These are provided as a convenient starting point for simple orbits.
# 'RADIUS' is the physical radius of the body (useful for collision detection).

# --- SUN ---
SUN_MASS = 1.989e30
SUN_RADIUS = 6.963e8

# --- PLANETS ---
# Mercury
MERCURY_MASS = 3.301e23
MERCURY_RADIUS = 2.440e6
MERCURY_ORBIT_R = 0.387 * AU
MERCURY_ORBIT_V = 4.787e4

# Venus
VENUS_MASS = 4.867e24
VENUS_RADIUS = 6.052e6
VENUS_ORBIT_R = 0.723 * AU
VENUS_ORBIT_V = 3.502e4

# Earth
EARTH_MASS = 5.972e24
EARTH_RADIUS = 6.371e6
EARTH_ORBIT_R = 1.0 * AU  # By definition
EARTH_ORBIT_V = 2.978e4

# Mars
MARS_MASS = 6.417e23
MARS_RADIUS = 3.390e6
MARS_ORBIT_R = 1.524 * AU
MARS_ORBIT_V = 2.407e4

# Jupiter
JUPITER_MASS = 1.898e27
JUPITER_RADIUS = 6.991e7
JUPITER_ORBIT_R = 5.204 * AU
JUPITER_ORBIT_V = 1.307e4

# Saturn
SATURN_MASS = 5.683e26
SATURN_RADIUS = 5.823e7
SATURN_ORBIT_R = 9.582 * AU
SATURN_ORBIT_V = 9.68e3

# Uranus
URANUS_MASS = 8.681e25
URANUS_RADIUS = 2.536e7
URANUS_ORBIT_R = 19.229 * AU
URANUS_ORBIT_V = 6.81e3

# Neptune
NEPTUNE_MASS = 1.024e26
NEPTUNE_RADIUS = 2.462e7
NEPTUNE_ORBIT_R = 30.11 * AU
NEPTUNE_ORBIT_V = 5.43e3

# --- OTHER BODIES ---

# Earth's Moon
MOON_MASS = 7.342e22
MOON_RADIUS = 1.737e6
MOON_ORBIT_R = 3.844e8  # (Relative to Earth)
MOON_ORBIT_V = 1.022e3  # (Relative to Earth)

# Halley's Comet (Perihelion data)
HALLEY_MASS = 2.2e14
HALLEY_APHELION_R = 35.14*AU
HALLEY_APHELION_V = 780
HALLEY_PERIHELION_R = 8.78e10
HALLEY_PERIHELION_V = 5.45e4