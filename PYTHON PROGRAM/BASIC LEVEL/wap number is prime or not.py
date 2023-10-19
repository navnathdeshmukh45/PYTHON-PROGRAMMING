import math

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    max_divisor = int(math.sqrt(number)) + 1
    for divisor in range(3, max_divisor, 2):
        if number % divisor == 0:
            return False

    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
    except ValueError:
        print("Error: Please enter a valid integer.")
