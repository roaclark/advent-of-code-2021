import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    vents = []
    for line in  get_file_lines(f):
      a, b = line.split(' -> ')
      ax, ay = a.split(',')
      bx, by = b.split(',')
      a = (int(ax), int(ay))
      b = (int(bx), int(by))
      vents.append((a, b))
    return vents

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
  return len(double)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))