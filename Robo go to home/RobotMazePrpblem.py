# Backtracking
maze = [[".", ".", ".", "."],
        [".", "X", "X", "X"],
        [".", ".", ".", "X"],
        ["X", "X", ".", "."]]
# maze = [["ROBOT IS HERE", ".", ".", "."],
#         [".", "X", "X", "X"],
#         [".", ".", ".", "X"],
#         ["X", "X", ".", "HOME_IS_HERE(Fixed)"]]

def print_maze(maze):
    for row in maze:
        for values in row:
            print(values, end="  ")
        print()


def solve_maze(maze):
    if len(maze) < 1:
        return None
    if len(maze[0]) < 1:
        return None
    return solve_maze_helper(maze, [], 0, 0)


def solve_maze_helper(maze, sol, pos_row, pos_col):
    # get the sizes of rows and cols
    num_rows = len(maze)
    num_cols = len(maze[0])

    # Base cases
    # is robo already home?
    if pos_row == num_rows - 1 and pos_col == num_cols - 1:
        return sol

    # Out of bounds
    if pos_col >= num_cols or pos_row >= num_rows:
        return None

    # Is on the obstacle?
    if maze[pos_row][pos_col] == "X":
        return None

    # Recusrive case
    # robo can do either "r" or "d"
    # Try going right
    sol.append("r")
    sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col+1)
    if sol_going_right is not None:
        return sol_going_right

    # If going right doesnt work, BACKTRACK
    sol.pop()

    # lets try going down
    sol.append("d")
    sol_going_down = solve_maze_helper(maze, sol, pos_row+1, pos_col)
    if sol_going_down is not None:
        return sol_going_down

    # No solution, backtrack
    sol.pop()
    return None



print_maze(maze)
# print(solve_maze_helper(maze, [], 0, 0))
print(solve_maze(maze))