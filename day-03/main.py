import re
from string import punctuation

OFFSETS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def is_valid(pos, h, l):
  row, col = pos
  return 0 <= row <= h and 0 <= col <= l

def generate_moves(pos, h, l):
  row, col = pos
  possible_moves = [
    (row + offset[0], col + offset[1]) for offset in OFFSETS
  ]

  return { move for move in possible_moves if is_valid(move, h, l) }

def find_symbols(row, arr, all_moves, h, l, symbols, symbol_locations, lines):  
  for col, el in enumerate(arr):
    if el in symbols:
      symbol_locations[(row, col)] = el
      for move in generate_moves((row, col), h, l):
        r, c = move
        all_moves.add(move) if lines[r][c].isdigit() else None

SYMBOLS = punctuation.replace(".", "")
GEARS = '*'

def main(part):
  if part == 1:
    symbols = SYMBOLS
  elif part == 2:
    symbols = GEARS
  
  with open('input.txt', 'r') as f:
    lines = f.readlines()

  h,l = len(lines), len(lines[0])

  symbol_locations = {}
  all_moves = set()
  nums_to_sum = {}

  for row, line in enumerate(lines):
    find_symbols(row, line, all_moves, h, l, symbols, symbol_locations, lines)

  num_pattern = r'(\d+)'

  for row, line in enumerate(lines):
    find_num = re.compile(num_pattern)
    start_idx = -1

    for match in find_num.finditer(line):
      num = match.group()
      start_idx = match.start()
      end_idx = match.end() - 1

      for i in range(start_idx, end_idx + 1):
          pos = (row, i)
          if part == 1:
            if pos in all_moves:
                nums_to_sum[(row, start_idx)] = int(num)
          if part == 2:
            if pos in all_moves and pos not in nums_to_sum:
                nums_to_sum[pos] = int(num)
  
  if part == 1:
    print("Sum of valid numbers is: ", sum(nums_to_sum.values()))
  elif part == 2:
    gear_ratios = set()
    
    for (row, col) in symbol_locations:
      adjacent_nums = [
        nums_to_sum.get((row + offset[0], col + offset[1])) for offset in OFFSETS
      ]

      adjacent_nums = set(num for num in adjacent_nums if num is not None)

      if len(adjacent_nums) == 2:
        gear_ratio = adjacent_nums.pop() * adjacent_nums.pop()
        gear_ratios.add(gear_ratio)
    print("Sum of gear ratios is: ", sum(gear_ratios))

if __name__ == "__main__":
  main(part=1)
  main(part=2)