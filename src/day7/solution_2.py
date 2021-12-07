import os
from .solution_1 import parse_input

# I have a hunch that you can use a similar proof to part 1 to find a global minima in less than O(n^2)
# The first step of the part 1 proof (prove there are no non-global local minima) still stands
# but I don't have an efficient way to compute a local minima like the median was for part 1

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute_cost(start, end):
  diff = abs(start - end)
  return (diff + 1) * diff // 2

def solve(pos):
  min_cost = None
  for target in range(min(pos), max(pos) + 1):
    cost = sum(compute_cost(p, target) for p in pos)
    min_cost = cost if min_cost is None else min(cost, min_cost)
  return min_cost

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))