""" 
    multiple times --> function
"""
#defining Function

def greetUser():
    #body of function
    print("Hello Lerners!")  
    
#function call --> execute the code in the function
# greetUser()

#pass information to function    
def greetUser2(username):
    print(f"hello, {username}")
    
greetUser2("SpiderMan")  #passing "spiderman" Argument to greetUser2
greetUser2("ModiJi")
greetUser2("Ajay")


"""
favouriteBook()
parameter --> title
body --> print a message " My favourit book is <bookTitle>" 
"""
    
def favouriteBook(title):     #definition of functin
    print(f"My favourite book is {title}!")             #body of function
    
    
favouriteBook("Quantum Physics")     #calling the functio
favouriteBook("Mind Reader")
favouriteBook("Elon Musk")
    
    
