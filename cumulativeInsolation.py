import numpy as np
import matplotlib.pyplot as plt

# Define the constrained grid for latitudes (70°N to 90°N) and months (Jan to Sep)
latitudes_constrained = np.linspace(70, 90, 21)  # Fine grid for latitudes between 70°N and 90°N
months_constrained = np.arange(9)  # Months from Jan to Sep

# Extracted monthly insolation values (W/m^2) from the graph for 60°N and 90°N latitudes
insolation_60N = np.array([0, 100, 200, 300, 400, 500, 400, 300, 200, 100, 0, 0])
insolation_90N = np.array([0, 0, 0, 100, 300, 500, 300, 100, 0, 0, 0, 0])

# Interpolate the insolation values for the constrained grid
insolation_constrained = np.zeros((21, 9))
for i, lat in enumerate(latitudes_constrained):
    # Linear interpolation between 60N and 90N
    insolation_interpolated = (insolation_60N[:9] * (90 - lat) + insolation_90N[:9] * (lat - 60)) / 30
    insolation_constrained[i] = insolation_interpolated

# Calculate cumulative insolation
cumulative_insolation_constrained = np.cumsum(insolation_constrained, axis=1)

# Create a meshgrid for plotting
lat_grid, month_grid = np.meshgrid(months_constrained, latitudes_constrained)

# Plot the contour plot for cumulative insolation over time and latitude
plt.figure(figsize=(12, 8))
cp = plt.contourf(month_grid, lat_grid, cumulative_insolation_constrained, cmap='viridis', levels=20)
plt.colorbar(cp, label='Cumulative Insolation (W/m^2)')
plt.title('Cumulative Insolation over Time and Latitude (70°N to 90°N)')
plt.xlabel('Month')
plt.ylabel('Latitude (°N)')
plt.xticks(months_constrained, ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S'])
plt.yticks(np.linspace(70, 90, 5))
plt.show()
