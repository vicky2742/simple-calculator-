# Min  Calculator
first = input("enter the first Number :")
second = input("enter the second Number :")
operator = input("press the operator (+ - * / %) :")
first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")
