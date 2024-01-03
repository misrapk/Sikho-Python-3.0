def userInfo(fName, lName, *userDetails):
    print(f"Hey, {fName} {lName}!")
    print(userDetails)
    
    
# userInfo("Peeyush", "misra")
# userInfo("Peeyush", "MIsra")
# userInfo("peeeyush", "Misra", 24)
# userInfo("Peeyush", "Misra", "Lakhimpur", "UP")
# # userInfo1234455)


def superHuman(name, **info):
    print(name)
    print(info)
    

superHuman("Spiderman", Company = "Marvel")
superHuman("Captain America", 
           location = "NewYork",
           Company = "Marvel")