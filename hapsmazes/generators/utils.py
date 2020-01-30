import numpy as np
from hapsmazes import UNVISITED


def create_empty_maze(height: int, width: int) -> np.ndarray:
    maze = np.zeros((2 * height + 1, 2 * width + 1), dtype=np.int8)
    maze[1::2, 1::2] = UNVISITED
    return maze
