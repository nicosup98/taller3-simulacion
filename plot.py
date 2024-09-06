from main import simulacion

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

data = simulacion()["data"]
data_x = []
data_y = []
for d in data:
    x, y = d
    data_x.append(x)
    data_y.append(y)


sizes = np.random.uniform(-10, 90, len(data_x))
colors = np.random.uniform(-10, 90, len(data_x))

fig, ax = plt.subplots()

ax.scatter(data_x, data_y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(-10, 10), xticks=np.arange(-10, 10),
       ylim=(-10, 10), yticks=np.arange(-10, 10))
ax.set_ylabel("y")
ax.set_xlabel("x")
ax.grid(True)

plt.show()
