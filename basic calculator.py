
print("Simple Calculator")
print("------------------")

while True:
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator... Goodbye!")
        break

    # Take numbers as input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform selected operation
    if choice == '1':
        result = num1 + num2
        print(f"The sum is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The difference is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The product is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The quotient is: {result}")
        else:
            print("Error! Cannot divide by zero.")
    else:
        print("Invalid input! Please enter 1, 2, 3, 4, or 5.")
