import os
from .solution_1 import parse_input

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(input):
  numbers, boards = input
  for n in numbers:
    if len(boards) > 1:
      boards = [b for b in boards if not b.call(n)[0]]
    else:
      has_won, score = boards[0].call(n)
      if has_won:
        return score
  return None

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))