







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

numb1 = float(input("what's the first number? :"))
numb2 = float(input("what's the second number? :"))
for operator in operations:
    print(operator)