# wap  to find number is even or odd
a=int(input("Enter the number is :"))
r=a%2
if r == 0:
 print("even",a)
elif r>0:
    print("odd",a)
else:
    print("you enter number 0 or less than 1 ")