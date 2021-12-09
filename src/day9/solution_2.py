import os
from .solution_1 import parse_input
from ..helpers.grid import iterate_grid, get_neighbors

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def get_basin_size(grid, low_point):
  visited = set()
  stack = [(low_point, grid[low_point[0]][low_point[1]])]
  while stack:
    curr_loc, curr_val = stack.pop()
    if curr_loc not in visited and curr_val != 9:
      visited.add(curr_loc)
      stack += list(get_neighbors(grid, curr_loc))
  return len(visited)

def solve(grid):
  basin_sizes = []
  for loc, val in iterate_grid(grid):
    if all(n_val > val for _, n_val in get_neighbors(grid, loc)):
      basin_sizes.append(get_basin_size(grid, loc))
  basin_sizes.sort()
  return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))