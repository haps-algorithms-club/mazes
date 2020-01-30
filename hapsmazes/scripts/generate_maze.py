"""Script for generating mazes."""
import argparse
import numpy as np
import matplotlib.pyplot as plt
from hapsmazes.generators.wilson import wilson
from hapsmazes.graphics import draw_maze


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", help="width of the maze", default=50, type=int)
    parser.add_argument("--height", help="height of the maze", default=50, type=int)
    parser.add_argument(
        "--algorithm", help="algorithm_to_use", choices=["wilson"], default="wilson"
    )
    parser.add_argument("--img", help="path of the image file", type=str)
    parser.add_argument("--dump", help="path of the dump file", type=str)

    args = parser.parse_args()

    if not args.img and not args.dump:
        print("You need to specify at least one of --img or --dump")
        exit(1)

    # TODO: add if-else-elif clause when there are more algorihtms implemented
    maze = wilson(args.height, args.width)

    if args.dump:
        np.save(args.dump, maze)
    if args.img:
        dpi = 80  # This could possibly be another parameter
        fig_height = 10 * args.height / dpi
        fig_width = 10 * args.width / dpi

        plt.figure(figsize=(fig_width, fig_height))
        draw_maze(maze)
        plt.savefig(args.img, dpi=dpi)


if __name__ == "__main__":
    main()
