from .vector import add_vectors

def get_neighbors(grid, location):
  width = len(grid)
  height = len(grid[0])
  if location[0] > 0:
    vec = tuple(add_vectors(location, (-1, 0)))
    yield vec, grid[vec[0]][vec[1]]
  if location[1] > 0:
    vec = tuple(add_vectors(location, (0, -1)))
    yield vec, grid[vec[0]][vec[1]]
  if location[0] < width-1:
    vec = tuple(add_vectors(location, (1, 0)))
    yield vec, grid[vec[0]][vec[1]]
  if location[1] < height-1:
    vec = tuple(add_vectors(location, (0, 1)))
    yield vec, grid[vec[0]][vec[1]]

def iterate_grid(grid):
  for r, row in enumerate(grid):
    for c, val in enumerate(row):
      yield (r, c), val