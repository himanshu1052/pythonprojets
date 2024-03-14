''' Topic:- Machine learning
Best-fit Line  =>  In linear regression the Best-fit Line  covers all data point with minimal Distance..

modely=np.poly1d(np.polyfit(x,y,3))
myline=np.linspace(10,25,100)
myline = np.linspace(0, 6, 100)
plt.scatter(x,y)
plt.plot(myline,modely(myline),color="red")
plt.xlim(5,30)
plt.ylim(500,3000)
plt.show()
newvalue=modely(25)
print(newvalue)
'''






import matplotlib.pyplot as plt

from scipy import stats
import numpy as np

# Define your data points
x = np.array([10, 15, 20, 25])
y = np.array([1000, 1200, 1800, 2800])

# Perform linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Function to predict future value
def future_value(x):
    return round(slope * x + intercept)

# Print future income for x=50
print("Future Income is =>", future_value(50))

# Print correlation coefficient
print("Correlation Coefficient:", r)

newy=list(map(future_value,x))

plt.plot(x,newy)
plt.scatter(x,newy)
plt.show()
          