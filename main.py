import matplotlib.pyplot as plt
import numpy as np

print(
    np.sqrt(2)
)

plt.plot(0, 1)

x = np.arange(0, np.pi*2, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
