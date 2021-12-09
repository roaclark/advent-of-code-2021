import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.grid import iterate_grid, get_neighbors

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [[int(x) for x in line] for line in get_file_lines(f)]

def solve(grid):
  res = 0
  for loc, val in iterate_grid(grid):
    if all(n_val > val for _, n_val in get_neighbors(grid, loc)):
      res += val + 1
  return res

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))