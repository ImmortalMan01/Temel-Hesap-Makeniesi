# Python Calculator Project

This repository contains a Python-based calculator with two main interfaces:
1.  A **Graphical User Interface (GUI)** built with Tkinter for ease of use.
2.  A **Command-Line Interface (CLI)** for users who prefer text-based interaction.

Both interfaces utilize the same underlying calculator logic found in `HesapMakinesi/calculator.py`.

---

## GUI Calculator (Recommended)

The GUI calculator provides a user-friendly, visual way to perform calculations. It's built using Python's standard Tkinter library.

### Running the GUI Calculator

To run the GUI calculator, navigate to the project's root directory in your terminal and execute:

```bash
python HesapMakinesi/gui_calculator.py
```

### GUI Layout and Usage

The GUI features:
-   **Display Area:** A large entry field at the top shows the current expression being built and the results of calculations.
-   **Number Buttons (0-9, .):** Standard numeric input and decimal point.
-   **Operator Buttons:**
    -   Basic Arithmetic: `+`, `-`, `*`, `/`
    -   Exponentiation: `pow`
-   **Function Buttons:**
    -   `sqrt`: Square Root
    -   `log`: Natural Logarithm (base e)
    -   `log10`: Base-10 Logarithm
    -   `sin`, `cos`, `tan`: Trigonometric functions (input angles in radians)
-   **Control Buttons:**
    -   `=` (Equals): Evaluates the current expression.
    -   `C` (Clear): Clears the entire current expression and resets the display.
    -   `CE` (Clear Entry): Clears the last character entered into the expression (simplified version).
-   **Other Buttons:**
    -   `(` and `)`: For grouping expressions.
    -   `π`: Inserts the constant Pi.

**How to Use:**
1.  Click the buttons to build your mathematical expression in the display area.
2.  Functions like `sqrt` or `log` will appear as `sqrt(` or `log(`, prompting you to enter the argument.
3.  Use parentheses `(` `)` to group parts of your expression as needed.
4.  Press the `=` button to see the result.
5.  The result of a calculation can be used as the starting point for the next calculation.
6.  Press `C` to clear the current expression and start over.

### Error Handling (GUI)
If you enter an invalid expression or a calculation results in a mathematical error (e.g., division by zero, square root of a negative number):
-   The display will typically show "Error".
-   A popup dialog box will appear with a more specific error message.
The expression will usually be cleared or reset after an error, allowing you to start a new calculation.

---

## Command-Line Interface (CLI) Calculator

For users who prefer a text-based interface, a command-line calculator is also available.

### Features (CLI)

-   **Basic Arithmetic:** Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`)
-   **Advanced Operations:**
    -   Exponentiation (`pow` or `power`)
    -   Square Root (`sqrt`)
    -   Natural Logarithm (`log` or `ln`)
    -   Base-10 Logarithm (`log10`)
    -   Trigonometric Functions: Sine (`sin`), Cosine (`cos`), Tangent (`tan`) (input angles in radians)
-   **Interactive CLI:** Easy-to-use command-line prompt.
-   **Error Handling:** Provides feedback for invalid inputs or mathematical errors.

### Running the CLI Calculator

To run the CLI calculator, execute the following command from the project's root directory:

```bash
python HesapMakinesi/calculator.py
```

This will start the interactive `calc> ` prompt.

### How to Use (CLI)

**Input Format:**

1.  **For binary operations (two numbers):** `number operator number`
    *   Examples: `10 + 5`, `2 pow 8`
2.  **For unary functions (one number):** `function_name number`
    *   Examples: `sqrt 25`, `log 10`

**Available Operations and Functions (CLI keywords):**
(Refer to the CLI prompts or `calculator.py` for the exact keywords if different from GUI buttons)
*   Addition: `+`
*   Subtraction: `-`
*   Multiplication: `*`
*   Division: `/`
*   Exponentiation: `pow`, `power`
*   Square Root: `sqrt`
*   Natural Logarithm (base e): `log`, `ln`
*   Base-10 Logarithm: `log10`
*   Sine (angle in radians): `sin`
*   Cosine (angle in radians): `cos`
*   Tangent (angle in radians): `tan`

**Exiting the CLI Calculator:**
Type `quit` or `exit` at the prompt and press Enter.

---

## Unit Tests

The core calculator logic (used by both GUI and CLI) is unit-tested using Python's `unittest` module. The tests are located in `HesapMakinesi/test_calculator.py`. To run the tests, navigate to the `HesapMakinesi` directory and run:
```bash
python -m unittest test_calculator.py
```

---
*Historical Note: This project initially started as a very basic C++ calculator. It has since evolved into a Python project featuring both a command-line interface and a more user-friendly GUI calculator, both sharing the same underlying Python-based calculation logic.*
