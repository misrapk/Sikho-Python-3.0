""" 
    Slicing: 
    
    4 ==> 1/4
    
    listName[start:stop:step]   #exculding Stop(stop-1)
"""
movieNames = ["Jawan", "Gadar2", "Animal", "Tiger 3", "Brmhastra"]

# print(movieNames[1:2])
# print(movieNames[0:2])
# print(movieNames[2:6])

# #from back
# print(movieNames[2:-2])
# print(movieNames[1:])
# print(movieNames[:3])
# print(movieNames[-3:])


squareNumber = [value**2 for value in range(1,11)]
print(squareNumber)

print(squareNumber[1:6])
print(squareNumber[1::2])
print(squareNumber[::2])
print(squareNumber[6:1:-2])


print(squareNumber[::-1])


squareNumberEven = squareNumber[1::2]
print(squareNumberEven)
squareNumberOdd = squareNumber[::2]
print(squareNumberOdd)


squareNumberOdd[1:3] = [14, 15, 13]
print(squareNumberOdd)
squareNumberOdd[:0] = [1,2,3]
print(squareNumberOdd)


#delete
print(squareNumber)
squareNumber[1:3] = []
print(squareNumber)