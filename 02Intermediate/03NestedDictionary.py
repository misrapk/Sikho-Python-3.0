#favourite programming language

userData = {
    "Amit" : {
    "first": "Amit",
    "role": "user"
    },  
    "Sakshi" : {
    "first":"Sakshi",
    "role": "content writer"
    }
    
}

# for k, v in userData.items():
#     print(f"{k} : {v}")
  
# for username, userinfo in userData.items():
#     print(f"Username: {username}")
#     firstName = f"{userinfo['first']}"
#     userrole = f"{userinfo['role']}"
#     print(firstName)
#     print(userrole)
    
    
favouriteLanguage = {
    'priya' : ['Python', 'C++'],
    'peeyush' : ['Python', 'JS', 'C++'],
    'akshay' : ['ReactJS', 'JS', 'HTML', 'CSS'],
}

for user, language in favouriteLanguage.items():
    print(user)
    for lang in language:
        print(lang)