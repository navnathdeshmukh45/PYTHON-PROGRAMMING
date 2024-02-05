# wap to find given number is prime or not 
n=int(input("Enter the number :"))
l=int(n/2)+1
for i in range(2,l):
    r=n%i
    if r==0:
        print("not prime",n)
    else:
        print("nos is prime",n)
