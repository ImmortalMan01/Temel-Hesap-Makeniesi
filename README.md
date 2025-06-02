# Python GUI Calculator

This repository contains a Python-based calculator with a **Graphical User Interface (GUI)** built with Tkinter for ease of use. 
The application uses an underlying calculator logic engine found in `HesapMakinesi/calculator.py`.

---

## GUI Calculator

The GUI calculator provides a user-friendly, visual way to perform calculations. It's built using Python's standard Tkinter library.

### Running the Calculator

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

### Error Handling
If you enter an invalid expression or a calculation results in a mathematical error (e.g., division by zero, square root of a negative number):
-   The display will typically show "Error".
-   A popup dialog box will appear with a more specific error message.
The expression will usually be cleared or reset after an error, allowing you to start a new calculation.

---

## Unit Tests

The core calculator logic (used by the GUI) is unit-tested using Python's `unittest` module. The tests are located in `HesapMakinesi/test_calculator.py`. To run the tests, navigate to the `HesapMakinesi` directory and run:
```bash
python -m unittest test_calculator.py
```

---
*Historical Note: This project initially started as a very basic C++ calculator. It then evolved into a Python project with a command-line interface (CLI). Recently, the CLI was replaced by the current, more user-friendly GUI calculator, which still utilizes the same underlying Python-based calculation logic.*
