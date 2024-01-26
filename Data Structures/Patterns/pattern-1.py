# This is pattern 1
# Input: N = 5
# Output:
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

n = int(input("Enter the value:"))
for i in range(n):
  for j in range(n):
     print("*",end=" ")
  print("")
