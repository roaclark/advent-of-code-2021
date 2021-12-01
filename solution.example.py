import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def solve(input):
  return 0

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))