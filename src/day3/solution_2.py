import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def filter_numbers(input, i, inv=False):
  ones = sum(line[i] == '1' for line in input)
  most_common = '1' if ones >= len(input) / 2 else '0'
  return [line for line in input if (line[i] == most_common) ^ inv]

def solve(input):
  i = 0
  ox_vals = input
  while len(ox_vals) > 1:
    ox_vals = filter_numbers(ox_vals, i)
    i += 1

  i = 0
  co2_vals = input
  while len(co2_vals) > 1:
    co2_vals = filter_numbers(co2_vals, i, inv=True)
    i += 1
  
  return int(ox_vals[0], 2) * int(co2_vals[0], 2)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))