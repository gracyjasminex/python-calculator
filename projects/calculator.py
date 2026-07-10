a = float(input("enter number 1: "))
b = float(input("enter number 2: "))

operation = input("Chooose (+, -, *, /) ")

if operation == "+":
    print("Answer = ", a+b)

elif operation == "-":
    print("Answer = ", a-b)

elif operation == "*":
    print("Answer = ", a*b)

elif operation == "/":
    if b != 0:
        print("Answer = ", a/b)
    
    else:
        print("A number cannot be divided by zero")

else:
    print("Sorry, this calculator can only add, subtract, multiply and divide.")



