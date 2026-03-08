import math

num1 = float(input("Enter first number: "))
op = input("Enter operator (+,-,*,/,%,**,sqrt): ")
num2 = None

if op != "sqrt":
    num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    print("Result:", num1 / num2)

elif op == "%":
    print("Result:", num1 % num2)

elif op == "**":
    print("Result:", num1 ** num2)

elif op == "sqrt":
    print("Result:", math.sqrt(num1))

else:
    print("Invalid Operator")