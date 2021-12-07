import os
from ..helpers.file_parsers import get_file_lines

class Board:
  def __init__(self, grid):
    self.board = grid
    self.row_count = [5 for _ in range(5)]
    self.col_count = [5 for _ in range(5)]
    self.val_to_loc = {}
    self.score = 0
    for r, row in enumerate(grid):
      for c, val in enumerate(row):
        self.val_to_loc[val] = (r, c)
        self.score += val
  
  # returns (has_won, score)
  def call(self, number):
    if number in self.val_to_loc:
      r, c = self.val_to_loc[number]
      self.row_count[r] -= 1
      self.col_count[c] -= 1
      self.score -= number
      if self.row_count[r] == 0 or self.col_count[c] == 0:
        return (True, number * self.score)
      return (False, None)
    return (False, None)

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    lines = get_file_lines(f)
    numbers = [int(x) for x in lines[0].split(',')]
    boards = []
    for i in range(2, len(lines)-4, 6):
      grid = []
      for offset in range(0, 5):
        grid.append([int(x) for x in lines[i+offset].split()])
      boards.append(Board(grid))
    return numbers, boards

def solve(input):
  numbers, boards = input
  for n in numbers:
    for b in boards:
      has_won, score = b.call(n)
      if has_won:
        return score
  return None

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))