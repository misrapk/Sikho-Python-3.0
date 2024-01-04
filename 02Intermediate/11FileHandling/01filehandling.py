#TODO: REadONLy
# with open("test.txt", 'r') as files:
#     # content = files.read()
#     # print("FIle CLosed\n")
#     lines = files.readlines()
    
    
# # print(content)

# for line in lines:
#     print(line.rstrip())

#TODO: WRite Files

with open("favProgramming.txt", "w") as files:
    files.write("I Love Python")
    
    
#TODO: Append
with open("favProgramming.txt", "a") as files:
    files.write("\nI Love C++.")
    