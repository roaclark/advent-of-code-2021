import os
from .solution_1 import parse_input, hits_range

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(input):
  goal_x, goal_y = input
  ans = 0
  for vel_x in range(goal_x[1]+1):
    for vel_y in range(goal_y[0], -goal_y[0]+1):
      if hits_range(goal_x, goal_y, vel_x, vel_y):
        ans += 1
  return ans

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))