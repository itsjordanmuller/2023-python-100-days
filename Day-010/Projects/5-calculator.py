from art import logo

print(logo)


# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2


# Function to divide two numbers
def divide(n1, n2):
    return n1 / n2


# Function to add two numbers
def add(n1, n2):
    return n1 + n2


# Function to subtract two numbers
def subtract(n1, n2):
    return n1 - n2


# Mapping of operators to corresponding functions
operators = {"*": multiply, "/": divide, "+": add, "-": subtract}


def calculator():
    num1 = float(input("What's the first number?: "))

    # Display all available operators
    for operator in operators:
        print(operator)

    calculating = True

    while calculating:
        operation_choice = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operators[operation_choice]
        answer = calculation_function(num1, num2)

        # Display result of the current operation
        print(f"{num1} {operation_choice} {num2} = {answer}")

        # Decide whether to continue with the current result or restart
        if input("Do you want to continue? 'y'/'n' ") == "y":
            num1 = answer
        else:
            calculating = False
            calculator()


# Start the calculator
calculator()
