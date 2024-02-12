n = int(input("Enter the Value"))
i = 0 

while(i < n):
    j = 0
    while(j < n):      
        j = j + 1
        print('*', end="")
    i = i + 1
    print('')

# output
# *******
# *******
# *******
# *******
# *******
# *******
# *******
    
# ======================================
    
# output
# 1111111
# 2222222
# 3333333
# 4444444
# 5555555
# 6666666
# 7777777 
i = 1 

while(i < n+1):
    j = 0
    while(j < n):      
        j = j + 1
        print(i, end="")
    i = i + 1
    print('')