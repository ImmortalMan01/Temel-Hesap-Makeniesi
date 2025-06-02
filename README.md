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

The GUI is organized with a display area at the top, followed by rows of buttons for various operations.

-   **Display Area:** A large entry field at the top shows the current expression being built and the results of calculations.

-   **Memory Buttons (Top Row):**
    -   `MC` (Memory Clear): Resets the value stored in memory to 0.
    -   `MR` (Memory Recall): Inserts the current memory value into the expression. Can be used as a number in your calculations.
    -   `MS` (Memory Store): Evaluates the current expression in the display and stores the result into memory.
    -   `M+` (Memory Add): Evaluates the current expression and adds the result to the value already in memory.
    -   `M-` (Memory Subtract): Evaluates the current expression and subtracts the result from the value already in memory.
    *Memory functions are useful for storing intermediate results or frequently used numbers.*

-   **Control and Basic Function/Operator Buttons (Second Row from Top):**
    -   `C` (Clear): Clears the entire current expression and resets the display.
    -   `CE` (Clear Entry): Clears the last character entered into the expression (simplified version).
    -   `sqrt`: Square Root function.
    -   `pow`: Exponentiation operator (use as `number pow exponent`).

-   **Number Buttons (0-9, .):** Standard numeric input and decimal point, arranged in a typical keypad layout.

-   **Operator Buttons:**
    -   Basic Arithmetic: `+`, `-`, `*`, `/` (generally found alongside number rows).

-   **Advanced Function Buttons (Dedicated Rows):**
    -   `log`: Natural Logarithm (base e).
    -   `log10`: Base-10 Logarithm.
    -   `sin`, `cos`, `tan`: Trigonometric functions (input angles in radians).

-   **Parentheses and Scientific Constants Buttons (Bottom Rows):**
    -   `(` and `)`: For grouping expressions.
    -   **Scientific Constants:**
        -   `π` (Pi): Inserts the value of Pi (approx. 3.14159).
        -   `e`: Inserts Euler's number (approx. 2.71828).
        -   `c`: Inserts the speed of light in vacuum (approx. 2.998e8 m/s).
        -   `h`: Inserts Planck's constant (approx. 6.626e-34 J*s).
        -   `G`: Inserts the Gravitational constant (approx. 6.674e-11 N*m²/kg²).
    *Pressing a constant button inserts its symbol (e.g., "pi", "e", "c_light") into the expression, which is then evaluated using its defined value.*

-   **Equals Button (`=`):** Evaluates the current expression displayed.

**How to Use (General):**
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
