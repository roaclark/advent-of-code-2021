import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.grid import get_neighbors
import heapq

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [[int(x) for x in l] for l in get_file_lines(f)]

def solve(grid):
  goal = (len(grid) - 1, len(grid[0]) - 1)
  heap = [(0, (0,0))]
  visited = set()
  while heap:
    cost, loc = heapq.heappop(heap)
    if loc == goal:
      return cost
    if loc not in visited:
      visited.add(loc)
      for nxt, nxt_cost in get_neighbors(grid, loc):
        heapq.heappush(heap, (cost + nxt_cost, nxt))
  return None

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))