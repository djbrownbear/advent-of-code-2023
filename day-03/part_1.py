import re
from string import punctuation

def is_valid(pos, h, l):
  row, col = pos
  return 0 <= row <= h and 0 <= col <= l

def generate_moves(pos, h, l):
  row, col = pos

  possible_moves = [
  (row, col),
  (row, col + 1),
  (row, col - 1),
  (row + 1, col),
  (row - 1, col),

  (row + 1, col + 1),
  (row + 1, col - 1),

  (row - 1, col + 1),
  (row - 1, col - 1),
]
  
  return { move for move in possible_moves if is_valid(move, h, l) }

def find_symbols(row, arr, all_moves, h, l):  
  for col, el in enumerate(arr):
    if el in SYMBOLS:
      for move in generate_moves((row, col), h, l):
        all_moves.add(move)

SYMBOLS = punctuation.replace(".", "")

def main():
  with open('input.txt', 'r') as f:
    lines = f.readlines()

  h,l = len(lines), len(lines[0])

  all_moves = set()
  nums_to_sum = {}

  print("h: {}, l: {}".format(h, l))

  for row, line in enumerate(lines):
    find_symbols(row, line, all_moves, h, l)

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
        if pos in all_moves:
          nums_to_sum[(row, start_idx, end_idx)] = int(num)

  print(sum(nums_to_sum.values()))

if __name__ == "__main__":
  main()