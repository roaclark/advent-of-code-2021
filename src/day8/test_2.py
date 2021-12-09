import os
import unittest
from .solution_2 import solution, parse_input, get_output_number, solve_line, get_segment_map

class TestSolution(unittest.TestCase):
  def test_solution(self):
    exp = 61229
    act = solution(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

  def test_parse(self):
    exp = [
      [['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb'], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']],
      [['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf', 'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec'], ['fcgedb', 'cgb', 'dgebacf', 'gc']],
      [['fgaebd', 'cg', 'bdaec', 'gdafb', 'agbcfd', 'gdcbef', 'bgcad', 'gfac', 'gcb', 'cdgabef'], ['cg', 'cg', 'fdcagb', 'cbg']],
      [['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega'], ['efabcd', 'cedba', 'gadfec', 'cb']],
      [['aecbfdg', 'fbg', 'gf', 'bafeg', 'dbefa', 'fcge', 'gcbea', 'fcaegb', 'dgceab', 'fcbdga'], ['gecf', 'egdcabf', 'bgf', 'bfgea']],
      [['fgeab', 'ca', 'afcebg', 'bdacfeg', 'cfaedg', 'gcfdb', 'baec', 'bfadeg', 'bafgc', 'acf'], ['gebdcfa', 'ecba', 'ca', 'fadegcb']],
      [['dbcfg', 'fgd', 'bdegcaf', 'fgec', 'aegbdf', 'ecdfab', 'fbedc', 'dacgb', 'gdcebf', 'gf'], ['cefg', 'dcbef', 'fcge', 'gbcadfe']],
      [['bdfegc', 'cbegaf', 'gecbf', 'dfcage', 'bdacg', 'ed', 'bedf', 'ced', 'adcbefg', 'gebcd'], ['ed', 'bcgafe', 'cdgba', 'cbgef']],
      [['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg'], ['gbdfcae', 'bgc', 'cg', 'cgb']],
      [['gcafb', 'gcf', 'dcaebfg', 'ecagb', 'gf', 'abcdeg', 'gaef', 'cafbge', 'fdbac', 'fegbdc'], ['fgae', 'cfgab', 'fg', 'bagce']],
    ]
    act = parse_input(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    self.assertEqual(exp, act)

  def test_get_output_number(self):
    exp = 5353
    segment_map = {
      'd': 'a',
      'e': 'b',
      'a': 'c',
      'f': 'd',
      'g': 'e',
      'b': 'f',
      'c': 'g',
    }
    output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
    act = get_output_number(segment_map, output)
    self.assertEqual(exp, act)

  def test_solve_line(self):
    exp = 5353
    act = solve_line([
      ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'],
      ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'],
    ])
    self.assertEqual(exp, act)

  def test_get_segment_map(self):
    exp = {
      'd': 'a',
      'e': 'b',
      'a': 'c',
      'f': 'd',
      'g': 'e',
      'b': 'f',
      'c': 'g',
    }
    act = get_segment_map(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'])
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()
