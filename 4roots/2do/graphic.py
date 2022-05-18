import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10,.1)
y = np.arange(1,10,.1)

plt.scatter(x,y, color="blue")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("incremento")
plt.show()