import os
from .solution_1 import parse_input, solve as solve_1

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

DUPLICATES = 5

def increment_grid(grid):
  return [[x + 1 if x < 9 else 1 for x in l] for l in grid]

def build_row(grid, duplicates):
  entries = [grid]
  for _ in range(duplicates - 1):
    entries.append(increment_grid(entries[-1]))
  return [[x for row in rows for x in row] for rows in zip(*entries)]

def expand_grid(grid, duplicates=DUPLICATES):
  new_grid = []
  row_start = grid
  for _ in range(duplicates):
    new_grid += build_row(row_start, duplicates)
    row_start = increment_grid(row_start)
  return new_grid

def solve(grid):
  return solve_1(expand_grid(grid))

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))