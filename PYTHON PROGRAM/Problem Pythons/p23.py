# wap sum of nth number 
n=int(input("Enter the limit "))
s=0
for c in range(1,n):
    s=c+s
    print("the sum is",s)