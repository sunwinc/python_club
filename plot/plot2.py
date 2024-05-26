import matplotlib.pyplot as plt
import numpy as np

plt.ion()

x = np.linspace(1, 10)
y = np.sin(x)
plt.plot(x, y)
plt.draw()
plt.pause(20)