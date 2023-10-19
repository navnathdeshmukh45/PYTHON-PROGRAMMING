# wap to create a tuple of value  input by user
a=()
l=[]
n=int(input("Enter the limit :"))
for  i in range(0,n):
    item=int(input("Enter the element :"))
    l.append(item)
    a=a+tuple(l)
    print("tuple is ",a)