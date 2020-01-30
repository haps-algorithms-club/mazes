# HAPS mazes

A library demonstrating maze generation and solving strategies.

## Installing

You can install library as usual with `pip install .`

## Command line scripts

The package install the following scripts:

- generate-maze

### Running maze generator

To run maze generator use `generate-maze`. The full usage looks like this:

```bash
generate-maze --algorithm wilson --width=50 --height=50 --img maze.png --dump maze.npy
```

This would generate 50x50 maze using Wilosn's algorithm and save its image as maze.png and corresponding numpy array as maze.npy.

## Examples

### Wilson algorithm

![Wilson](images/wilson.gif =200x200)
