def print_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        table_limit = int(input("Enter the table limit: "))
        print_table(num, table_limit)
    except ValueError:
        print("Error: Please enter a valid integer.")
