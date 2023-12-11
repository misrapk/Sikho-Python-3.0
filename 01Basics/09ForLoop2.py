""" 
    range(start, end)  --> end Excluded
"""

# numbers = list(range(0,1000, 100))

# print(numbers)

squares = []  #empty

for value in range(1,11):
    square = value**2
    squares.append(square)
    
print(squares)


#list compreshension
cubes = [value**3 for value in range(1,11)]
print(cubes)