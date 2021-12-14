import os
from collections import Counter
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    template = f.readline().strip()
    f.readline()
    rules = [l.split(' -> ') for l in get_file_lines(f)]
    rules = {k: v for k, v in rules}
    return template, rules

def get_inner_counts_for_pair(pair, rules, steps, memo={}):
  if (pair, steps) in memo:
    return memo[(pair, steps)]
  if steps == 1:
    ans = Counter(rules[pair])
    memo[(pair, steps)] = ans
    return ans
  mid = rules[pair]
  ans = get_inner_counts_for_pair(pair[0] + mid, rules, steps-1, memo) \
    + get_inner_counts_for_pair(mid + pair[1], rules, steps-1, memo) \
    + Counter(mid)
  memo[(pair, steps)] = ans
  return ans

def solve(input, steps=10):
  template, rules = input
  c = Counter(template)
  for a, b in zip(template[:-1], template[1:]):
    c += get_inner_counts_for_pair(a + b, rules, steps)
  letter_counts = c.most_common()
  return letter_counts[0][1] - letter_counts[-1][1]

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))