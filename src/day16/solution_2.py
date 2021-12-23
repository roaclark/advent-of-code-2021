import os
from ..helpers.math import product
from .solution_1 import parse_input, parse_packet

computations = {
  0: sum,
  1: product,
  2: min,
  3: max,
  5: lambda x: 1 if x[0] > x[1] else 0,
  6: lambda x: 1 if x[0] < x[1] else 0,
  7: lambda x: 1 if x[0] == x[1] else 0,
}

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute_packet(packet):
  if packet.type_id == 4:
    return packet.value
  subvalues = [compute_packet(p) for p in packet.subpackets]
  return computations[packet.type_id](subvalues)

def solve(input):
  packet = parse_packet(input)
  return compute_packet(packet)

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))