""" 
Basic Calculator Program in Python
This code snippet provides a simple command-line interface calculator that supports:
- Addition
- Subtraction
- Multiplication
- Division
- Modulo
- Floor Division
- Exponentiation
Note:
This calculator does NOT support scientific or advanced math operations.
"""

def add(x, y):
    """Return the sum of x and y"""
    return x + y

def subtract(x, y):
    """Return the difference of x and y"""
    return x - y

def multiply(x, y):
    """Return the product of x and y"""
    return x * y

def divide(x, y):
    """Return the quotient of x divided by y"""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def modulo(x, y):
    """Return the remainder of x divided by y"""
    if y == 0:
        raise ValueError("Cannot take modulo by zero.")
    return x % y

def floor_division(x, y):
    """Return the floor division result of x by y"""
    if y == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return x // y

def exponent(x, y):
    """Return x raised to the power of y"""
    return x ** y

def display_menu():
    """Display the list of available operations"""
    print("\n📌 Basic Calculator Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. Floor Division (//)")
    print("7. Exponentiation (**)")
    print("0. Exit")

def main():
    """Main function to run the calculator"""
    print("🔢 Welcome to the Basic Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Choose an operation (0-7): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        if choice == 0:
            print("👋 Exiting the calculator. Goodbye!")
            break

        if choice not in range(1, 8):
            print("❌ Invalid choice. Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid number. Please enter numeric values.")
            continue

        try:
            if choice == 1:
                result = add(num1, num2)
                operation = '+'
            elif choice == 2:
                result = subtract(num1, num2)
                operation = '-'
            elif choice == 3:
                result = multiply(num1, num2)
                operation = '*'
            elif choice == 4:
                result = divide(num1, num2)
                operation = '/'
            elif choice == 5:
                result = modulo(num1, num2)
                operation = '%'
            elif choice == 6:
                result = floor_division(num1, num2)
                operation = '//'
            elif choice == 7:
                result = exponent(num1, num2)
                operation = '**'

            print(f"✅ Result: {num1} {operation} {num2} = {result}")

        except ValueError as ve:
            print(f"❗ Error: {ve}")
        except Exception as e:
            print(f"❗ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
