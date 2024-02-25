def reverse_number(number):
    reversed_num = 0
    while number > 0:
        remainder = number % 10
        reversed_num = reversed_num * 10 + remainder
        number //= 10
    return reversed_num

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        reversed_num = reverse_number(num)
        print("Reversed number:", reversed_num)
    except ValueError:
        print("Error: Please enter a valid integer.")