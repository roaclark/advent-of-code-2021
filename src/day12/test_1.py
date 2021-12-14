import os
import unittest
from .solution_1 import solution

class TestSolution(unittest.TestCase):
  def test_solution_1(self):
    exp = 10
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_1.txt'))
    self.assertEqual(exp, act)

  def test_solution_2(self):
    exp = 19
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_2.txt'))
    self.assertEqual(exp, act)

  def test_solution_3(self):
    exp = 226
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_3.txt'))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()