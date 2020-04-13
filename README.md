# MAZE SOLVER

# This program is solving mazes.

# IDEAS:

- Load maze into 2D Array [8][8]

# EXAMPLE:

[O][S][O][O][O][O][O][O]\
[O][I][N][I][N][I][N][O]\
[O][O][I][O][X][O][X][O]\
[O][O][I][O][O][O][O][O]\
[O][N][N][I][N][I][N][O]\
[O][I][O][O][I][O][I][O]\
[O][X][O][O][N][N][N][O]\
[O][O][O][O][O][E][O][O]\

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