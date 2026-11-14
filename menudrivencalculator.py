
# Menu Driven Calculator
# Project: Python 3

# Function for Addition
def addition(a, b):
    return a + b


# Function for Subtraction
def subtraction(a, b):
    return a - b


# Function for Multiplication
def multiplication(a, b):
    return a * b


# Function for Division
def division(a, b):
    return a / b


# Function for Power
def power(a, b):
    return a ** b


# Function for Modulus
def modulus(a, b):
    return a % b


# Main calculator function
def calculator():

    while True:

        print("\n========== MENU DRIVEN CALCULATOR ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Exit")
        print("============================================")

        choice = input("Enter your choice: ").strip()

        # Exit option
        if choice == "7":
            print("Thank you for using the calculator. Exiting...")
            break

        # Validate menu choice
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid choice. Please select between 1 and 7.")
            continue

        # Take numeric inputs
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform selected operation
            if choice == "1":
                result = addition(num1, num2)

            elif choice == "2":
                result = subtraction(num1, num2)

            elif choice == "3":
                result = multiplication(num1, num2)

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = division(num1, num2)

            elif choice == "5":
                result = power(num1, num2)

            elif choice == "6":
                if num2 == 0:
                    print("Error: Cannot calculate modulus with zero.")
                    continue
                result = modulus(num1, num2)

            # Display result up to two decimal places
            print(f"Result: {result:.2f}")

        except ValueError:
            print("Error: Please enter valid numeric values.")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

        except OverflowError:
            print("Error: The result is too large to calculate.")


# Start the calculator
if __name__ == "__main__":
    calculator()
            
    