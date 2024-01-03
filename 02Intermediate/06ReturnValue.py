def formattedName(firstName, lastName):
    fullName = f"{firstName} {lastName}"
    return fullName.title()
    
    
# firstName = input("Enter your first name: ")
# lastName = input("Enter your second name: ")

# print(formattedName(firstName, lastName))


# def userData(fName, lName):
#     user = {'first':fName, 'last':lName}
    
#     return user

# userInfo = userData(firstName, lastName)
# print(userInfo)


while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' to quit!)")
    firstName = input("Enter your first name: ")
    if(firstName == 'q'):
        break
    
    lastName = input("Enter your second name: ")
    if(lastName == 'q'):
        break
    
    name = formattedName(firstName, lastName)
    print(f"\nHello, {name}!")