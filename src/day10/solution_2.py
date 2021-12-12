import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

charmap = {
  ')': '(',
  ']': '[',
  '}': '{',
  '>': '<',
}

charscores = {
  '(': 1,
  '[': 2,
  '{': 3,
  '<': 4,
}

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return get_file_lines(f)

def score(line):
  stack = []
  for c in line:
    if c in charmap:
      if stack.pop() != charmap[c]:
        return None
    else:
      stack.append(c)

  score = 0
  for c in stack[::-1]:
    score = score * 5 + charscores[c]
  return score

def solve(input):
  scores = [x for x in [score(l) for l in input] if x is not None]
  return sorted(scores)[len(scores) // 2]

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))