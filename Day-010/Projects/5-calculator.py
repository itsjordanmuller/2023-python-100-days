from art import logo

print(logo)


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


operators = {"*": multiply, "/": divide, "+": add, "-": subtract}


def calculator():
    num1 = float(input("What's the first number?: "))
    for operator in operators:
        print(operator)
    calculating = True

    while calculating:
        operation_choice = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operators[operation_choice]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_choice} {num2} = {answer}")

        if input("Do you want to continue? 'y'/'n' ") == "y":
            num1 = answer
        else:
            calculating = False
            calculator()


calculator()
