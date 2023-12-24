userData = {"userName":"peeyush", 
        "role" : "admin", 
        "active" : True}

# print(userData)

#first method  --> item()
# for k, v in userData.items():
#     print(f"Key: {k}")
#     print(f"Value: {v}")
    
#second method --> keys
# for k in userData.keys():
#     print(k)
    
#third method --> values
for v in userData.values():
    print(v)