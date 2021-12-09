import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 1, 7, 4, 8
unique_counts = set([2, 3, 4, 7])

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [l.split(' | ')[1].split(' ') for l in get_file_lines(f)]

def solve(input):
  return sum(1 for l in input for d in l if len(d) in unique_counts)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))