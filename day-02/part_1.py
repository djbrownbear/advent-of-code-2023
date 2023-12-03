import re

f = open('input.txt', 'r')
lines = f.readlines()

game_num = r'Game (\d+):'
game_set = r'(\d+) (\w+)' # tested on https://pythex.org/

all_games = {}

cubes = {"red": 12, "green": 13, "blue": 14}

for line in lines:
 gid_pattern = re.compile(game_num)
 gid = int(gid_pattern.findall(line)[0])
 all_games[gid] = gid

 pattern = re.compile(game_set)
 cur_max = {"red": 0, "green": 0, "blue": 0}

 for num, color in pattern.findall(line):
  cur_max[color] = max(cur_max[color], int(num))

  if cur_max[color] > cubes[color]: # check for impossible game
   all_games[gid] = 0

print(sum(all_games.values())) 

