import numpy as np
import matplotlib.pyplot as plt

x = []
lx = int(input("Enter x array length: "))
for i in range(lx):
    l = float(input("Enter lx: "))
    x.append(l)

ly = float(input("Enter ly: "))
t = np.arange(0, ly, 0.01)
h = np.zeros(len(t))
for i in range(lx):
    h += x[i] * np.cos(2 * np.pi * t * (i + 1))

plt.plot(t, h)
plt.show()
