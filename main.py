# MAKING A CALCULATOR

# DEFINING OPERATIONS

def add(x, y):
    return(x + y)

def subtract(x, y):
    return(x - y)

def multiply(x, y):
    return(x * y)

def divide(x, y):
    numerator = x
    denominator = y
    if denominator == 0:
        print("Division by zero is not allowed. Please provide a non-zero denominator.")

    else:
        result = numerator / denominator
        print(result)
    return(x / y)

# SETTING WHILE LOOP

while True:
    # Displaying options for the user
    print("Options: ")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the application")

    # Getting the user answers
    user_input = input(": ")

    # Checking if user wants to quit
    if user_input == 'quit':
        break

    # Operations used
    if user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == 'add':
            print("Resut: " ,add(num1 , num2))

        elif user_input == 'subtract':
            print("Result: ", subtract(num1, num2))

        elif user_input == 'multiply':
            print("Result: ", multiply(num1, num2))

        elif user_input == 'divide':
            print("Result: ", divide(num1, num2))

        else:
            print("Invalid Input!")

