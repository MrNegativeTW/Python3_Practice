import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

norm = stats.norm(0, 1)

x1 = norm.rvs(size=100000)**2
x2 = norm.rvs(size=100000)**2
x3 = norm.rvs(size=100000)**2

f = x1 + x2 + x3

plt.hist(f, 60, normed=True)

# Plot the theoretical density of f
x = np.arange(0, 30, .05)
plt.plot(x, stats.chi2.pdf(x, df=3), color='r', lw=2)
plt.show()