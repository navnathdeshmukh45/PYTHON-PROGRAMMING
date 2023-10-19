def convert_to_uppercase(input_string):
    return input_string.upper()

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    uppercased_string = convert_to_uppercase(input_string)
    print("Uppercase string:", uppercased_string)
