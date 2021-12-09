from io import TextIOWrapper

def get_file_lines(file: TextIOWrapper):
  return file.read().splitlines()