class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def convert_list_to_linkedlist(lis):
  nodes = [Node(val) for val in lis]
  for i in range(0, len(nodes)):
    if i > 0:
      nodes[i].prev = nodes[i-1]
    if i < len(nodes)-1:
      nodes[i].next = nodes[i+1]
  return nodes[0]

def copy_linked_list(lis):
  new_head = Node(lis.val)
  new_curr = new_head
  lis_curr = lis
  while lis_curr.next is not None:
    lis_curr = lis_curr.next
    new_curr.next = Node(lis_curr.val)
    new_curr.next.prev = new_curr
    new_curr = new_curr.next
  return new_head
