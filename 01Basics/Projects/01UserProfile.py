""" 
    Name: Rahul
    Age: 16
    
    
"""
userName = input("Enter the User Name: ")
userAge = int(input("Enter your age: "))

if userName == "rahul":
    print("Hello, " + userName)
    
elif userAge < 16:
    print("You are not Rahul, Kid")
elif (userAge >16) and (userAge<=60):      # userage in between 16 and 60
    print("You are not Rahul, Mr./Miss Elder")
elif userAge > 1000:
    print("Rahul is still alive. Are you a ghost!")
     
# else:
#     print("Incorrect User Name!")
#     print("Hello, Stranger!")
    