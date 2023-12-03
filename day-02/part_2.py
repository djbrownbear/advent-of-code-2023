import re
import math

f = open('input.txt', 'r')
lines = f.readlines()

game_num = r'Game (\d+):'
game_set = r'(\d+) (\w+)'

all_games = {}

for line in lines:
 gid_pattern = re.compile(game_num)
 gid = int(gid_pattern.findall(line)[0])

 pattern = re.compile(game_set)
 cur_max = {"red": 0, "green": 0, "blue": 0}

 # find the fewest of each color to make the game possible
 for num, color in pattern.findall(line):
  cur_max[color] = max(cur_max[color], int(num))

 all_games[gid] = math.prod(cur_max.values())

print(sum(all_games.values()))

