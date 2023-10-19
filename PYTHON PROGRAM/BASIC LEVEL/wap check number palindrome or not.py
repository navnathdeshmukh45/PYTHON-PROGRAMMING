def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder
        number //= 10

    return original_number == reversed_number

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if is_palindrome(num):
            print(num, "is a palindrome.")
        else:
            print(num, "is not a palindrome.")
    except ValueError:
        print("Error: Please enter a valid integer.")
