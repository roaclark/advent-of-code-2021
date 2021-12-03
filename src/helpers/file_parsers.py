from io import TextIOWrapper


def get_file_lines(file: TextIOWrapper):
  return file.read().splitlines()

def add_vectors(*vectors):
  return [sum(vals) for vals in zip(*vectors)]