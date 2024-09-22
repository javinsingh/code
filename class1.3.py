num = int(input("enter a number"))
sum = 0
temp = num
while temp > 0:
  digit = temp %10
  sum += digit**3
  temp //=10
if num == sum:
   print("this is a armstong number")
else:
   print("this is not an armstrong number")