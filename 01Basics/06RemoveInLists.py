""" 
    Removing elements from list:
    1. del
    2. remove(value)
    3. pop
    
    Reeference: 
    queue ==> station, ticket counter
    t --> 1 2 3 4 5 6 7 8 9 10
    stack ==> bundle of books
    10 9 8 7 6 5 4 3 2 1
"""

programmingLanguages = ["pyhton", "c++", "JAVA", "JS", "Machine Learning", "Ruby", "web development"]

skill =[]   #empty list

print(programmingLanguages)

# del programmingLanguages[4]

# programmingLanguages.remove("Machine Learning")

skillElement = programmingLanguages.pop()
skillElement2 = programmingLanguages.pop(4)

print(programmingLanguages)
print(skillElement)
skill.append(skillElement)
skill.append(skillElement2)
print(skill)