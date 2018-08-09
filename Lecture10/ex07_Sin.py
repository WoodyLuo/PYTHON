'''
Exercise07 - Sin(x) Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0, 2 * np.pi, 100)
np.savetxt("sin.txt", n, fmt="%.6f")
x = np.loadtxt("sin.txt")
y = np.sin(x)
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.legend()
plt.savefig("sin(x).png")
plt.show()


