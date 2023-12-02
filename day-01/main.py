def numConcat(num1, num2):
  return int("{}{}".format(num1, num2))
  
def calibrate(arr):
  l = 0
  r = len(arr) - 1
  first_digit = float('-inf')
  last_digit = float('-inf')

  while l <= r:
    if arr[l].isdigit() and first_digit <= 0:
      first_digit = int(arr[l])
    elif arr[r].isdigit() and last_digit <= 0:
      last_digit = int(arr[r])
    elif first_digit > 0 and last_digit > 0:
      break
    elif first_digit <= 0:
      l += 1
    else:
      r -= 1
  return numConcat(first_digit,last_digit)

f = open('input.txt', 'r')
lines = f.readlines()

total_sum = 0

for i, line in enumerate(lines):
  total_sum += calibrate(line)

print("part 1 total: {}".format(total_sum))

# part_2

spelled_out_numbers = {"one": "1", 
                       "two": "2", 
                       "three": "3", 
                       "four": "4", 
                       "five": "5", 
                       "six": "6", 
                       "seven": "7", 
                       "eight": "8", 
                       "nine": "9"}

def subsets(elements):
  elements = elements.strip()
  if not elements:
    return 0
    
  l = 0
  r = 1

  subs = []

  # TODO: check for optimization here...
  for i in range(len(elements)):
   for j in range(i + 1, len(elements) + 1):
      sub = elements[i:j]
      if sub in spelled_out_numbers.keys():
        subs.append(spelled_out_numbers[sub])
      else:
        subs.append(sub) 
  
  return subs
  

f = open('input.txt', 'r')
lines = f.readlines()

total_sum = 0

for i, line in enumerate(lines):
  subset_result = subsets(line)
  res = calibrate(subset_result)
  if res is not None:
    total_sum += res
print("part 2 total: {}".format(total_sum))