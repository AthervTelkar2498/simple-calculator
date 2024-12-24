# Simple Calculator Program

def calculator():
    """A simple calculator to perform basic arithmetic operations."""
    print("Welcome to the Simple Calculator!")

    # Input two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Display operation options
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Input the user's choice
    choice = input("Enter the number corresponding to your choice (1/2/3/4): ")

    # Perform the selected operation
    if choice == "1":
        result = num1 + num2
        operation = "+"
    elif choice == "2":
        result = num1 - num2
        operation = "-"
    elif choice == "3":
        result = num1 * num2
        operation = "*"
    elif choice == "4":
        if num2 == 0:  # Handle division by zero
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = "/"
    else:
        print("Invalid choice. Please select a valid operation.")
        return

    # Display the result
    print(f"\nThe result of {num1} {operation} {num2} is: {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
