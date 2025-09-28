while True:
    num1 = int(input("Give 1st number: "))
    num2 = int(input("Give 2nd number: "))

    operator = input("Give operator (+, -, *, /): ")

    if operator == "+":
        print(f"Addition of 2 numbers is {num1 + num2}")
    elif operator == "-":
        print(f"Subtraction of 2 numbers is {num1 - num2}")
    elif operator == "*":
        print(f"Multiplication of 2 numbers is {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"Division of 2 numbers is {num1 / num2}")
        else:
            print("Division by zero is not allowed")
    else:
        print("Not valid operator")

    # Ask if user wants to continue
    choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting calculator... Goodbye!")
        break
