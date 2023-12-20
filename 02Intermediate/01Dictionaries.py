""" 
    {key, value}
"""



# userData = {"name":"peeyush", "age": 20}

userData = {}    #empty dict

# print(type(userData))
userData["name"] = "peeyush"
userData["age"] = 20

print(userData["name"])
print(userData["age"])

print(userData)

#TODO: adding new value
userData["roll"] = "admin"
print(userData)

#TODO: modifying value
userData["age"] = 22
print(userData)

#TODO: deleting
#pop
deletedValue = userData.pop("age")
print(deletedValue)


# #del
# del userData["age"]
print(userData)

#TODO modify Key
# 1. pop the value form old Key
# 2. assign it to new key
# {'name': 'peeyush', 'roll': 'admin'}

oldValue = userData.pop("roll")
userData["Type"] = oldValue      #userData["Type"] = userData.pop("roll")

print(userData)