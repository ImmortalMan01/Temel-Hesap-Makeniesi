# This is the calculator.py file.
# It will contain the calculator logic.

import math

def _is_numeric(val):
    """Helper function to check if a value is numeric (int or float)."""
    return isinstance(val, (int, float))

def add(x, y):
  """Adds two numbers."""
  if not (_is_numeric(x) and _is_numeric(y)):
    raise TypeError("Inputs must be numeric")
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  if not (_is_numeric(x) and _is_numeric(y)):
    raise TypeError("Inputs must be numeric")
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  if not (_is_numeric(x) and _is_numeric(y)):
    raise TypeError("Inputs must be numeric")
  return x * y

def divide(x, y):
  """Divides two numbers."""
  if not (_is_numeric(x) and _is_numeric(y)):
    raise TypeError("Inputs must be numeric")
  if y == 0:
    raise ZeroDivisionError("Cannot divide by zero")
  return x / y

def power(x, y):
  """Calculates x raised to the power of y."""
  if not (_is_numeric(x) and _is_numeric(y)):
    raise TypeError("Inputs must be numeric")
  return math.pow(x, y)

def square_root(x):
  """Calculates the square root of x."""
  if not _is_numeric(x):
    raise TypeError("Input must be numeric")
  if x < 0:
    raise ValueError("Cannot calculate square root of a negative number")
  return math.sqrt(x)

def log_natural(x):
  """Calculates the natural logarithm (base e) of x."""
  if not _is_numeric(x):
    raise TypeError("Input must be numeric")
  if x <= 0:
    raise ValueError("Cannot calculate logarithm of a non-positive number")
  return math.log(x)

def log_base10(x):
  """Calculates the base-10 logarithm of x."""
  if not _is_numeric(x):
    raise TypeError("Input must be numeric")
  if x <= 0:
    raise ValueError("Cannot calculate logarithm of a non-positive number")
  return math.log10(x)

def sine(x):
  """Calculates the sine of x (x in radians)."""
  if not _is_numeric(x):
    raise TypeError("Input must be numeric")
  return math.sin(x)

def cosine(x):
  """Calculates the cosine of x (x in radians)."""
  if not _is_numeric(x):
    raise TypeError("Input must be numeric")
  return math.cos(x)

def tangent(x):
  """Calculates the tangent of x (x in radians)."""
  if not _is_numeric(x):
    raise TypeError("Input must be numeric")
  # tan(pi/2 + k*pi) is undefined
  if math.isclose(math.cos(x), 0):
      raise ValueError("Tangent is undefined for angles where cosine is zero (e.g., pi/2 + k*pi)")
  return math.tan(x)

# --- CLI Implementation ---
def parse_input(user_input):
    """Parses user input into operation and arguments."""
    parts = user_input.strip().lower().split()

    if not parts:
        raise ValueError("Input cannot be empty.")

    op_or_func = parts[0]

    # Two-argument operations: num op num
    if len(parts) == 3:
        try:
            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])
            # Re-assign op_or_func to be the actual operator symbol
            return op, [num1, num2]
        except ValueError: # If first part is not a number, it might be a function call that was mistyped with 3 args
            pass # Fall through to check if it's a known single-argument function name with wrong number of args

    # Single-argument functions: func num
    if len(parts) == 2:
        try:
            num = float(parts[1])
            return op_or_func, [num]
        except ValueError:
            raise ValueError(f"Invalid number: {parts[1]}")

    # Handle cases like "10 +", "sqrt" (missing arguments) or "10 + 5 extra"
    if op_or_func in COMMANDS_WITH_TWO_ARGS or op_or_func in FUNCTIONS_WITH_ONE_ARG:
        if len(parts) < COMMANDS_WITH_TWO_ARGS.get(op_or_func, FUNCTIONS_WITH_ONE_ARG.get(op_or_func, [0,0])[1] ) +1 : # +1 for the command itself
             raise ValueError(f"Missing arguments for '{op_or_func}'.")
        else:
             raise ValueError(f"Too many arguments for '{op_or_func}'.")


    # If input is like "num op num" but was parsed initially as op_or_func = parts[0] (a number)
    # This is a bit of a workaround due to initial split.
    # Example: "10 + 5", parts = ["10", "+", "5"]. op_or_func = "10"
    # This was handled by the len(parts) == 3 block if the first part is successfully float(parts[0])
    # However, if parts[0] is not a float, we might have a function name.
    # Let's refine the logic for "num op num"
    if len(parts) == 3 and parts[1] in COMMANDS_WITH_TWO_ARGS:
        try:
            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])
            return op, [num1, num2]
        except ValueError:
            raise ValueError(f"Invalid numbers: {parts[0]}, {parts[2]}")


    raise ValueError(f"Invalid input format: '{user_input}'. Expected 'number operator number' or 'function number'.")


COMMANDS_WITH_TWO_ARGS = {
    '+': (add, 2),
    '-': (subtract, 2),
    '*': (multiply, 2),
    '/': (divide, 2),
    'pow': (power, 2),
    'power': (power, 2)
}

FUNCTIONS_WITH_ONE_ARG = {
    'sqrt': (square_root, 1),
    'log': (log_natural, 1),
    'ln': (log_natural, 1),
    'log10': (log_base10, 1),
    'sin': (sine, 1),
    'cos': (cosine, 1),
    'tan': (tangent, 1)
}

def run_cli():
    """Runs the command-line interface for the calculator."""
    print("Welcome to the Command-Line Calculator!")
    print("You can perform calculations like:")
    print("  '10 + 5' (for basic arithmetic: +, -, *, /)")
    print("  'pow 2 3' (for exponentiation)")
    print("  'sqrt 25' (for square root)")
    print("  'log 10' or 'ln 10' (for natural logarithm)")
    print("  'log10 100' (for base-10 logarithm)")
    print("  'sin 1.57' (for sine, angle in radians)")
    print("  'cos 3.14' (for cosine, angle in radians)")
    print("  'tan 0.785' (for tangent, angle in radians)")
    print("Type 'quit' or 'exit' to close.")
    print("-" * 30)

    while True:
        try:
            user_input = input("calc> ").strip()
            if user_input.lower() in ['quit', 'exit']:
                print("Exiting calculator. Goodbye!")
                break
            if not user_input:
                continue

            # Try parsing as "num op num" first if possible
            parts = user_input.split()
            parsed_op = None
            args = []

            if len(parts) == 3 and parts[1] in COMMANDS_WITH_TWO_ARGS:
                try:
                    num1 = float(parts[0])
                    op_symbol = parts[1]
                    num2 = float(parts[2])
                    parsed_op = op_symbol
                    args = [num1, num2]
                except ValueError:
                    # Could be "func arg1 arg2" which is not supported for our functions
                    # or "func arg" which is handled next.
                    # Or just invalid numbers.
                    pass # Let the generic parser handle it or raise error.

            if not parsed_op: # If not "num op num" or failed parsing it
                # Try parsing as "func arg" or handle errors
                parsed_op, args = parse_input(user_input)


            result = None
            if parsed_op in COMMANDS_WITH_TWO_ARGS:
                func, _ = COMMANDS_WITH_TWO_ARGS[parsed_op]
                result = func(args[0], args[1])
            elif parsed_op in FUNCTIONS_WITH_ONE_ARG:
                func, _ = FUNCTIONS_WITH_ONE_ARG[parsed_op]
                result = func(args[0])
            else:
                # This case should ideally be caught by parse_input raising an error
                print(f"Error: Unknown operation or function '{parsed_op}'")
                continue

            # Check if result is a float and if it's an integer, print as int
            if isinstance(result, float) and result.is_integer():
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result:.4f}" if isinstance(result, float) else f"Result: {result}")

        except (ValueError, TypeError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_cli()
