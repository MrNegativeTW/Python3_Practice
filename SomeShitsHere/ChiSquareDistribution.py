# 統計學作業 2019/12/09
# ------------------------------
import numpy as numpy
import scipy.stats as stats
import matplotlib.pyplot as plt

# Normal Distribution
norm = stats.norm(0, 1)

# Degree of freedom: 4
# Number of samples: 100,000
x1 = norm.rvs(size = 100000)**2
x2 = norm.rvs(size = 100000)**2
x3 = norm.rvs(size = 100000)**2
x4 = norm.rvs(size = 100000)**2

# Add each of them
y = x1 + x2 + x3 + x4


# Plot the histogram
plt.hist(y, 30, normed = True, color = 'c')

# Plot the curve
x = numpy.arange(0, 30, .05)
plt.plot(x, stats.chi2.pdf(x, df = 4), color = 'r', lw = 2)


# Fire it up
plt.show()