import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6)
y = np.exp(-t)

t_pts = np.array([0.2, 2, 5])
y_pts = np.exp(-t_pts)
print(y_pts)

plt.figure(figsize=(9, 5))
plt.plot(t, y)
plt.scatter(t_pts, y_pts)
plt.xlabel('time t', fontsize=18)
plt.ylabel('exp ( -t / T )', fontsize=18)
plt.xlim([np.min(t), np.max(t)])
plt.ylim([0, 1])
plt.xticks([0.2, 1, 2, 3, 4, 5], ['0.2T', 'T', '2T', '3T', '4T', '5T'], fontsize=14)
plt.yticks(np.arange(0, 1.2, 0.2), fontsize=14)
plt.grid()
plt.show()
