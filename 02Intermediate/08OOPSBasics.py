class User:
    
    def __init__(self, fName, lName, location):
        self.fName = fName
        self.lName = lName
        self.location = location
        self.loginCount = 0    #defualt attribute.
        
    def getUser(self):
        print(f"Full Name: {self.fName} {self.lName}")
        print(f"Location: {self.location}")
        
    def showLoginCount(self):
        print(f"{self.fName} has logged in {self.loginCount} times.")
        
    def incrementLoginCount(self):
        self.loginCount +=1
        
    def resetLoginCount(self):
        print("RESET DONE!")
        self.loginCount = 0
        
    
    
#creating instance(object of class USer)
user1 = User("Rahul", "Singh", "Kolkata")
user2 = User("Shital", "Saxena", "Delhi")
user3 = User("Amir", "Khan", "Mumbai")
user1.getUser()
user2.getUser()
user3.getUser()
user1.showLoginCount()
user1.incrementLoginCount()
user1.incrementLoginCount()
user1.incrementLoginCount()
user1.incrementLoginCount()
user1.showLoginCount()
user2.showLoginCount()
user1.resetLoginCount()
user1.showLoginCount()


# user1.loginCount +=1
# user1.showLoginCount()
