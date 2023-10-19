def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if is_even(num):
            print(num, "is even.")
        else:
            print(num, "is not even.")
    except ValueError:
        print("Error: Please enter a valid integer.")
