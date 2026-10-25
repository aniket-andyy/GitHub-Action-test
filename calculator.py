
import math


# Basic arithmetic operations

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# Scientific operations

def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)


def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Factorial requires a non-negative integer.")
    return math.factorial(n)


def sin(degrees):
    return math.sin(math.radians(degrees))


def cos(degrees):
    return math.cos(math.radians(degrees))


def tan(degrees):
    if math.isclose(
        math.cos(math.radians(degrees)), 0.0, abs_tol=1e-12
    ):
        raise ValueError("Tangent is undefined at this angle.")
    return math.tan(math.radians(degrees))


def log10(x):
    if x <= 0:
        raise ValueError("Logarithm requires a positive number.")
    return math.log10(x)


def natural_log(x):
    if x <= 0:
        raise ValueError("Natural logarithm requires a positive number.")
    return math.log(x)


# Interactive command-line interface

def main():
    operations = {
        "1": ("Add", add, 2),
        "2": ("Subtract", subtract, 2),
        "3": ("Multiply", multiply, 2),
        "4": ("Divide", divide, 2),
        "5": ("Power", power, 2),
        "6": ("Square root", square_root, 1),
        "7": ("Factorial", factorial, 1),
        "8": ("Sine (degrees)", sin, 1),
        "9": ("Cosine (degrees)", cos, 1),
        "10": ("Tangent (degrees)", tan, 1),
        "11": ("Log base 10", log10, 1),
        "12": ("Natural logarithm", natural_log, 1),
    }

    while True:
        print("\n=== SCIENTIFIC CALCULATOR ===")
        for key, (name, _, _) in operations.items():
            print(f"{key}. {name}")
        print("0. Exit")

        choice = input("Choose an operation: ").strip()

        if choice == "0":
            print("Calculator closed.")
            break

        if choice not in operations:
            print("Invalid choice. Try again.")
            continue

        name, function, argument_count = operations[choice]

        try:
            values = []
            for i in range(argument_count):
                values.append(float(input(f"Enter number {i + 1}: ")))

            # Factorial accepts integers only.
            if choice == "7":
                if not values[0].is_integer():
                    raise ValueError(
                        "Factorial requires a non-negative integer."
                    )
                values[0] = int(values[0])

            result = function(*values)
            print(f"{name} result: {result:.10g}")

        except (ValueError, OverflowError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
