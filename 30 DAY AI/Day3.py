print("Hello Sir")
# Variable --> store data
x = 5
print(x)
# Operators
# program arithmatic operator
a=45
b=34
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
# program on relational op
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
#bitwise op
print(a&b)
print(a|b)
print(a^b)
print(~b)
print(a<<b)
print(a>>b)

#assignment op
x=10
x+=0
print(x)
x-=20
print(x)
x*=10
print(x)
x/=10
print(x)

#ternary op
y= input("Enter the value y")
z=input("Enter the value z")
min =y if y<z else z
print("minmum  value :",min)

# String
string =" Welcome to python programming "
str =""
print(string)
print(string[0:10])

# list
a = ["is",45,67,78]
b = "nice"
print("boys",a,b)

# 
dicit={"math":90,"phy":90}
print(dicit)

set ={90,99,98,97}
print(set)

tuple=(99,90,98,89,87)
print(tuple)

#function
def sum(a,b):
   print(3,4)
  
sum(3,6)

# condition
a= input("Enter the name :")
if a=="ram":
    print("good moring ram sir")
else:
    print("good moring guest")

#loop 
for a in range(1,4):
 print(a)
 #for loop

# for i in range(7):
#     print(i)
#     i=i+1
#     continue
#     break

i=1
while(i<=5):
    print(i)
    i=i+1
