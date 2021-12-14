import os
import unittest
from .solution_2 import solution, solve

class TestSolution(unittest.TestCase):
  def test_solution_1(self):
    exp = 36
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_1.txt'))
    self.assertEqual(exp, act)

  def test_solution_2(self):
    exp = 103
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_2.txt'))
    self.assertEqual(exp, act)

  def test_solution_3(self):
    exp = 3509
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input_3.txt'))
    self.assertEqual(exp, act)

  def test_solve_1(self):
    exp = 1
    input = {
      'start': ['end'],
      'end': ['start'],
    }
    act = solve(input)
    self.assertEqual(exp, act)

  def test_solve_2(self):
    exp = 2
    input = {
      'start': ['b'],
      'b': ['start', 'd', 'end'],
      'd': ['b'],
      'end': ['b'],
    }
    act = solve(input)
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()