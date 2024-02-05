# wap to print pattern a ab,abc...
ch=str(input("enter  a character:"))
a =  ord(ch)
for x in range(65,a+1):
    for ch in range(65,x+1):
        print(chr(ch),end="")
        print("")