def check_substring(string, substring):
    if substring in string:
        return True
    else:
        return False

# Example usage
string = "Hello, world!"
substring = "world"
result = check_substring(string, substring)
print(result)
