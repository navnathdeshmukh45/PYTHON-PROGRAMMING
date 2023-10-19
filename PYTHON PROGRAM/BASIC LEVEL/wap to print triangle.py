def print_triangle(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    try:
        triangle_height = int(input("Enter the height of the triangle: "))
        print_triangle(triangle_height)
    except ValueError:
        print("Error: Please enter a valid integer.")
