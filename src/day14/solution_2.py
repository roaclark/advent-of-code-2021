import os
from .solution_1 import parse_input, solve

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solution(filepath):
  input = parse_input(filepath)
  return solve(input, steps=40)

if __name__ == '__main__':
  print(solution(input_path))