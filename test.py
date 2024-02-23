import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

max_iterations = 20  # or any desired value
plot_interval = 1  # set to 30 for saving every 30 iterations

# Lists to store data for each 30 iterations
all_angles = []
all_distances = []

for i in range(max_iterations):
    angles = []  # Initialize as a Python list
    distances = []  # Initialize as a Python list

    print(i)
    current_data = get_data()
    for point in current_data:
        if point[0] == 15:
            angles.append(np.radians(point[1]))  # Convert angle to radians
            distances.append(point[2])

    if i % plot_interval == 0 and angles and distances:
        all_angles.append(angles)
        all_distances.append(distances)

# Create 3D plot with x, y, and z coordinates
fig = plt.figure()
ax3d = fig.add_subplot(111, projection='3d')

for i, (angles, distances) in enumerate(zip(all_angles, all_distances)):
    x = distances * np.cos(np.radians(angles)) 
    y = distances * np.sin(np.radians(angles))
    z = np.full_like(distances, i * plot_interval)
    ax3d.scatter(x, y, z, cmap='Pink', marker='o', alpha=0.5)

ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z ')
plt.title('3D Plot')
plt.grid(True)
plt.show()
