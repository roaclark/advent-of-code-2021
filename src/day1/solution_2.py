import os
from .solution_1 import parse_input
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(input):
  return sum(a < b for a, b in zip(input[:-3], input[3:]))

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))