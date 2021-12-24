import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input(filepath):
  with open(filepath, 'r') as f:
    x_str, y_str = f.readline()[13:].split(', ')
    x = tuple(sorted(int(v) for v in x_str[2:].split('..')))
    y = tuple(sorted(int(v) for v in y_str[2:].split('..')))
    return x, y
  
def hits_range(goal_x, goal_y, start_vel_x, start_vel_y):
  goal_x_min, goal_x_max = goal_x
  goal_y_min, goal_y_max = goal_y
  loc_x = 0
  loc_y = 0
  vel_y = start_vel_y
  vel_x = start_vel_x
  while loc_x <= goal_x_max and loc_y >= goal_y_min:
    loc_x += vel_x
    loc_y += vel_y
    vel_y -= 1
    vel_x = max(0, vel_x - 1)
    if loc_x >= goal_x_min and loc_x <= goal_x_max and loc_y >= goal_y_min and loc_y <= goal_y_max:
      return True
  return False

def max_height(vel_y):
  return int((vel_y + 1) * vel_y / 2)

def solve(input):
  goal_x, goal_y = input
  for vel_y in range(-goal_y[0]+1, 0, -1):
    for vel_x in range(goal_x[1]+1):
      if hits_range(goal_x, goal_y, vel_x, vel_y):
        return max_height(vel_y)
  return None

def solution(filepath):
  input = parse_input(filepath)
  return solve(input)

if __name__ == '__main__':
  print(solution(input_path))