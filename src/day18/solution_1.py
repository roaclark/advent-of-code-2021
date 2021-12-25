import os
from ..helpers.file_parsers import get_file_lines
from ..helpers.linkedlist import convert_list_to_linkedlist, Node

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def stringify_number(number):
  ans = []
  n = number
  prev_val = None
  while n is not None:
    if (prev_val == ']' or isinstance(prev_val, int)) and n.val != ']':
      ans.append(',')
    if isinstance(n.val, str):
      ans.append(n.val)
    else:
      ans.append(str(n.val))
    prev_val = n.val
    n = n.next
  return ''.join(ans)

def parse_number(number_str):
  i = 0
  parsed = []
  while i < len(number_str):
    if number_str[i] == '[':
      parsed.append('[')
      i += 1
    elif number_str[i] == ']':
      parsed.append(']')
      i += 1
    elif number_str[i] == ',':
      i += 1
    else:
      j = i
      while j < len(number_str) and number_str[j] in '0123456789':
        j += 1
      parsed.append(int(number_str[i:j]))
      i = j
  return convert_list_to_linkedlist(parsed)

def parse_input(filepath):
  with open(filepath, 'r') as f:
    return [parse_number(l) for l in get_file_lines(f)]

def explode_pair(start):
  open_bracket = start
  first_val = start.next.val
  second_val = start.next.next.val
  close_bracket = start.next.next.next

  new_zero = Node(0)
  new_zero.prev = open_bracket.prev
  new_zero.next = close_bracket.next
  open_bracket.prev.next = new_zero
  close_bracket.next.prev = new_zero

  n = open_bracket.prev
  while n is not None and not isinstance(n.val, int):
    n = n.prev
  if n is not None:
    n.val += first_val

  n = close_bracket.next
  while n is not None and not isinstance(n.val, int):
    n = n.next
  if n is not None:
    n.val += second_val

# returns True if exploded, False otherwise
def attempt_to_explode_pair(number):
  depth = 0
  n = number
  while n is not None:
    if n.val == '[':
      depth += 1
      if depth == 5:
        explode_pair(n)
        return True
    elif n.val == ']':
      depth -= 1
    n = n.next
  return False

def attempt_to_split_pair(number):
  n = number
  while n is not None:
    if isinstance(n.val, int) and n.val > 9:
      open_bracket = Node('[')
      first_val = Node(n.val // 2)
      second_val = Node(n.val - n.val // 2)
      close_bracket = Node(']')
      open_bracket.next, first_val.prev = first_val, open_bracket
      first_val.next, second_val.prev = second_val, first_val
      second_val.next, close_bracket.prev = close_bracket, second_val
      open_bracket.prev, n.prev.next = n.prev, open_bracket
      n.next.prev, close_bracket.next = close_bracket, n.next
      return True
    n = n.next
  return False

def reduce_number(number):
  done = False
  while not done:
    exploded = attempt_to_explode_pair(number)
    if not exploded:
      split = attempt_to_split_pair(number)
      if not split:
        done = True
  return number

def add_numbers(a, b):
  start_bracket = Node('[')
  end_bracket = Node(']')
  a_tail = a
  while a_tail.next is not None:
    a_tail = a_tail.next
  b_tail = b
  while b_tail.next is not None:
    b_tail = b_tail.next
  start_bracket.next, a.prev = a, start_bracket
  a_tail.next, b.prev = b, a_tail
  b_tail.next, end_bracket.prev = end_bracket, b_tail
  return reduce_number(start_bracket)

def add_all(input):
  ans = input[0]
  for i in range(1, len(input)):
    ans = add_numbers(ans, input[i])
  return ans

def calculate_magnitude(number):
  stack = []
  n = number
  while n is not None:
    if n.val == ']':
      stack.append(stack.pop() * 2 + stack.pop() * 3)
    elif isinstance(n.val, int):
      stack.append(n.val)
    n = n.next
  if len(stack) > 1:
    raise Exception('Invalid stack: ' + str(stack))
  return stack[0]

def solve(input):
  return calculate_magnitude(add_all(input))

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))