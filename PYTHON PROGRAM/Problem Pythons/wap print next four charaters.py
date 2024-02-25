def print_next_4_characters(input_string):
    current_position = int(input("Enter the starting position: "))
    next_4_characters = input_string[current_position:current_position + 4]
    print("Next 4 characters:", next_4_characters)

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print_next_4_characters(input_string)
