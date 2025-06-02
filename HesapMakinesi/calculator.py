# This is the calculator.py file.
# It contains core calculator logic and a command-line interface.

# --- Core Calculator Logic ---
# The functions in this section are self-contained, perform mathematical
# operations, and raise exceptions for errors. They do not handle
# user input directly or print to the console, making them suitable for import.

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

# End of Core Calculator Logic.
# CLI components previously below this line have been removed.
