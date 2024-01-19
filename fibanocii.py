# Fibanocii series : 1,1,2,3,5,8..... ->We obtain this series by following this if you want third number we add first and second number.

#Using Brute Force

def fibanocii(n):
  if n == 1 or n == 2:
    return 1
  else:
    result =  fibanocii(n-1) + fibanocii(n-2)
  return result

n = int(input("Enter number"))
print(fibanocii(n))


# Using Dynamic Programming with the help of memoization
# memoization -> The process of storing the result and using it later.This way the process of calaculating the result can be reduced.

def fibanocii(n,mem):

  if mem[n] is not None:
    return mem[n]

  if n == 1 or n == 2:
    return 1
  else:
    result =  fibanocii(n-1,mem) + fibanocii(n-2,mem)
    mem[n] = result

  return result

n = int(input("Enter number"))
mem = [None] * (n+1)
print(fibanocii(n,mem))
