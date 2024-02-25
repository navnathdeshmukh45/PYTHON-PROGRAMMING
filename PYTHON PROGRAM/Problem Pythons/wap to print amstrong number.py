def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit)**num_digits for digit in num_str)
    return number == total

def print_armstrong_numbers(start, end):
    print(f"Armstrong numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            print(num)

if __name__ == "__main__":
    try:
        start_range = int(input("Enter the start of the range: "))
        end_range = int(input("Enter the end of the range: "))
        print_armstrong_numbers(start_range, end_range)
    except ValueError:
        print("Error: Please enter valid integers for the range.")
