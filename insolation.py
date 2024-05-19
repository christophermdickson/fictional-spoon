
# Generate latitudes from 60°N to 90°N
latitudes = np.linspace(60, 90, 31)

# Initialize an array to hold the cumulative insolation values for each latitude and month
cumulative_insolation = np.zeros((len(latitudes), len(months)))

# Calculate cumulative insolation for each latitude by interpolating between 60°N and 90°N
for i, lat in enumerate(latitudes):
    # Linear interpolation for the current latitude
    insolation = insolation_60N + (lat - 60) / 30 * (insolation_90N - insolation_60N)
    # Compute cumulative insolation
    cumulative_insolation[i, :] = np.cumsum(insolation)

# Create the contour plot
X, Y = np.meshgrid(months, latitudes)
plt.figure(figsize=(10, 6))
contour = plt.contourf(X, Y, cumulative_insolation, cmap='viridis', levels=20)
plt.colorbar(contour, label='Cumulative Insolation (W/m^2)')
plt.title('Cumulative Insolation over Time and Latitude (60°N to 90°N)')
plt.xlabel('Month')
plt.ylabel('Latitude (°N)')
plt.xticks(months, ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])
plt.grid(True)
plt.show()

# To resolve the plotting issue, let's use a different approach for creating the contour plot

# Define the grid for months and latitudes
latitudes_fine = np.linspace(60, 90, 100)  # Finer grid for smooth contour
months_fine = np.arange(12)

# Interpolate insolation values for the fine latitude grid
insolation_fine = np.zeros((100, 12))
for i, lat in enumerate(latitudes_fine):
    insolation_fine[i] = (insolation_60N * (90 - lat) + insolation_90N * (lat - 60)) / 30

# Compute cumulative insolation for the fine grid
cumulative_insolation_fine = np.cumsum(insolation_fine, axis=1)

# Create the contour plot
plt.figure(figsize=(12, 8))
lat_grid, month_grid = np.meshgrid(months_fine, latitudes_fine)
cp = plt.contourf(month_grid, lat_grid, cumulative_insolation_fine, cmap='viridis', levels=20)
plt.colorbar(cp, label='Cumulative Insolation (W/m^2)')
plt.title('Cumulative Insolation over Time and Latitude')
plt.xlabel('Month')
plt.ylabel('Latitude (°N)')
plt.xticks(months_fine, ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])
plt.yticks(np.linspace(60, 90, 7))
plt.show()

# Trying another method to ensure the contour plot is generated properly

# Define a finer grid for latitudes and months
latitudes_fine = np.linspace(60, 90, 100)  # Fine grid for latitudes
months_fine = np.arange(12)  # Months from Jan to Dec

# Interpolate the cumulative insolation values for the fine latitude grid
cumulative_insolation_fine = np.zeros((100, 12))
for i, lat in enumerate(latitudes_fine):
    # Linear interpolation between 60N and 90N
    cumulative_insolation_fine[i] = np.cumsum((insolation_60N * (90 - lat) + insolation_90N * (lat - 60)) / 30)

# Create a meshgrid for plotting
lat_grid, month_grid = np.meshgrid(months_fine, latitudes_fine)

# Plot the contour plot for cumulative insolation over time and latitude
plt.figure(figsize=(12, 8))
cp = plt.contourf(month_grid

