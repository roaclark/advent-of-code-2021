import os
import unittest
from .solution_1 import solution, parse_input

class TestSolution(unittest.TestCase):
  def test_parse_input(self):
    exp = 100
    _, boards = parse_input(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(len(boards), 3)
    self.assertEqual(len(boards[0]), 5)
    self.assertEqual(len(boards[0][0]), 5)
    self.assertEqual(boards[0], [
      [22, 13, 17, 11,  0],
      [ 8,  2, 23,  4, 24],
      [21,  9, 14, 16,  7],
      [ 6, 10,  3, 18,  5],
      [ 1, 12, 20, 15, 19],
    ])

  def test_solution(self):
    exp = 4512
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()