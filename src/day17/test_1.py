import os
import unittest
from .solution_1 import solution, parse_input, hits_range

class TestSolution(unittest.TestCase):
  def test_parse_input(self):
    exp = ((20, 30), (-10, -5))
    act = parse_input(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

  def test_hits_range_1(self):
    goal_x = (20, 30)
    goal_y = (-10, -5)
    vel_x = 7
    vel_y = 2
    exp = True
    act = hits_range(goal_x, goal_y, vel_x, vel_y)
    self.assertEqual(exp, act)

  def test_hits_range_2(self):
    goal_x = (20, 30)
    goal_y = (-10, -5)
    vel_x = 6
    vel_y = 0
    exp = True
    act = hits_range(goal_x, goal_y, vel_x, vel_y)
    self.assertEqual(exp, act)

  def test_hits_range_3(self):
    goal_x = (20, 30)
    goal_y = (-10, -5)
    vel_x = 7
    vel_y = -1
    exp = True
    act = hits_range(goal_x, goal_y, vel_x, vel_y)
    self.assertEqual(exp, act)

  def test_solution(self):
    exp = 45
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()