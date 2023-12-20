""" 
    Restraunt : Buffet Items --> list
    codition : Not replacable 
    
    Tuple --> immutable  --> ()
    List --> mutable  --> []
"""

buffetItems = ("Panner", "aloo", "tandoori roti", "rice")

# print(type(buffetItems))

print("Original Items: ")
for item in buffetItems:
    print(item)
    
    
# buffetItems[1] = "Bhindi"

buffetItems = ("Panner", "bhindi", "tawa roti", "rice")



print("\nModified Items")
for item in buffetItems:
    print(item)
    