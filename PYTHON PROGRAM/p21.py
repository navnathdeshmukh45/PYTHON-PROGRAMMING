# wap to check division in result 
a =eval(input("Enter mark out of 300 :"))
b=a/300*100
print("percentage is ",b,"%")
if(a>300):
    print("you enter wrong mark ")
elif b>60:
    print("your division are first")
elif (b>50 and b<53):
    print("your division are second")
elif(b>33 and b<50):
    print("your division is third")
else:
    print("fail")