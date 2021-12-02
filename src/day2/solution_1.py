import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    lines = [s.split() for s in get_file_lines(f)]
    return [[a, int(b)] for a, b in lines]

def solve(input):
  depth = 0
  hori = 0
  for dir, mag in input:
    if dir == 'forward':
      hori += mag
    elif dir == 'up':
      depth -= mag
    elif dir == 'down':
      depth += mag
  return depth * hori

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))