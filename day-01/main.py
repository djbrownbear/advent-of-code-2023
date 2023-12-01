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
    elif first_digit <= 0:
      l += 1
    else:
      r -= 1
  print("first_digit: {}, last_digit: {}".format(first_digit, last_digit))
  return numConcat(first_digit,last_digit)

f = open('input.txt', 'r')
lines = f.readlines()

total_sum = 0

for i, line in enumerate(lines):
  # print("line #: {}".format(i))
  total_sum += calibrate(line)

print(total_sum)
