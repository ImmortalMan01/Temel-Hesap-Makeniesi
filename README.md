# Python Command-Line Calculator

This repository contains a command-line calculator implemented in Python (`HesapMakinesi/calculator.py`). It supports basic arithmetic, advanced mathematical operations, and provides a simple interactive interface.

## Features

-   **Basic Arithmetic:** Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`)
-   **Advanced Operations:**
    -   Exponentiation (`pow` or `power`)
    -   Square Root (`sqrt`)
    -   Natural Logarithm (`log` or `ln`)
    -   Base-10 Logarithm (`log10`)
    -   Trigonometric Functions: Sine (`sin`), Cosine (`cos`), Tangent (`tan`) (input angles in radians)
-   **Interactive CLI:** Easy-to-use command-line interface.
-   **Error Handling:** Provides feedback for invalid inputs or mathematical errors (e.g., division by zero, square root of a negative number).

## Running the Calculator

To run the calculator, navigate to the project's root directory in your terminal and execute the following command:

```bash
python HesapMakinesi/calculator.py
```

This will start the interactive calculator prompt.

## How to Use

The calculator will display a `calc> ` prompt, waiting for your input.

**Input Format:**

You can enter expressions in two main formats:

1.  **For binary operations (two numbers):**
    `number operator number`
    *   Examples:
        *   `10 + 5`
        *   `20.5 * 2`
        *   `100 / 8`
        *   `2 pow 8` (or `2 power 8`)

2.  **For unary functions (one number):**
    `function_name number`
    *   Examples:
        *   `sqrt 25`
        *   `log 10` (natural logarithm)
        *   `ln 2.718` (natural logarithm)
        *   `log10 1000`
        *   `sin 1.5708` (sine of approx. pi/2 radians)
        *   `cos 3.14159` (cosine of approx. pi radians)
        *   `tan 0.7854` (tangent of approx. pi/4 radians)

**Available Operations and Functions:**

*   **Addition:** `+`
*   **Subtraction:** `-`
*   **Multiplication:** `*`
*   **Division:** `/`
*   **Exponentiation:** `pow`, `power`
*   **Square Root:** `sqrt`
*   **Natural Logarithm (base e):** `log`, `ln`
*   **Base-10 Logarithm:** `log10`
*   **Sine (angle in radians):** `sin`
*   **Cosine (angle in radians):** `cos`
*   **Tangent (angle in radians):** `tan`

**Exiting the Calculator:**

To close the calculator, type `quit` or `exit` at the prompt and press Enter.

```
calc> quit
Exiting calculator. Goodbye!
```

## Unit Tests

The calculator functions are unit-tested using Python's `unittest` module. The tests are located in `HesapMakinesi/test_calculator.py`. To run the tests, navigate to the `HesapMakinesi` directory and run:
```bash
python -m unittest test_calculator.py
```

*(Previously, this README described a basic C++ calculator. It has been updated to reflect the current Python CLI calculator project.)*
