# wap to print pascal triangle 
n =int(input("Enter the rows :"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end="")
        for j in range(0,i+1):
            print("*",end="")
        print()