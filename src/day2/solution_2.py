import os
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(input):
  depth = 0
  hori = 0
  aim = 0
  for dir, mag in input:
    if dir == 'forward':
      hori += mag
      depth += aim * mag
    elif dir == 'up':
      aim -= mag
    elif dir == 'down':
      aim += mag
  return depth * hori

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))