import os

from src.helpers.grid import get_neighbors, iterate_grid
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [[int(x) for x in l] for l in get_file_lines(f)]
  
def simulate_step(grid):
  flash_processing = []
  for point, val in iterate_grid(grid):
    grid[point[0]][point[1]] = val + 1
    if val + 1 > 9:
      flash_processing.append(point)

  flashed = set()
  while flash_processing:
    point = flash_processing.pop()
    if point not in flashed:
      flashed.add(point)
      for nxt, val in get_neighbors(grid, point, diagonal=True):
        grid[nxt[0]][nxt[1]] = val + 1
        if val + 1 > 9:
          flash_processing.append(nxt)
  
  for point in flashed:
    grid[point[0]][point[1]] = 0

  return len(flashed), grid

def solve(grid, steps=100):
  flashes = 0
  for _ in range(steps):
    step_flashes, grid = simulate_step(grid)
    flashes += step_flashes
  return flashes

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))