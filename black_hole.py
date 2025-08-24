import matplotlib.pyplot as plt
import astropy.constants as c
import astropy.units as u
import numpy as np

mass = 1 # solar mass

class BlackHole:
    """A simple Schwarzschild black hole model."""

    def __init__(self, M):
        self.M = M  # mass in solar masses
        solar_mass = c.M_sun.to(u.kg)
        m          = M * solar_mass
        self.radius     = (2*c.G*m/c.c**2).to(u.m).value
        self.shadow     = (np.sqrt(27)/2*(2*c.G*m/c.c**2)).value
        self.sphere = (1.5*(2*c.G*m/c.c**2)).value
        self.m_thresh = ((c.au.to(u.m)*c.c**2)/(2*c.G)).value/c.M_sun

    def summary(self):
        return {
            "Mass (M_sun)": self.M,
            "Radius (m)": self.radius,
            "Shadow (m)": self.shadow,
            "Photon Sphere (m)": self.sphere,
            "Mass Threshold (M_sun)": self.m_thresh
            }
print(f'\n{BlackHole(mass).summary()}\n')
black_hole    = plt.Circle((0, 0),
                           BlackHole(mass).radius,
                           color='black',
                           label='Black Hole')
shadow_radius = plt.Circle((0, 0),
                           BlackHole(mass).shadow,
                           color='gray',
                           alpha=0.5,
                           label='Black Hole Shadow')
photon_sphere = plt.Circle((0, 0),
                           BlackHole(mass).sphere,
                           color='yellow',
                           fill=False,
                           linestyle='-',
                           label='Photon Sphere')
sun           = plt.Circle((0, 0),
                           c.R_sun.to(u.au).value,
                           color='orange',
                           label='Sun',
                           fill=True)
earth_orbit   = plt.Circle((0, 0),
                           1,
                           color='tab:blue',
                           fill=False,
                           linestyle='--',
                           label='Earth Orbit') 
fig, ax = plt.subplots()

for object in [shadow_radius, photon_sphere, black_hole]:
    ax.add_artist(object)

if mass >= BlackHole(mass).m_thresh.value:
    ax.add_artist(earth_orbit)
    ax.add_artist(sun)
    plt.xlabel('x (AU)')
    plt.ylabel('y (AU)')
else:
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

if mass >= 1e5:
    plt.title(f'Black Hole Diagram for M = {mass:.1e} $M_\odot$')
else:
    plt.title(f'Black Hole Diagram for M = {mass:.0f} $M_\odot$')

plt.xlim(-BlackHole(mass).shadow*1.25, BlackHole(mass).shadow*1.25)
plt.ylim(-BlackHole(mass).shadow*1.25, BlackHole(mass).shadow*1.25)
plt.legend()
plt.grid('--', alpha = 0.3)
plt.gca().set_aspect('equal', adjustable='box')
#plt.savefig(f'/home/liamhall/github/black_holes/plots/initial_black_hole_'\
#            f'{mass}_solarmass.png', dpi=600)
plt.show()