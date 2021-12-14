import os
from collections import defaultdict
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

FAILSAFE_LIMIT = 100000

def parse_input(filepath):
  children = defaultdict(list)
  with open(filepath, 'r') as f:
    for f in get_file_lines(f):
      a, b = f.split('-')
      children[a].append(b)
      children[b].append(a)
  return children

def solve(graph):
  processing = [('start', set())]
  ans = 0
  failsafe = 0
  while processing:
    failsafe += 1
    if failsafe > FAILSAFE_LIMIT:
      raise Exception('possible loop detected')

    node, visited = processing.pop()
    if node == 'end':
      ans += 1
    elif node[0].isupper() or node not in visited:
      visited = set(visited)
      visited.add(node)
      for ch in graph[node]:
        processing.append((ch, visited))
  
  return ans

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))