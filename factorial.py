def calculate_factorial():

  num = int(input("input a number: "))
  factorial = 1
 

  if num < 0:
   print("error")
  elif num == 0:
   print("the factorial of 0 is 1")
  else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("%d is the factorial of %d" %(factorial,num))
calculate_factorial()