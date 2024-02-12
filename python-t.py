import numpy as np
import matplotlib.pyplot as plt
from rplidar import RPLidar, RPLidarException

def get_data():
    try:
        lidar = RPLidar('/dev/ttyUSB0')
        for scan in lidar.iter_scans(max_buf_meas=500):
            break
        lidar.stop()
        lidar.disconnect()
        return scan
    except RPLidarException as e:
        print(f"Error: {e}")
        return []

plot_interval = 1  # Plot every iteration
max_iterations = 10000000

angle_min = np.radians(0)
angle_max = np.radians(90) # restricting from 0 to 90 degrees 

max_depth = 5.0 # depth is 5 feet

# print theta and r - r = √(x2 + y2) θ = tan-1 ( y / x )


for i in range(max_iterations):
    if (i % plot_interval == 0):
        angles = []  # Initialize as a Python list
        distances = []  # Initialize as a Python list
        intensity = []  # Initialize as a Python list
    print(i)
    current_data = get_data()
    for point in current_data:
        # Filter points based on angle and depth range
        if angle_min <= np.radians(point[1]) <= angle_max and point[2] <= max_depth:
            angles.append(np.radians(point[1]))  # Convert angle to radians
            distances.append(point[2])
            intensity.append(point[1])  # Use distance (or another appropriate value) as intensity

    if i % plot_interval == 0 and angles and distances:
        plt.clf()
        ax = plt.subplot(111, polar=True)
        sc = ax.scatter(angles, distances, c=intensity, cmap='viridis', marker='o', alpha=0.5)
        plt.title('RPLidar Data (Polar Plot)')
        plt.colorbar(sc, label='Intensity')
        plt.grid(True)
        plt.pause(0.1)

plt.show(block=False)
plt.pause(10)  # Adjust as needed to keep the plot visible for some time
plt.close()
