import re

def main():
  cards = {}

  with open('input.txt', 'r') as f:
    lines = f.readlines()

  card_count = [1] * len(lines)
  for row, line in enumerate(lines):
    matched_nums = []
    nums_to_match = set()
    card_re = re.compile(r'Card\s+(\d+):')
    card_num = card_re.search(line)

    n = int(card_num.group(1))

    winning_nums, card_nums = line.split(":")[1].split(" | ")
    {nums_to_match.add(int(num)) for num in winning_nums.split()}
    
    for num in card_nums.split():
      if int(num) in nums_to_match:
        matched_nums.append(int(num))
    cards[n] = len(matched_nums)

    for i in range(cards[n]):
      card_count[row + i + 1] +=  card_count[row]
      
  return sum(card_count)

if __name__ == "__main__":
  res = main()
  print(res)