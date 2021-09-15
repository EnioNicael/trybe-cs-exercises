# Calcule a média aritmética dos valores contidos em uma lista

def calculate_average ():
  numbers = [4, 8, 5, 7]
  sum_numbers = 0

  for number in numbers:
    sum_numbers += number

  average = sum_numbers // len(numbers)

  return average


print(calculate_average())