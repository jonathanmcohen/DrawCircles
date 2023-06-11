import numpy as np
import matplotlib.pyplot as plt

# Create a blank image
image_size = (2000, 2000)
image = np.ones(image_size) * 255

# Define the circle parameters
circle_center = (1000, 1000)
circle_radii = [150, 300, 450, 600]
circle_colors = ['red', 'green', 'blue', 'yellow']
circle_dots = [4, 8, 16, 32]

# Draw the concentric circles
for radius, color in zip(circle_radii, circle_colors):
    y, x = np.ogrid[:image_size[0], :image_size[1]]
    mask_circle = (x - circle_center[0]) ** 2 + (y - circle_center[1]) ** 2 <= radius ** 2
    mask_background = (x - circle_center[0]) ** 2 + (y - circle_center[1]) ** 2 > (radius - 1) ** 2
    image[mask_circle] = 255
    image[mask_background] = 255

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Show the image with white background
ax.imshow(image, cmap='gray', vmin=0, vmax=255)

# Set the axis limits
ax.set_xlim(0, image_size[1])
ax.set_ylim(image_size[0], 0)

# Remove the axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])

# Plot the dots inside the circles
for radius, dots in zip(circle_radii, circle_dots):
    if dots > 0:
        theta = np.linspace(0, 2 * np.pi, dots, endpoint=False)
        x_coords = circle_center[0] + (radius - 10) * np.cos(theta)  # Adjusted radius to place dots inside
        y_coords = circle_center[1] + (radius - 10) * np.sin(theta)  # Adjusted radius to place dots inside
        dot_radius = 2  # Radius of the dots
        dot_color = 'black'  # Color of the dots
        ax.scatter(x_coords, y_coords, s=dot_radius ** 2, color=dot_color)

# Set the outline colors for the circles
for radius, color in zip(circle_radii, circle_colors):
    circle = plt.Circle(circle_center, radius, edgecolor=color, linewidth=2, fill=False)
    ax.add_artist(circle)

# Save the image as a JPG file
plt.savefig("concentric_circles.jpg", bbox_inches='tight', pad_inches=0, dpi=300)
