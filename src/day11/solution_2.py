import os
from .solution_1 import parse_input, simulate_step
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

LIMIT = 10000

def solve(grid):
  size = len(grid) * len(grid[0])
  step = 0
  while step < LIMIT:
    step += 1
    flashed, grid = simulate_step(grid)
    if flashed == size:
      return step
  raise Exception('Exceeded maximum step count')
    

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))