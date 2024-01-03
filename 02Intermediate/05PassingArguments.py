# print("Delhi is in India!")


def cityInfo(cityName, countryName):
    print(f"\nI live in {cityName}.")
    print(f"{cityName} is in {countryName}.")
    
# cityInfo("Lakhimpur", "India")
# # cityInfo("India", "Kolkata")

# cityInfo(cityName="Delhi", countryName="India")
# cityInfo(countryName="China", cityName="Beijing")

#Default Value

def describePets(petName, age, animalType = "Dog"):
    print(f"\nI have {animalType}.")
    print(f"My {animalType}'s name is {petName}")
    print(f"{petName} is {age} years old!")


describePets("Rocky", 5, "Dog")
describePets(petName="Bruno", animalType="Dog", age=1)
describePets("Kitty", 3, "Cat")
describePets("Tiger", 5)