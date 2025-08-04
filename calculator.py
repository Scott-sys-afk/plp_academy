# Basic Calculator Program

# Step 1: Get user input for two numbers
print("Welcome to the Basic Calculator!")
num1 = float(input("Enter the first number: "))  # We use float() to handle decimal numbers
num2 = float(input("Enter the second number: "))

# Step 2: Get the operation from the user
print("Available operations:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operation = input("Enter the operation (+, -, *, /): ")

# Step 3: Perform the calculation based on the operation
result = 0  # We'll store the result here

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")  # f-string makes formatting easy
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 == 0:  # Check for division by zero
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation! Please use +, -, *, or /")

# Step 4: End the program
print("Thank you for using the Basic Calculator!")