# wap to print fibonacci series use for  loop
a = eval(input("Enter the range is :"))
f=0
s=1
for a in range(0,a):
    if(a<=1):
        n=a
    else:
        n = f + s
        f = s
        s = n
        print(n)
    