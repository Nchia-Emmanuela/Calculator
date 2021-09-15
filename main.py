







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
continue_calulating False
while not continue_calculating:
numb1 = float(input("what's the first number?: "))
for operator in operations:
    print(operator)
operation_symbol = input("pick an operation from the line above: ")
numb2 = float(input("what's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(numb1, numb2)
print(f"{numb1} {operation_symbol} {numb2} = {answer}")