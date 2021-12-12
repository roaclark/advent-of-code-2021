import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

charmap = {
  ')': ('(', 3),
  ']': ('[', 57),
  '}': ('{', 1197),
  '>': ('<', 25137),
}

def score(line):
  stack = []
  for c in line:
    if c in charmap:
      match, score = charmap[c]
      if stack.pop() != match:
        return score
    else:
      stack.append(c)
  return 0

def solve(input):
  return sum(score(l) for l in input)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))