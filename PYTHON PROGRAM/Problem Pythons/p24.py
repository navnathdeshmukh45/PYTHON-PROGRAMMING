# wap to check the value  of factorial
a = int(input("enter a number :"))
f=1
if a<0:
    print("negative  number is invalid")
elif a==0:
    print(" factorial of 0 is 1")
else:
    for i in range(1,a+1):
        f=f*i
        print("the factorial of ",a,"is",f)