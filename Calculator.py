print("Simple Calculator")
print("Operations: +  -  *  /")

num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        result = "Error: cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)