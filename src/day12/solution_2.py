from collections import defaultdict
import os
from .solution_1 import parse_input

FAILSAFE_LIMIT = 10000000

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def solve(graph):
  processing = [('start', set(), False)]
  ans = 0
  failsafe = 0
  while processing:
    failsafe += 1
    if failsafe > FAILSAFE_LIMIT:
      raise Exception('possible loop detected')

    node, visited, second_visit = processing.pop()
    if node == 'end':
      ans += 1
    elif node[0].isupper() or node not in visited or (node != 'start' and not second_visit):
      second_visit = second_visit or (node[0].islower() and node != 'start' and node in visited)
      visited = set(visited)
      visited.add(node)
      for ch in graph[node]:
        processing.append((ch, visited, second_visit))
  
  return ans

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))