"""

@Author: ayushi raval
Institute: RK UNIVERSITY , INDIA
Language: Python
Version: 3.x

"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("--- Python Calculator ---")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit the program.\n")

    while True:
        # Take input for the operator or exit command
        operator = input("Enter operator (+, -, *, /) or 'exit': ").strip()

        if operator.lower() == 'exit':
            print("Goodbye!")
            break

        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator! Please try again.\n")
            continue

        try:
            # Take input for numbers and convert to float for decimal support
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")
            continue

        # Perform the calculation based on the operator
        if operator == '+':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}\n")
        elif operator == '-':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}\n")
        elif operator == '*':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}\n")
        elif operator == '/':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}\n")

# Run the calculator
if __name__ == "__main__":
    calculator()


