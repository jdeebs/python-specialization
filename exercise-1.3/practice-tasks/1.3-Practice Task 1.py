a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
operation = str(input("Do you want to add or subtract the numbers? Use '+' or '-': "))

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
else:
    print("Unknown operator")