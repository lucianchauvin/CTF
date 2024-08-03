import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a list of 3D points
points = []
with open("better.data") as f:
    for x in f:
        l = x.split(",")
        points.append((int(l[0]),int(l[1]),int(l[2])))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter3D(*zip(*points))

# Set the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
