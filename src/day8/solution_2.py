import os
from ..helpers.file_parsers import get_file_lines

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

segment_to_number = {
  'abcefg': '0',
  'cf': '1',
  'acdeg': '2',
  'acdfg': '3',
  'bcdf': '4',
  'abdfg': '5',
  'abdefg': '6',
  'acf': '7',
  'abcdefg': '8',
  'abcdfg': '9',
}

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [[x.split(' ') for x in l.split(' | ')] for l in get_file_lines(f)]
  
def get_only_value(set):
  if len(set) != 1:
    raise Exception('set does not have one value: ' + str(set))
  return list(set)[0]

# actual => correct
def get_segment_map(digits):
  one = None
  four = None
  seven = None
  eight = None
  six_segments = []
  for d in digits:
    if len(d) == 2:
      one = d
    elif len(d) == 4:
      four = d
    elif len(d) == 3:
      seven = d
    elif len(d) == 7:
      eight = d
    elif len(d) == 6:
      six_segments.append(d)

  zero = None
  six = None
  nine = None
  for d in six_segments:
    if set(d).issuperset(set(seven + four)):
      nine = d
    elif set(d).issuperset(set(one)):
      zero = d
    else:
      six = d

  a = get_only_value(set(seven) - set(four))
  d = get_only_value(set(eight) - set(zero))
  b = get_only_value(set(four) - set(one) - set([d]))
  c = get_only_value(set(eight) - set(six))
  e = get_only_value(set(eight) - set(nine))
  f = get_only_value(set(one).intersection(set(six)))
  g = get_only_value(set(nine) - set(four) - set(seven))

  return {
    a: 'a',
    d: 'd',
    b: 'b',
    c: 'c',
    e: 'e',
    f: 'f',
    g: 'g',
  }

def get_output_number(segment_map, output):
  corrected_output = [''.join(sorted(segment_map[seg] for seg in x)) for x in output]
  output_num = ''.join([segment_to_number[x] for x in corrected_output])
  return int(output_num)
  
def solve_line(line):
  digits, output = line
  segment_map = get_segment_map(digits)
  return get_output_number(segment_map, output)

def solve(input):
  return sum(solve_line(l) for l in input)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))