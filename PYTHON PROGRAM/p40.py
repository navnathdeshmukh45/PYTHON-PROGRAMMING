# wap in python to create  a phone   dictionary 
n=int(input("Enter the limit :"))
m={}
mob=0
name=""
i=0
for i in range(0,n):
    mob=int(input("Enter the mobile number :"))
    name=str(input("Enter the name: "))
    z=dict({mob:name})
    m.update(z)
    print(m)
    n=int(input("Enter the no to search in dictinarry"))
    print("the name of person is ",m[n])