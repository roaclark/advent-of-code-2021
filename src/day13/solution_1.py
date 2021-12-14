import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    dots, folds = f.read().split('\n\n')
    dots = set(tuple([int(x) for x in l.split(',')]) for l in dots.splitlines())
    folds = [(l[11], int(l[13:])) for l in folds.splitlines()]
    return dots, folds

def fold_dot(dot, fold):
  axis, fold_line = fold
  x, y = dot
  new_x = x if axis == 'y' else fold_line - abs(fold_line - x)
  new_y = y if axis == 'x' else fold_line - abs(fold_line - y)
  return (new_x, new_y)

def fold_paper(dots, fold):
  return set(fold_dot(d, fold) for d in dots)

def solve(input):
  dots, folds = input
  return len(fold_paper(dots, folds[0]))

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))