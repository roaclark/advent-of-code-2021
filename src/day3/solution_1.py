import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.vector import add_vectors

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def sum_bits(input):
  ones = [0 for _ in input[0]]
  for line in input:
    ones = add_vectors(ones, [int(i) for i in line])
  return ones

def solve(input):
  bit_counts = sum_bits(input)
  gamma = ''.join('1' if cnt > len(input) / 2 else '0' for cnt in bit_counts)
  epsilon = ''.join('0' if cnt > len(input) / 2 else '1' for cnt in bit_counts)
  return int(gamma, 2) * int(epsilon, 2)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))