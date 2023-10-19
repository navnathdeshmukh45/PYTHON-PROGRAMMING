# wap  greatest number in four number
a=input("Enter first number :")
b=input("Enter second number :")
c=input("Enter third number :")
d=input("Enter four number :")
if (a>b and a<c and a>d):
    print("greatest number is ",a)
elif (b>c and  b>d):
 print("greatest number is ",b)
elif(c>d):
  print("greatest number is ",c)
elif(d>c):
  print("greatest number is ",d)
else:
    print(" not match")