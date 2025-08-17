import matplotlib.pyplot as plt
import astropy.constants as c
import astropy.units as u
import numpy as np

mass = 1 # solar mass

def black_hole_calc(M):
    """Calculating the Schwarzschild radius, shadow and photon sphere for a
    given mass (M)."""
    
    solar_mass      = c.M_sun.to(u.kg)
    m               = M * solar_mass
    r               = 2*c.G*m/c.c**2
    return r

bh_radius       = black_hole_calc(mass).value
bh_shadow       = np.sqrt(27)/2 * bh_radius
photon_sphere   = 1.5 * bh_radius

black_hole    = plt.Circle((0, 0),
                           bh_radius,
                           color='black',
                           label='Black Hole')
shadow_radius = plt.Circle((0, 0),
                           bh_shadow,
                           color='gray',
                           alpha=0.5,
                           label='Black Hole Shadow')
photon_sphere = plt.Circle((0, 0),
                           photon_sphere,
                           color='yellow',
                           fill=False,
                           linestyle='-',
                           label='Photon Sphere')
 
fig, ax = plt.subplots()
ax.add_patch(shadow_radius)
ax.add_patch(photon_sphere)
ax.add_patch(black_hole)

plt.xlim(-bh_shadow*1.25, bh_shadow*1.25)
plt.ylim(-bh_shadow*1.25, bh_shadow*1.25)

plt.title(f'Black Hole Diagram for M = {mass} $M_\odot$')
plt.xlabel('x (m)')
plt.ylabel('y (m)')

plt.legend()
plt.grid('--', alpha = 0.3)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig(f'/home/liamhall/github/black_hole/inital_black_hole_{mass}_solarmass.png', dpi=600)
plt.show()