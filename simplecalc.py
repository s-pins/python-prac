num1 = float(input("Enter the first number. \n" ))
num2 = float(input("Enter the second number. \n"))
action = input("What arithmetic action to perform(+, -, *, /). \n")

if '+' == action:
    result = num1 + num2
elif '-' == action:
    result = num1 - num2
elif '*' == action:
    result = num1 * num2
elif '/' == action:
    if num1 and num2 != 0:
        result = num1 / num2
    else:
        print("Error division by 0")
        exit()
else:
    print("Operation unknown")

print(f"{num1} {action} {num2} = {result}")