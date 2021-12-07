import os
from .solution_1 import solve, parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solution(filepath):
  input = parse_input(filepath)
  return solve(input, 256)

if __name__ == '__main__':
  print(solution(input_path))