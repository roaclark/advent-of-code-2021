import unittest
from .solution_2 import solve

class TestSolution(unittest.TestCase):
  def test_solve_1(self):
    inp = 'C200B40A82'
    exp = 3
    act = solve(inp)
    self.assertEqual(exp, act)

  def test_solve_2(self):
    inp = '04005AC33890'
    exp = 54
    act = solve(inp)
    self.assertEqual(exp, act)

  def test_solve_3(self):
    inp = '880086C3E88112'
    exp = 7
    act = solve(inp)
    self.assertEqual(exp, act)

  def test_solve_4(self):
    inp = 'CE00C43D881120'
    exp = 9
    act = solve(inp)

  def test_solve_5(self):
    inp = 'D8005AC2A8F0'
    exp = 1
    act = solve(inp)

  def test_solve_6(self):
    inp = 'F600BC2D8F'
    exp = 0
    act = solve(inp)

  def test_solve_7(self):
    inp = '9C005AC2F8F0'
    exp = 0
    act = solve(inp)

  def test_solve_8(self):
    inp = '9C0141080250320F1802104A08'
    exp = 1
    act = solve(inp)
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()