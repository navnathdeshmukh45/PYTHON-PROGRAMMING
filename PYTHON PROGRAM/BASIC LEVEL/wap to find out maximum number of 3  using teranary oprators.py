def find_max_using_ternary(a, b, c):
    max_number = a if a > b and a > c else (b if b > c else c)
    return max_number

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
        result = find_max_using_ternary(num1, num2, num3)
        print("The maximum number is:", result)
    except ValueError:
        print("Error: Please enter valid integers for all three numbers.")
