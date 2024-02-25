import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

if __name__ == "__main__":
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")

    choice = int(input("Enter option number: "))

    if choice in [1, 2, 3, 4, 6]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    elif choice in [5, 7, 8, 9]:
        num = float(input("Enter the number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    elif choice == 5:
        print("Result:", square_root(num))
    elif choice == 6:
        print("Result:", power(num1, num2))
    elif choice == 7:
        print("Result:", sin(num))
    elif choice == 8:
        print("Result:", cos(num))
    elif choice == 9:
        print("Result:", tan(num))
    else:
        print("Invalid option")
