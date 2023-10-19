def calculate_love_percentage(name1, name2):
    combined_names = (name1 + name2).lower().replace(" ", "")
    love_score = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")
    return love_score

if __name__ == "__main__":
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    love_percentage = calculate_love_percentage(name1, name2)
    print(f"Love Percentage: {love_percentage}%")
