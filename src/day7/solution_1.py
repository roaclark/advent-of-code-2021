import os

# The median can be proven to be the optimal solution using the following steps:
# 1. Prove there are no non-global local minima by contradiction
#    a. Two minima means there must be a local maxima
#    b. Prove by contradiction that there cannot by a local maxima (an index where both neighbors cost less)
#       (This isn't exactly right since adjacent costs may be the same, but meh)
# 2. Prove the median is a local minima
# 3. Combining 1 and 2 proves the median is the global minima

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [int(x) for x in f.readline().split(',')]

def solve(pos):
  pos = sorted(pos)
  target = pos[len(pos) // 2] if len(pos) % 2 else (pos[len(pos) // 2] + pos[len(pos) // 2 - 1]) // 2
  return sum(abs(p - target) for p in pos)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))