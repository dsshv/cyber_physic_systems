import numpy as np
import matplotlib.pyplot as plt

space_count = 100
binary_digits = 10

rand_n = np.random.rand(binary_digits)
rand_n[np.where(rand_n >= 0.5)] = 1
rand_n[np.where(rand_n < 0.5)] = 0

sig = np.zeros(space_count*binary_digits)

id = np.where(rand_n == 1)

for i in id[0]:
    t = int(i*space_count)
    sig[t:t+space_count] = 1


plt.plot(sig)
plt.show()

