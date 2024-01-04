num1 = int(input("Enter First Numnber: "))
num2 = int(input("Enter Second Number: "))

try:
    answer = num1/num2    
 
except ZeroDivisionError:
    print("Can't divide by zero")   

except Exception:
    print(f"Unexpected error: {Exception}")
    
else:
    print(f"num1/num2 = {answer}")
    
finally:
    print("Thank You")
    




