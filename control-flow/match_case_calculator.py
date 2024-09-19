num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
choice = input("Choose the operation (+, -, *, /): ")
match choice:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:  
            result = num1 / num2
            print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")