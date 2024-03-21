import numpy as np
import matplotlib.pyplot as plt

# Read data from file
data = []
with open('./city.dat', 'r') as f:
    headers = next(f).strip().split()
    for line in f:
        row = list(map(lambda x: (x.strip() if type(x) is str else float(x)),
line.strip().split()))
        data.append(row)

# Extract cities, population, and area columns from the data
cities = np.array([city for city in [row[0] for row in data]])
populations = np.array([row[1] for row in data], dtype=float)
areas = np.array([row[2] for row in data], dtype=float)

# Create a scatter plot with cities as markers based on their population size
fig, ax = plt.subplots()
ax.scatter(populations, areas)

# Set up the figure and labels
ax.set_xlabel('Population')
ax.set_ylabel('Area (km²)')
ax.set_title('City Size Comparison')
ax.set_xticks(np.linspace(min(populations), max(populations), 10))
ax.legend(cities, loc='best')
plt.show()