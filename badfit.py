from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Define your data points with a quadratic relationship
x = np.array([1, 2, 3, 4, 5])
y = np.array([190, 672, 377, 166, 255])  # Quadratic relationship y = x^2

# Perform linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Function to predict future value
def future_value(x):
    return slope * x + intercept

# Print future value for x=6
print("Predicted value for x=6 (from linear regression):", future_value(6))

# Print correlation coefficient
print("Correlation Coefficient:", r)

plt.plot(x,y)
plt.scatter(x,y)
plt.show()
