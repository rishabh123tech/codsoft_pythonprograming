a = float(input("First number: "))
b = float(input("Second number: "))
print("\nChoose operation:")
print("1  add")
print("2 subtract ")
print("3 multiply ")
print("4 divide ")

op = input("Enter 1 / 2 / 3 / 4: ")


if op == "1":
    result = a + b
elif op == "2":
    result = a - b
elif op == "3":
    result = a * b
elif op == "4":
    if b == 0:
        print("Cannot divide by zero.")
        quit()
    result = a / b
else:
    print("Invalid choice.")
    quit()

print("Result:", result)
