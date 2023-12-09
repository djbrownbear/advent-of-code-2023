import re

def calculate_score(matched_nums, score):
  if len(matched_nums) == 0:
    return 0
  if len(matched_nums) == 1:
    return 1
  elif len(matched_nums) >= 2:
    for i in range(len(matched_nums)):
      if i == 0:
        score += 1
      else:
        score = score * 2  
  return score

def main():
  total_score = 0

  with open('input.txt', 'r') as f:
    lines = f.readlines()

  for row, line in enumerate(lines):
    score = 0
    matched_nums = []
    nums_to_match = set()
    card_re = re.compile(r'Card (\d+):')
    card_num = card_re.search(line)

    winning_nums, card_nums = line.split(":")[1].split(" | ")
    {nums_to_match.add(int(num)) for num in winning_nums.split()}
    
    for n in card_nums.split():
      if int(n) in nums_to_match:
        matched_nums.append(int(n))
    
    score = calculate_score(matched_nums, score)
    total_score += score
  return total_score

if __name__ == "__main__":
  res = main()
  print(f"total score is: {res}")