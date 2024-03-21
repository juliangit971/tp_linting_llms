import numpy as np
import matplotlib.pyplot as plt

# Parameters
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)

# Function
def sin_product(x, y):
    """Helper function to compute sin(x)*sin(y)."""
    return np.sin(X) * np.sin(Y)

# Create data
Z = sin_product(X, Y)

# Plotting
fig, ax = plt.subplots()
ax.contourf(X, Y, Z, cmap='coolwarm')
cb = fig.colorbar(ax.contourf(X, Y, Z, cmap='summer'), shrink=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('2D Plot of sin(x)*sin(y)')
plt.show()