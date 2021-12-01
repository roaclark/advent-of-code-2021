import os
from functools import reduce
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(input):
  return reduce(lambda a, b: a * b, input)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))