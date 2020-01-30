"""Implementation of Wilson algorithm."""
import random
from typing import List, Tuple, Optional
import numpy as np
from hapsmazes import ADDED, UNVISITED
from hapsmazes.generators.utils import create_empty_maze


def fill_path(maze: np.ndarray, path: List[Tuple[int, int]]) -> None:
    for i in range(len(path) - 1):
        maze[path[i]] = ADDED
        maze[(path[i][0] + path[i + 1][0]) // 2, (path[i][1] + path[i + 1][1]) // 2] = ADDED
    maze[path[-1]] = ADDED


def choose_random_unvisited_node(maze: np.ndarray) -> Optional[Tuple[int, int]]:
    y_indices, x_indices = np.where(maze == UNVISITED)
    if len(y_indices) == 0:
        return None
    idx = np.random.choice(len(y_indices))
    return y_indices[idx], x_indices[idx]


def random_walk(maze: np.ndarray, start_node) -> List[Tuple[int, int]]:
    path = [start_node]
    previous = None

    while maze[path[-1]] != ADDED:

        neighbours = []

        if path[-1][0] - 2 >= 1:
            neighbours.append((path[-1][0] - 2, path[-1][1]))
        if path[-1][1] - 2 >= 1:
            neighbours.append((path[-1][0], path[-1][1] - 2))
        if path[-1][0] + 2 <= maze.shape[0] - 1:
            neighbours.append((path[-1][0] + 2, path[-1][1]))
        if path[-1][1] + 2 <= maze.shape[1] - 1:
            neighbours.append((path[-1][0], path[-1][1] + 2))

        if previous in neighbours:
            neighbours.remove(previous)

        next_node = random.choice(neighbours)

        if next_node in path:
            path = path[: path.index(next_node) + 1]
        else:
            path.append(next_node)

        previous = None if len(path) < 2 else path[-2]
    return path


def wilson(height: int, width: int) -> np.ndarray:
    maze = create_empty_maze(height, width)
    maze[choose_random_unvisited_node(maze)] = ADDED

    next_unvisited = choose_random_unvisited_node(maze)

    while next_unvisited is not None:
        path = random_walk(maze, next_unvisited)
        fill_path(maze, path)
        next_unvisited = choose_random_unvisited_node(maze)

    return maze
