import os
import unittest
from .solution_2 import expand_grid, solution

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 315
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

  def test_expand_grid_1(self):
    inp = [
      [1,2],
      [3,4],
    ]
    exp = [
      [1,2,2,3],
      [3,4,4,5],
      [2,3,3,4],
      [4,5,5,6],
    ]
    act = expand_grid(inp, 2)
    self.assertEqual(exp, act)

  def test_expand_grid_2(self):
    inp = [
      [1,9],
      [3,4],
    ]
    exp = [
      [1,9,2,1],
      [3,4,4,5],
      [2,1,3,2],
      [4,5,5,6],
    ]
    act = expand_grid(inp, 2)
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()