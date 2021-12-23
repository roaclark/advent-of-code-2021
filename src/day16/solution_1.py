import os

hex_to_bin = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111',
}

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

class Packet:
  def __init__(self, version, type_id, subpackets=None, value=None):
    self.version = version
    self.type_id = type_id
    self.subpackets = subpackets
    self.value = value

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return f.readline()
  
def convert_to_bin(packet):
  return ''.join(hex_to_bin[c] for c in packet)

def parse_literal_value(packet, start):
  i = start
  num = ''
  while packet[i] == '1':
    num += packet[i+1:i+5]
    i += 5
  num += packet[i+1:i+5]
  i += 5
  return int(num, 2), i

def parse_operator(packet, start):
  i = start
  length_type_id = packet[i]
  subpackets = []

  if length_type_id == '0':
    length = int(packet[i+1:i+16], 2)
    i += 16
    goal = i + length
    while i < goal:
      subpacket, i = parse_packet_helper(packet, i)
      subpackets.append(subpacket)
  else:
    count = int(packet[i+1:i+12], 2)
    i += 12
    for _ in range(count):
      subpacket, i = parse_packet_helper(packet, i)
      subpackets.append(subpacket)
  
  return subpackets, i

def parse_packet_helper(packet, start):
  i = start
  version = int(packet[i:i+3], 2)
  i += 3
  type_id = int(packet[i:i+3], 2)
  i += 3

  if type_id == 4:
    num, i = parse_literal_value(packet, i)
    return Packet(version, type_id, value=num), i
  else:
    subpackets, i = parse_operator(packet, i)
    return Packet(version, type_id, subpackets=subpackets), i

def parse_packet(packet):
  return parse_packet_helper(convert_to_bin(packet), 0)[0]

def solve(input):
  packet = parse_packet(input)
  version_sum = 0
  queue = [packet]
  while queue:
    p = queue.pop()
    version_sum += p.version
    if p.subpackets is not None:
      queue += p.subpackets
  return version_sum

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))