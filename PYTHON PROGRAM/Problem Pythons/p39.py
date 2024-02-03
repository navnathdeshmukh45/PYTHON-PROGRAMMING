# sorting  in accending use bubble sort
a=int(input("Enter the limit:"))
l=[]
for  li in range(l,a+1):
    a=int(input("Enter the element"))
    l.append(a)
    print(l)
    l1=len(l)
    for i in range(l1):
        for j in range(0,l-i-1):
            if l[j]>l[j+1]:
             temp =l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            
            print("after sorting the list is ")
            print(l)




