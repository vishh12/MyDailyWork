def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Perform the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operation. Please choose one of the listed operations.")
            return
        
        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
