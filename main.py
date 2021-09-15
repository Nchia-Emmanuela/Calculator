from art import logo
# addition
def add(n1, n2):
    return n1 + n2

# subtraction
def subtract(n1, n2):
    return n1 - n2

# division
def divide(n1, n2):
    return n1 / n2

# multiplication
def multiply(n1, n2):
    return n1 * n2
# dictionary to be able to access each operation
operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}

# this calculator function is a recursive function that calls it self 
# it takes no input and has no output.
def calculator():
    numb1 = float(input("what's the first number?: "))
    for operator in operations:
        print(operator)
    should_continue = True
    while should_continue:
        operation_symbol = input("pick an operation: ")
        numb2 = float(input("what's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(numb1, numb2)
        print(f"{numb1} {operation_symbol} {numb2} = {answer}")
        if input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            numb1 = answer
        else:
            should_continue = False
            # this calculator call will take us back to the beginning
            calculator()

calculator()
        