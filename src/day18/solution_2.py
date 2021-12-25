import os
from .solution_1 import parse_input, add_numbers, calculate_magnitude
from ..helpers.linkedlist import copy_linked_list

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(input):
  res = 0
  for i in range(len(input)):
    for j in range(len(input)):
      if i != j:
        mag = calculate_magnitude(add_numbers(
          copy_linked_list(input[i]),
          copy_linked_list(input[j]),
        ))
        res = max(res, mag)
  return res

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))