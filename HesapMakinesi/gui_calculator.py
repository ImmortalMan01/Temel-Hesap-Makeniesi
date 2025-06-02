import tkinter as tk
from tkinter import messagebox
import math # For math.pi and potentially other functions if not in calc_logic
import calculator as calc_logic # Core calculator functions

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator") # Simplified title
        master.geometry("420x620") # Slightly adjusted for more padding/consistent look
        master.resizable(False, False) 

        # Configure root window's background color (optional)
        # master.configure(bg="#f0f0f0") # Light gray background

# Define physical constants at the class or module level for clarity
SPEED_OF_LIGHT = 299792458  # m/s
PLANCK_CONSTANT = 6.62607015e-34  # J*s
GRAVITATIONAL_CONSTANT = 6.67430e-11  # N*m^2/kg^2

        # Expression string
        self.expression = ""
        self.memory = 0.0

        # Setup for eval context
        self.eval_context = {
            # Custom functions from calc_logic
            'sqrt': calc_logic.square_root,
            'log': calc_logic.log_natural, # GUI 'log' maps to natural log
            'ln': calc_logic.log_natural,  # Allow 'ln' as well if typed or from future button
            'log10': calc_logic.log_base10,
            'sin': calc_logic.sine,
            'cos': calc_logic.cosine,
            'tan': calc_logic.tangent,
            # Standard math constants/functions
            'pi': math.pi,
            'e': math.e,
            'c_light': SPEED_OF_LIGHT,
            'h_planck': PLANCK_CONSTANT,
            'G_grav': GRAVITATIONAL_CONSTANT,
            # Note: 'pow' is handled by replacing "pow" with "**" in the expression string
        }


        # Display Entry widget (Increased font size, padding, and defined background)
        self.display_var = tk.StringVar()
        display_font = ('Arial', 28, 'bold')
        display_entry = tk.Entry(master, textvariable=self.display_var, font=display_font,
                                 bd=10, relief=tk.SUNKEN, width=14, # Using relief for a bit of depth
                                 state='readonly', justify='right', bg="#ffffff", fg="#000000") # White bg, black text
        # columnspan adjusted to 5 as we will have 5 columns for memory buttons
        display_entry.grid(row=0, column=0, columnspan=5, pady=20, padx=10, sticky="nsew")


        # --- Button Frame and Definitions ---
        button_frame = tk.Frame(master) 
        button_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

        # Define button texts, their grid positions (row, col), type, and any specific styling
        # (text, row, col, type, [optional: colspan])
        # Memory row now has 5 buttons. Other rows will have 4 buttons, centered or spanned.
        # For simplicity, we'll let the 5th column be empty for rows with 4 buttons.
        buttons = [
            # Memory Row (row 0) - 5 columns
            ('MC', 0, 0, 'memory'), ('MR', 0, 1, 'memory'), ('MS', 0, 2, 'memory'), 
            ('M+', 0, 3, 'memory'), ('M-', 0, 4, 'memory'),
            # Row 1 (Control and first functions/operators) - 4 main columns, 5th empty
            ('C', 1, 0, 'clr'), ('CE', 1, 1, 'clr_entry'), ('sqrt', 1, 2, 'func'), ('pow', 1, 3, 'op'),
            # Empty for (1,4) or a new button could go here if needed
            # Row 2 (was 1)
            ('7', 2, 0, 'num'), ('8', 2, 1, 'num'), ('9', 2, 2, 'num'), ('/', 2, 3, 'op'),
            # Row 3 (was 2)
            ('4', 3, 0, 'num'), ('5', 3, 1, 'num'), ('6', 3, 2, 'num'), ('*', 3, 3, 'op'),
            # Row 4 (was 3)
            ('1', 4, 0, 'num'), ('2', 4, 1, 'num'), ('3', 4, 2, 'num'), ('-', 4, 3, 'op'),
            # Row 5 (was 4)
            ('0', 5, 0, 'num'), ('.', 5, 1, 'num'), ('=', 5, 2, 'eq'), ('+', 5, 3, 'op'),
            # Row 6 (was 5 - Advanced functions)
            ('log', 6, 0, 'func'), ('log10', 6, 1, 'func'), ('sin', 6, 2, 'func'), ('cos', 6, 3, 'func'),
            # Row 7 (was 6) - Parentheses and existing constants
            ('(', 7, 0, 'char'), 
            (')', 7, 1, 'char'), 
            ('π', 7, 2, 'const', 'pi'), 
            ('e', 7, 3, 'const', 'e'),
            # Row 8 (New row for additional scientific constants)
            ('c', 8, 0, 'const', 'c_light'),   # Speed of Light
            ('h', 8, 1, 'const', 'h_planck'),  # Planck's Constant
            ('G', 8, 2, 'const', 'G_grav'),   # Gravitational Constant
            # Potentially 2 empty slots here in column 3 and 4 for this new row
        ]
        
        button_font = ('Arial', 12) # Further reduced font size for more rows
        button_bold_font = ('Arial', 12, 'bold') 

        # Create and place buttons in the button_frame
        for i, btn_info in enumerate(buttons):
            text_on_btn = btn_info[0]
            r, c, btn_type = btn_info[1], btn_info[2], btn_info[3]
            
            # Determine value passed to on_button_click: use text_on_btn by default
            value_for_command = text_on_btn
            if len(btn_info) > 4: # If a specific value for command is provided (like "pi" for 'π')
                value_for_command = btn_info[4]

            # Default styling
            fg_color = 'black'
            bg_color = '#f7f7f7' # Off-white for numbers
            font_style = button_font

            if btn_type == 'op':
                bg_color = '#e0e0e0' # Light grey for operators
                font_style = button_bold_font
            elif btn_type == 'func':
                bg_color = '#d3d3d3' # Slightly darker grey for functions
                font_style = button_bold_font
            elif btn_type == 'eq':
                bg_color = '#4CAF50' # Green for equals
                fg_color = 'white'
                font_style = button_bold_font
            elif btn_type == 'clr' or btn_type == 'clr_entry':
                bg_color = '#f44336' # Red for clear buttons
                fg_color = 'white'
                font_style = button_bold_font
            elif btn_type == 'char' or btn_type == 'const': # Parentheses, Pi
                bg_color = '#e0e0e0' 
                font_style = button_bold_font
            elif btn_type == 'memory':
                bg_color = '#FF9800' # Orange for memory buttons
                fg_color = 'white'
                font_style = button_bold_font


            # Override styles if provided in btn_info (optional feature, not used in current buttons list)
            if len(btn_info) > 4 and btn_info[4]:
                bg_color = btn_info[4]
            if len(btn_info) > 5 and btn_info[5]:
                font_style = btn_info[5]

            # Consistent padding and make buttons expand
            # relief=tk.RAISED for a bit of 3D effect on buttons
            current_colspan = 1
            # if len(btn_info) > 4 and isinstance(btn_info[4], int) : # Check if colspan is provided
            #     current_colspan = btn_info[4]
                
            button = tk.Button(button_frame, text=text_on_btn, font=font_style, fg=fg_color, bg=bg_color,
                               relief=tk.RAISED, bd=2,
                               command=lambda v=value_for_command, bt=btn_type: self.on_button_click(v, bt))
            button.grid(row=r, column=c, columnspan=current_colspan, sticky="nsew", padx=3, pady=3) 


        # Configure column and row weights for button_frame for uniform button sizing
        # Now we have 5 columns for the button_frame due to memory buttons
        for i in range(5): 
            button_frame.grid_columnconfigure(i, weight=1)
        # And 9 rows of buttons now (0-8)
        for i in range(9): 
            button_frame.grid_rowconfigure(i, weight=1)
            
        # Configure master window's row weights (display row 0, button_frame row 1)
        master.grid_rowconfigure(0, weight=0) # Display row should not expand as much
        master.grid_rowconfigure(1, weight=1) # Button frame row takes remaining space
        master.grid_columnconfigure(0, weight=1) # Ensure master column expands

        # Initialize display
        self.display_var.set("0")
        self.just_calculated = False # Flag to clear expression on new number input after '='

    def _evaluate_expression(self, expression_str):
        """Helper to evaluate an expression string, returns number or raises exception."""
        if not expression_str:
            # Attempting to evaluate an empty string often happens with MS/M+/M- if display is "0" or "Error"
            # We can either return 0.0 or raise a specific error.
            # Let's try to evaluate what's literally in the display if expression_str is empty
            # This is relevant if user clears expression then hits MS with "0" in display.
            current_display = self.display_var.get()
            if current_display == "Error" : # Add more specific error checks if needed
                 raise ValueError("Cannot store/use error message in memory.")
            try:
                 return float(current_display) # Try to convert display directly if expression is empty
            except ValueError:
                 raise ValueError("Invalid value in display for memory operation.")


        eval_expression = expression_str.replace("pow", "**")
        # pi is handled by eval_context
        
        # Important: Security with eval. Restrict builtins.
        # Allowing specific math functions from calc_logic via eval_context.
        result = eval(eval_expression, {"__builtins__": {}}, self.eval_context)
        return result

    def on_button_click(self, value, btn_type):
        current_display_text = self.display_var.get()

        if btn_type == 'clr': # 'C'
            self.expression = ""
            self.display_var.set("0")
            self.just_calculated = False
        
        elif btn_type == 'clr_entry': # 'CE' - Simplified: clear last character
            if self.expression:
                self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
            self.just_calculated = False

        elif btn_type == 'eq':
            if not self.expression:
                self.display_var.set("0")
                return
            try:
                result = self._evaluate_expression(self.expression)
                if isinstance(result, float) and result.is_integer():
                    result_str = str(int(result))
                else:
                    result_str = f"{result:.10g}"
                self.display_var.set(result_str)
                self.expression = result_str
                self.just_calculated = True
            except ZeroDivisionError:
                self.display_var.set("Error: Division by zero")
                messagebox.showerror("Calculation Error", "Cannot divide by zero.")
                self.expression = "" 
                self.just_calculated = True
            except (SyntaxError, NameError) as e:
                self.display_var.set("Error: Invalid syntax")
                messagebox.showerror("Calculation Error", f"Invalid expression syntax or unknown function: {e}")
                self.expression = ""
                self.just_calculated = True
            except (ValueError, TypeError) as e: 
                self.display_var.set("Error: Math domain/type")
                messagebox.showerror("Calculation Error", f"Mathematical error: {e}")
                self.expression = ""
                self.just_calculated = True
            except Exception as e:
                self.display_var.set("Error: Unknown")
                messagebox.showerror("Calculation Error", f"An unexpected error occurred: {e}")
                self.expression = ""
                self.just_calculated = True
            return 

        elif btn_type == 'memory':
            try:
                if value == 'MC':
                    self.memory = 0.0
                    print("Memory Cleared") # For debugging, no direct display change
                elif value == 'MR':
                    # Treat MR like number input
                    mem_str = str(self.memory)
                    if mem_str.endswith(".0"): mem_str = mem_str[:-2] # Clean display for whole numbers
                    
                    if self.just_calculated or (current_display_text == "0" and self.expression == "0"):
                        self.expression = mem_str
                    else:
                         # If last char in expression is a digit or ')', add '*' for implicit multiplication
                        if self.expression and self.expression[-1].isdigit() or self.expression[-1] == ')':
                            self.expression += " * " + mem_str
                        else: # Otherwise, just append (e.g. after an operator or '(')
                            self.expression += mem_str
                    self.display_var.set(self.expression)
                    self.just_calculated = False
                
                elif value == 'MS':
                    # Use current expression on display for MS
                    # If display is "0" and expression is empty, store 0.
                    # If display is an error, do not store.
                    if current_display_text == "Error": # Add more specific error checks if needed
                        messagebox.showerror("Memory Error", "Cannot store error value.")
                        return
                    
                    # We want to store the evaluated value of the current expression, or current number on display
                    # If expression is empty, it means user might have typed '0' or it's the initial state.
                    # Or if an error just occurred and display shows "Error"
                    val_to_store_str = self.expression if self.expression else current_display_text
                    if not val_to_store_str and current_display_text == "0": # Store 0 if expression is empty and display is 0
                        self.memory = 0.0
                    else:
                        self.memory = self._evaluate_expression(val_to_store_str)
                    print(f"Memory Stored: {self.memory}") # Debug
                    self.just_calculated = True 

                elif value == 'M+':
                    val_to_add = self._evaluate_expression(self.expression if self.expression else current_display_text)
                    self.memory += val_to_add
                    print(f"Memory Add: {self.memory}") # Debug
                    self.just_calculated = True 
                
                elif value == 'M-':
                    val_to_subtract = self._evaluate_expression(self.expression if self.expression else current_display_text)
                    self.memory -= val_to_subtract
                    print(f"Memory Subtract: {self.memory}") # Debug
                    self.just_calculated = True

            except ValueError as e: 
                messagebox.showerror("Memory Operation Error", str(e))
            except Exception as e: # Catch other eval errors for M ops
                messagebox.showerror("Memory Operation Error", f"Could not perform memory operation: {e}")
            # No display_var.set here for MC/MS/M+/M- unless we want to show memory content,
            # which is not standard. MR handles display.
            return # Skip default print at end of on_button_click for memory ops

        elif btn_type == 'num':
            if self.just_calculated or current_display_text == "0" and value != ".":
                self.expression = value # Start new expression
                self.just_calculated = False
            elif value == '.':
                # Prevent multiple decimal points in the current number segment
                # This requires finding the last number segment
                last_segment = ""
                for char in reversed(self.expression):
                    if char in " +/-*()": # Stop at operator or parenthesis
                        break
                    last_segment = char + last_segment
                if '.' not in last_segment:
                    self.expression += value
            else:
                self.expression += value
            self.display_var.set(self.expression)

        elif btn_type == 'op': # Includes 'pow'
            if self.expression: # Allow starting with '-' for negative numbers
                # Add space around operators for better parsing later (unless it's a starting negative)
                if value == '-' and not self.expression:
                     self.expression += value
                # Avoid double operators, or operator after opening parenthesis if not '-'
                elif self.expression[-1] not in [' ', '(', '+', '*', '/', 'w']: # 'w' from 'pow'
                    self.expression += f" {value} "
                elif value == '-' and self.expression.endswith('('): # Allow func(-
                    self.expression += value

            elif value == '-': # Allow starting expression with a negative number
                self.expression = value
            
            self.display_var.set(self.expression if self.expression else "0")
            self.just_calculated = False

        elif btn_type == 'func': # sqrt, log, log10, sin, cos, tan
            if self.just_calculated: # Start new expression if after '='
                self.expression = value + "("
            elif not self.expression or self.expression.endswith((' ', '(', '+', '-', '*', '/', 'w')):
                self.expression += value + "("
            else: # If there's a number before, multiply (e.g. 2sqrt(4) -> 2 * sqrt(4)) - advanced
                  # For now, just append, implies user must use operators explicitly
                  # Or, we can decide to overwrite or show error.
                  # Let's assume for now it's appended if it's after a number, though this isn't ideal.
                  # A better way might be to enforce an operator or start new.
                  # Simplified: if expression is not empty and doesn't end with operator/paren, add "*"
                if self.expression and not self.expression.endswith(tuple(' +/-*()')):
                     self.expression += " * " + value + "("
                else:
                    self.expression += value + "("

            self.display_var.set(self.expression if self.expression else "0")
            self.just_calculated = False
            
        elif btn_type == 'char': # Parentheses
            if self.just_calculated:
                self.expression = value
                self.just_calculated = False
            else:
                self.expression += value
            self.display_var.set(self.expression if self.expression else "0")

        elif btn_type == 'const': # 'pi', 'e'
            # 'value' here will be "pi" or "e"
            if self.just_calculated or (current_display_text == "0" and self.expression == "0"):
                self.expression = value 
            elif self.expression and not self.expression.endswith(tuple(' +/-*().')):
                self.expression += " * " + value 
            else:
                self.expression += value 
            self.display_var.set(self.expression)
            self.just_calculated = False
        
        # Final display update, if not handled by specific cases like '='
        # This was mostly integrated into each condition block to ensure "0" is shown when expression is empty.
        # However, a fallback might be useful if a new button type doesn't set display_var.
        # For now, existing logic should cover it.

        print(f"Button '{value}' (type: {btn_type}) clicked. Expression: '{self.expression}'")


if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()
