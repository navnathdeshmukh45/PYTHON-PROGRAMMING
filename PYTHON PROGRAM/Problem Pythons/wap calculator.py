# a = 50
# b = 3

# print("The value of", a, "+", 3, "is: ", a + b)
# print("The value of", a, "-", 3, "is: ", a - b)
# print("The value of", a, "*", 3, "is: ", a * b)
# print("The value of", a, "/", 3, "is: ", a / b)

# 

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y
print("Welcome to the Basic Calculator!")
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator.")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))

