import os
import unittest
from .solution_1 import solution, solve

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 5934
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()