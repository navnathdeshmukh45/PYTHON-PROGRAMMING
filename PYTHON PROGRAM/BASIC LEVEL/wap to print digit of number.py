def print_digits_of_number(number):
    num_str = str(number)
    for digit_char in num_str:
        print(int(digit_char))

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print("Digits of the number:")
        print_digits_of_number(num)
    except ValueError:
        print("Error: Please enter a valid integer.")
