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
