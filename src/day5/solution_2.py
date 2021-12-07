import os
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(vents):
  single = set()
  double = set()
  for a, b in vents:
    if a[0] == b[0]:
      for x in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
        point = (a[0], x)
        if point in single:
          double.add(point)
        else:
          single.add(point)
    elif a[1] == b[1]:
      for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
        point = (x, a[1])
        if point in single:
          double.add(point)
        else:
          single.add(point)
    else:
      x_dir = 1 if a[0] < b[0] else -1
      x_range = range(a[0], b[0] + x_dir, x_dir)
      y_dir = 1 if a[1] < b[1] else -1
      y_range = range(a[1], b[1] + y_dir, y_dir)
      for x, y in zip(x_range, y_range):
        point = (x, y)
        if point in single:
          double.add(point)
        else:
          single.add(point)
  return len(double)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))