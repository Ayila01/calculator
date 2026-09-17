
import tkinter as tk
from tkinter import messagebox


# =========================
# Mathematical operations
# =========================

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
    return a / b


# =========================
# Calculator logic
# =========================

def calculate():
    """Read the inputs and display the result."""

    try:
        # Read the numbers
        first_number = float(first_number_entry.get())
        second_number = float(second_number_entry.get())

        # Read the selected operation
        operation = operation_var.get()

        # Perform the calculation
        if operation == "+":
            result = add(first_number, second_number)

        elif operation == "-":
            result = subtract(first_number, second_number)

        elif operation == "*":
            result = multiply(first_number, second_number)

        elif operation == "/":
            result = divide(first_number, second_number)

        # Display the result
        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )

    except ZeroDivisionError:
        messagebox.showerror(
            "Error",
            "Cannot divide by zero."
        )


def clear():
    """Clear the input fields and result."""

    first_number_entry.delete(0, tk.END)
    second_number_entry.delete(0, tk.END)

    operation_var.set("+")

    result_label.config(text="Result: ")


def insert_operation(operation):
    """Insert an operation into the interface."""

    operation_var.set(operation)


# =========================
# Graphical interface
# =========================

window = tk.Tk()
window.title("Calculator")
window.geometry("400x450")
window.resizable(False, False)


# Title
title_label = tk.Label(
    window,
    text="CALCULATOR",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)


# First number
first_number_label = tk.Label(
    window,
    text="First number:"
)
first_number_label.pack()

first_number_entry = tk.Entry(
    window,
    width=30
)
first_number_entry.pack(pady=5)


# Second number
second_number_label = tk.Label(
    window,
    text="Second number:"
)
second_number_label.pack()

second_number_entry = tk.Entry(
    window,
    width=30
)
second_number_entry.pack(pady=5)


# Operation selection
operation_label = tk.Label(
    window,
    text="Choose an operation:"
)
operation_label.pack(pady=(15, 5))


operation_var = tk.StringVar(value="+")

operation_menu = tk.OptionMenu(
    window,
    operation_var,
    "+",
    "-",
    "*",
    "/"
)
operation_menu.pack()


# Calculate button
calculate_button = tk.Button(
    window,
    text="Calculate",
    command=calculate,
    width=20
)
calculate_button.pack(pady=20)


# Result
result_label = tk.Label(
    window,
    text="Result: ",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)


# Clear button
clear_button = tk.Button(
    window,
    text="Clear",
    command=clear,
    width=20
)
clear_button.pack(pady=10)


# Start application
window.mainloop()