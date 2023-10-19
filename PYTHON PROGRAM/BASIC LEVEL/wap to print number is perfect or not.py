def is_perfect_number(number):
    if number <= 0:
        return False

    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor

    return sum_of_divisors == number

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if is_perfect_number(num):
            print(num, "is a perfect number.")
        else:
            print(num, "is not a perfect number.")
    except ValueError:
        print("Error: Please enter a valid integer.")
