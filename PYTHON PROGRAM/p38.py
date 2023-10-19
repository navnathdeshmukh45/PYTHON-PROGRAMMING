# wap to create  a list of value input  by the user and sort  increasing order 
a =int(input("Enter the limit:"))
lst=[]
for a in range(1,a+1):
    a=int(input("Enter the element"))
    lst.append(a)
    l=len(lst)
    for i in range(l):
        for j in range(0,l-i-1):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
print("after sorting the list is")
print(lst)