"""
Author: Paul Moran
Fibonnaci spiral
16/08/2024
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#The golden ration, omega
omega = (1 + math.sqrt(5)) /2
pi = 3.1415

x = []
y = []

for t in np.arange(0, 20,0.05):
	x.append(math.sin(t) * omega**(t/pi))
	y.append(math.cos(t) * omega**(t/pi))

plt.plot(x,y)
plt.show()