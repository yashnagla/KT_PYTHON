class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
res = 0
while True:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operator = input("Enter the operator +, -, *, /, e(to exit) : ")
    if operator == "+":
        res = Calculator().add(x, y)
    elif operator == "-":
        res = Calculator().sub(x, y)
    elif operator == "*":
        res = Calculator().mul(x, y)
    elif operator == "/":
        res = Calculator().div(x, y)
    elif operator == "e":
        break
    else:
        result = "Invalid operator"
    print("Result: ", result)
    conProgram = input("Do you want to continue? (yes/no) : ").strip().lower()
    if conProgram != "yes":
        print("Exiting the program. Goodbye!")
        break