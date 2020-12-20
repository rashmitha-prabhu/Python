import art

print(art.logo)


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    if n2 == 0:
        return "Divide by zero error"
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("Operations available: ")
for keys in operations:
    print(keys)


def calculator():
    num1 = float(input("What's the first number? : "))
    ch = 'y'
    while ch == 'y':
        op = input("Operation : ")
        num2 = float(input("What's the next number? : "))
        function = operations[op]
        ans = round(function(num1, num2), 2)
        print(f"\n{num1} {op} {num2} = {ans}\n")
        
        ch = input(f"Type 'y' to continue calculating with {ans}, 'n' to restart and 'x' to exit: ")

        if ch == 'y':
            num1 = ans
        elif ch == 'n':
            calculator()


calculator()
