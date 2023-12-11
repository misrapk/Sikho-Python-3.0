""" 
    Lists --> collection of items in a particular order.
    alphabets, 0-9, names
    
    [] 
    
    index value --> 0, 1, 2, 3, 4, 5, 6 (from front)
                    -7, -6, -5, -4, -3, -2, -1   (from back)     
                    
    ADDING ELEMENT:             
    append --> at the end
    insert(i, value) --> at index i
    
    
"""
            
superhuman = ["SpiderMan", "SuperMan", "Shaktimaan", "IronMan", 230,True]


# print(type(superhuman))
# print(superhuman)


# print(type(superhuman[0]))
# print(superhuman[1])
# print(superhuman[3])
# print(type(superhuman[4]))

print(superhuman[-1])
print(superhuman[5])


#change
print(superhuman)
superhuman[4] = "Captain America"
print(superhuman)

#TODO: add element
# superhuman.append("Junior G")    #at end of string
superhuman.insert(1, "Juinor G")   #at specific index
print(superhuman)


marks = []  #empty list

marks.append(23)
marks.append(26)