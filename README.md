# Maze Solver using Backtracking

This Python code demonstrates a simple maze-solving algorithm using backtracking. The goal is to find a path from the start point (top-left) to the end point (bottom-right) in a given maze, avoiding obstacles represented by "X" cells.

## How it Works

1. **Maze Representation**: The maze is represented as a 2D grid, where "." represents open cells, "X" represents obstacles, and the robot's starting point is at the top-left corner (0,0).

2. **Base Cases**: Several base cases are checked before proceeding with the backtracking. If the robot is already at the home location (bottom-right), the solution is found and returned. If the robot is out of bounds (beyond the maze's boundaries) or on an obstacle, it returns None, indicating no solution.

3. **Backtracking**: The algorithm uses recursive backtracking to explore all possible paths. It tries to move right ("r") and then down ("d"). If moving right or down leads to a valid solution, it returns the solution path. If not, it backtracks by removing the last move and tries the other direction.

4. **Printing the Maze**: The `print_maze` function is used to display the maze grid, marking the robot's path with "r" for right and "d" for down.

5. **Solving the Maze**: The `solve_maze` function initiates the maze-solving process, starting from the top-left corner. If a solution is found, it returns the path as a list of moves (e.g., ["r", "r", "d", "r"]). If no solution is possible, it returns None.

## How to Use

1. Define the maze as a 2D grid, where "." represents open cells, "X" represents obstacles, and the starting point is at the top-left.

2. Call the `solve_maze` function with your maze as an argument.

3. If a solution exists, it will return a list of moves to reach the home location. Otherwise, it will return None.

## Example

```python
maze = [[".", ".", ".", "."],
        [".", "X", "X", "X"],
        [".", ".", ".", "X"],
        ["X", "X", ".", "."]]

path = solve_maze(maze)
if path:
    print("Solution Path:", path)
else:
    print("No solution found.")
```

## GitHub README

**Repository Name**: Robo Go To Home

**Description**: This repository contains a Python implementation of a maze-solving algorithm using backtracking. The algorithm finds a path from the top-left corner to the bottom-right corner of a maze while avoiding obstacles.

**Usage**:
1. Define your maze in the code.
2. Call the `solve_maze` function to find a solution path.
3. If a solution exists, it will be returned as a list of moves.

**Sample Code**:
```python
# Define your maze
maze = [[".", ".", ".", "."],
        [".", "X", "X", "X"],
        [".", ".", ".", "X"],
        ["X", "X", ".", "."]]

# Solve the maze
path = solve_maze(maze)
if path:
    print("Solution Path:", path)
else:
    print("No solution found.")
```

This simple backtracking maze solver can be a useful addition to your projects requiring pathfinding in grid-based environments.
