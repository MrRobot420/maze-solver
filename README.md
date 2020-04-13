# MAZE SOLVER

# This program is solving mazes.

# IDEAS:

- Load maze into 2D Array [8][8]

# EXAMPLE:

[b][s][b][b][b][b][b][b]\
[b][w][w][w][w][w][w][b]\
[b][b][w][b][w][b][w][b]\
[b][b][w][b][b][b][b][b]\
[b][w][w][w][w][w][w][b]\
[b][w][b][b][w][b][w][b]\
[b][w][b][b][w][w][w][b]\
[b][b][b][b][b][e][b][b]\

# MEANING:

- b = black
- w = white
- s = start
- e = end
- n = node  --> A point that has more than 2 possibilities
- d = dead  --> A point that has no possibility (dead end)


# FLOW:

- Program will begin @start and search the @end of the maze.
- Will thereby mark @nodes & @deadends
- Will check on every position (index) what possibilities it has.
- Will check left, right and down / up --> track which movement is executed