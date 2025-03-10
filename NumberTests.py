#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p == 2:
    return True
  if isEven(p):
    return False
  
  for div in range(3, p // 2, 2):
    if p % div == 0:
      return False
  
  return True

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

def find_10001st_prime():
  count = 0
  num = 2

  while count < 10001:
    if isPrime(num):
      count += 1
    num += 1
  
  return num - 1

def sum_of_primes(limit):
  print(f"Staring summation of primes up to 2000000...")
  total = 0
  for num in range(2, limit):
    if isPrime(num):
      total += num
  return total

#Test your new functions in this main
def main():
  #knownPrimes = [3, 7, 11, 13, 17]

  #num = int(input("Enter a number: "))

  #if isPrime(num):
    #print("%d is a prime number" %(num))

  #if isEven(num):
    #print("%d is an even number" %(num))

  #result = find_10001st_prime()
  #print(result)

  result = sum_of_primes(2000000)
  print(result)
if __name__ == '__main__':
    main()
