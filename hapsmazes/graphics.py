"""Utilities for drawing mazes."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def draw_maze(maze):
    """Draw maze as an image."""
    color_map = ListedColormap(np.array([[0, 0, 0, 1], [1, 1, 1, 1]]))
    plt.axis("off")
    plt.imshow(maze, cmap=color_map)

