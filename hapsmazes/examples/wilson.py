"""Example generation of maze with Wilson algorithm."""
import matplotlib.pylab as plt
from hapsmazes.generators.wilson import wilson
from hapsmazes.graphics import draw_maze

HEIGHT = 50
WIDTH = 50


if __name__ == "__main__":
    maze = wilson(HEIGHT, WIDTH)
    draw_maze(maze)
    plt.show()
