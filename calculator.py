def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers."""
    if (b==0):
        return("Division par zéro")
    else:
        return a / b


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 30)
    print("       CALCULATOR")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 30)


def get_numbers():
    """Ask the user for two numbers."""
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    return (a, b)

def main():
    """Run the calculator."""

    while True:
        display_menu()

        choice = input("Choose an operation: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice.")
            continue

        # Get the numbers
        (a, b) = get_numbers()

        if choice == "1":
            result = add(a, b)

        if choice == "2":
            result = subtract(a, b)

        if choice == "3":
            result = multiply(a, b)

        if choice == "4":
            result = divide(a, b)

        # Perform the selected operation
        # result = ...

        # Display the result
        print(f"Result: {result}")


if __name__ == "__main__":
    main()