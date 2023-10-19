# wap to print factorial of list
a=[]
fa=[]
c="y"
while c=="y" or c=="Y":
    item=int(input("Enter the element of list :"))
    a.append(item)
    c=input("do you want to enter more element")
    print("the list is :",a)
    for i in a :
        f=1
        for j in range(1,i+1):
            f=f*j
fa.append(f)
print("the factorial of each element  is :",F)