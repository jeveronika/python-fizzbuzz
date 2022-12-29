def fizzbuzz(limit):
  result = []
  for number in range(1, limit+1):
    if number % 5 == 0 and number % 3 == 0:
      result.append("FizzBuzz")
    elif number % 3 == 0:
      result.append("Fizz")
    elif number % 5 == 0:
      result.append("Buzz")
    else:
      result.append(number)
  return result

print(fizzbuzz(100))