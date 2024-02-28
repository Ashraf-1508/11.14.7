import numpy as np
import matplotlib.pyplot as plt

# Parameters for the first graph
A1 = np.sqrt(2)
omega1 = np.pi
phi1 = -np.pi/4

# Parameters for the second graph
A2 = np.sqrt(2)
omega2 = np.pi
phi2 = np.pi/4

# Time values
t = np.linspace(0, 2*np.pi, 100)

# SHM equations
y1 = A1 * np.cos(omega1 * t + phi1)
y2 = A2 * np.sin(omega2 * t + phi2)

# Plotting both graphs
plt.plot(t, y1, label=f'$A \cos( \omega t + \phi)$', color='blue')
plt.plot(t, y2, label=f'$B \sin( \omega t + \\alpha)$', color='red')

plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.legend()
plt.grid(True)
plt.show()

