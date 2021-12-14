import os
from .solution_1 import parse_input, fold_paper

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def format_string(dots):
  max_x = max(d[0] for d in dots)
  max_y = max(d[1] for d in dots)
  return '\n'.join([
    ''.join(['#' if (x, y) in dots else ' ' for x in range(max_x+1)])
    for y in range(max_y+1)
  ])

def get_dots(dots, folds):
  for f in folds:
    dots = fold_paper(dots, f)
  return dots

def solve(input):
  dots, folds = input
  return format_string(get_dots(dots, folds))

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))