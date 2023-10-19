def square_using_operator(number):
    return number ** 2

def square_using_pow_function(number):
    return pow(number, 2)

if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))  # We use float to handle both integers and decimals.
        print("Square using operator:", square_using_operator(num))
        print("Square using pow function:", square_using_pow_function(num))
    except ValueError:
        print("Error: Please enter a valid number.")
