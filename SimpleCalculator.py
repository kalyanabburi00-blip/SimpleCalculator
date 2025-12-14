#inputs

v1 = int(input("Enter First Value: "))
v2 = int(input("Enter Second Value: "))

o = input("Enter Operation: ")

if o == "+" :
    print(f"Your Sum is:{v1+v2} ")
    
elif o == "-" :
    print(f"Your Sub is:{v1-v2} ")
    
elif o == "*" :
    print(f"Your Mul is:{v1*v2} ")
    
elif o == "/" :
    print(f"Your Div is:{v1/v2} ")
    
else:
    print(f"You Entered Invalid Operator")
    