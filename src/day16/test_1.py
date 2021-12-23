import unittest
from .solution_1 import parse_packet, solve

class TestSolution(unittest.TestCase):
  def test_parse_packet_1(self):
    inp = 'D2FE28'
    act = parse_packet(inp)
    self.assertEqual(act.version, 6)
    self.assertEqual(act.value, 2021)

  def test_solve_1(self):
    inp = '8A004A801A8002F478'
    exp = 16
    act = solve(inp)
    self.assertEqual(exp, act)

  def test_solve_2(self):
    inp = '620080001611562C8802118E34'
    exp = 12
    act = solve(inp)
    self.assertEqual(exp, act)

  def test_solve_3(self):
    inp = 'C0015000016115A2E0802F182340'
    exp = 23
    act = solve(inp)
    self.assertEqual(exp, act)

  def test_solve_4(self):
    inp = 'A0016C880162017C3686B18A3D4780'
    exp = 31
    act = solve(inp)
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()