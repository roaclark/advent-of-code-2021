from io import TextIOWrapper


def get_file_lines(file: TextIOWrapper):
  return [s.strip() for s in file.read().strip().split('\n')]