num_rows = int(input("Enter the number of rows in the pyramid: "))

for i in range(num_rows):
    # print spaces before the first star in each row
    for j in range(num_rows-i-1):
        print(" ", end="")
    
    # print stars for this row
    for j in range(2*i+1):
        print("*", end="")
    
    # move to the next row
    print()
