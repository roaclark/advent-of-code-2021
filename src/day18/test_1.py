import os
import unittest
from .solution_1 import parse_input, add_all, add_numbers, attempt_to_explode_pair, calculate_magnitude, reduce_number, solution, parse_number, stringify_number

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 4140
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

  def test_parse_number(self):
    inp = '[[[[1,2],[3,4]],[[5,6],[7,8]]],9]'
    node = parse_number(inp)
    self.assertEqual(node.val, '[')
    node = node.next
    self.assertEqual(node.val, '[')
    node = node.next
    self.assertEqual(node.val, '[')
    node = node.next
    self.assertEqual(node.val, '[')
    node = node.next
    self.assertEqual(node.val, 1)
    node = node.next
    self.assertEqual(node.val, 2)
    node = node.next
    self.assertEqual(node.val, ']')
    node = node.next
    self.assertEqual(node.val, '[')
    node = node.next
    self.assertEqual(node.val, 3)
    node = node.next
    self.assertEqual(node.val, 4)
    node = node.next
    self.assertEqual(node.val, ']')
    node = node.next
    self.assertEqual(node.val, ']')
    node = node.next
    self.assertEqual(node.val, '[')
    node = node.next
    self.assertEqual(node.val, '[')
    node = node.next
    self.assertEqual(node.val, 5)
    node = node.next
    self.assertEqual(node.val, 6)
    node = node.next
    self.assertEqual(node.val, ']')
    node = node.next
    self.assertEqual(node.val, '[')
    node = node.next
    self.assertEqual(node.val, 7)
    node = node.next
    self.assertEqual(node.val, 8)
    node = node.next
    self.assertEqual(node.val, ']')
    node = node.next
    self.assertEqual(node.val, ']')
    node = node.next
    self.assertEqual(node.val, ']')
    node = node.next
    self.assertEqual(node.val, 9)
    node = node.next
    self.assertEqual(node.val, ']')
    node = node.next
    self.assertIsNone(node)

  def test_attempt_to_explode_pair_1(self):
    num = parse_number('[[[[[9,8],1],2],3],4]')
    did_explode = attempt_to_explode_pair(num)
    exploded = stringify_number(num)
    self.assertTrue(did_explode)
    self.assertEqual(exploded, '[[[[0,9],2],3],4]')

  def test_attempt_to_explode_pair_2(self):
    num = parse_number('[7,[6,[5,[4,[3,2]]]]]')
    did_explode = attempt_to_explode_pair(num)
    exploded = stringify_number(num)
    self.assertTrue(did_explode)
    self.assertEqual(exploded, '[7,[6,[5,[7,0]]]]')

  def test_attempt_to_explode_pair_3(self):
    num = parse_number('[[6,[5,[4,[3,2]]]],1]')
    did_explode = attempt_to_explode_pair(num)
    exploded = stringify_number(num)
    self.assertTrue(did_explode)
    self.assertEqual(exploded, '[[6,[5,[7,0]]],3]')

  def test_attempt_to_explode_pair_4(self):
    num = parse_number('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    did_explode = attempt_to_explode_pair(num)
    exploded = stringify_number(num)
    self.assertTrue(did_explode)
    self.assertEqual(exploded, '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')

  def test_attempt_to_explode_pair_5(self):
    num = parse_number('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
    did_explode = attempt_to_explode_pair(num)
    exploded = stringify_number(num)
    self.assertTrue(did_explode)
    self.assertEqual(exploded, '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')

  def test_reduce_1(self):
    inp = parse_number('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
    exp = '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
    act = stringify_number(reduce_number(inp))
    self.assertEqual(act, exp)

  def test_add_numbers_1(self):
    inp_a = parse_number('[[[[4,3],4],4],[7,[[8,4],9]]]')
    inp_b = parse_number('[1,1]')
    exp = '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
    act = stringify_number(add_numbers(inp_a, inp_b))
    self.assertEqual(act, exp)

  def test_add_all_1(self):
    inp = [parse_number(x) for x in [
      '[1,1]',
      '[2,2]',
      '[3,3]',
      '[4,4]',
    ]]
    exp = '[[[[1,1],[2,2]],[3,3]],[4,4]]'
    act = stringify_number(add_all(inp))
    self.assertEqual(act, exp)

  def test_add_all_2(self):
    inp = [parse_number(x) for x in [
      '[1,1]',
      '[2,2]',
      '[3,3]',
      '[4,4]',
      '[5,5]',
    ]]
    exp = '[[[[3,0],[5,3]],[4,4]],[5,5]]'
    act = stringify_number(add_all(inp))
    self.assertEqual(act, exp)

  def test_add_all_3(self):
    inp = [parse_number(x) for x in [
      '[1,1]',
      '[2,2]',
      '[3,3]',
      '[4,4]',
      '[5,5]',
      '[6,6]',
    ]]
    exp = '[[[[5,0],[7,4]],[5,5]],[6,6]]'
    act = stringify_number(add_all(inp))
    self.assertEqual(act, exp)

  def test_add_all_4(self):
    inp = [parse_number(x) for x in [
      '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
      '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
      '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
      '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
      '[7,[5,[[3,8],[1,4]]]]',
      '[[2,[2,2]],[8,[8,1]]]',
      '[2,9]',
      '[1,[[[9,3],9],[[9,0],[0,7]]]]',
      '[[[5,[7,4]],7],1]',
      '[[[[4,2],2],6],[8,7]]',
    ]]
    exp = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
    act = stringify_number(add_all(inp))
    self.assertEqual(act, exp)
  
  def test_calculate_magnitude_1(self):
    inp = '[9,1]'
    exp = 29
    act = calculate_magnitude(parse_number(inp))
    self.assertEqual(exp, act)
  
  def test_calculate_magnitude_2(self):
    inp = '[1,9]'
    exp = 21
    act = calculate_magnitude(parse_number(inp))
    self.assertEqual(exp, act)
  
  def test_calculate_magnitude_3(self):
    inp = '[[9,1],[1,9]]'
    exp = 129
    act = calculate_magnitude(parse_number(inp))
    self.assertEqual(exp, act)
  
  def test_calculate_magnitude_4(self):
    inp = '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
    exp = 4140
    act = calculate_magnitude(parse_number(inp))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()