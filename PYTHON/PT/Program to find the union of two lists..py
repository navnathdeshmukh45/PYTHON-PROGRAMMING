list1 = []
list2 = []
len1 = int(input("Enter Length of List 1:"))
for i in range(len1):
    el1 = int(input("Enter Element:"))
    list1.append(el1)
print("List A:",list1)
len2 = int(input("Enter Length of List 2:"))
for i in range(len2):
    el2 = int(input("Enter Element:"))
    list2.append(el2)
print("List B:",list2)
unionList = list(set().union(list1,list2))
print("---------------------")
print("List A:",list1)
print("List B:",list2)
print("A U B:",unionList)
