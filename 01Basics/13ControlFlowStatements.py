""" 
Box --> toys --> Doraemon

1. look into the box
2. pick a toy
3. compare with "Doraemon"
4. if doaremon then hurray. Goto 6.
5. else repeat 2 to 4.
6. Found End!
"""

toys = ["Spiderman", "Doll","Doraemon" ,"Remote car", "Car", "Shinchan" ]
favouriteToy = "Spiderman"

# for toy in toys:
#     if toy == favouriteToy:
#         print("Hooray! I Found Dorameon!")
#         break     #end the loop
    
#     else:
#         print("This is not what i am looking")
        
        
        
for num in range(1,11):
    if num%2 !=0:
        continue
    print(num)