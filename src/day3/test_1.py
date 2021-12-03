import os
import unittest
from .solution_1 import solution, parse_input, sum_bits

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 198
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

  def test_sum_bits(self):
    exp = [7, 5, 8, 7, 5]
    act = sum_bits(parse_input(os.path.join(os.path.dirname(__file__), 'test_input.txt')))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()