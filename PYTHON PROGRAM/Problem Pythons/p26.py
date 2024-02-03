# wap  to print opposite right angle triangle 
n=int(input("enter the number rows:"))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*" ,end="")
    print()