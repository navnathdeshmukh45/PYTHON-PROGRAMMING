def recommend_pet_food(species, age):
    if species.lower() == "dog":
        if age < 2:
            return "Puppy food"
        elif 2 <= age <= 7:
            return "Adult dog food"
        else:
            return "Senior dog food"
    elif species.lower() == "cat":
        if age < 2:
            return "Kitten food"
        elif 2 <= age <= 5:
            return "Adult cat food"
        else:
            return "Senior cat food"
    else:
        return "Sorry, we don't have a specific recommendation for that pet."


pet_species = input("Enter pet species (dog or cat): ")
pet_age = int(input("Enter pet age in years: "))

recommendation = recommend_pet_food(pet_species, pet_age)
print("Recommended pet food:", recommendation)
