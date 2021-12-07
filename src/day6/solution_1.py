import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [int(x) for x in f.readline().split(',')]

def solve(input, days=80):
  fish = {k: 0 for k in range(9)}
  for v in input:
    fish[v] += 1
  for _ in range(days):
    fish = {k-1: v for k, v in fish.items()}
    fish[6] += fish[-1]
    fish[8] = fish[-1]
    del fish[-1]
  return sum(fish[k] for k in fish)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))