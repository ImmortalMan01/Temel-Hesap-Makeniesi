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

        # Expression string
        self.expression = ""

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
            # 'e': math.e, # Could add if there's an 'e' button
            # Note: 'pow' is handled by replacing "pow" with "**" in the expression string
        }


        # Display Entry widget (Increased font size, padding, and defined background)
        self.display_var = tk.StringVar()
        display_font = ('Arial', 28, 'bold')
        display_entry = tk.Entry(master, textvariable=self.display_var, font=display_font,
                                 bd=10, relief=tk.SUNKEN, width=14, # Using relief for a bit of depth
                                 state='readonly', justify='right', bg="#ffffff", fg="#000000") # White bg, black text
        # columnspan adjusted to 4 as we have 4 columns of buttons now
        display_entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")


        # --- Button Frame and Definitions ---
        button_frame = tk.Frame(master) # bg="#f0f0f0" if master bg is set
        button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        # Define button texts, their grid positions (row, col), type, and any specific styling
        # columnspan and rowspan are mostly 1 now, can be specified if needed
        # (text, row, col, type, [optional: bg_color_override, font_style_override])
        buttons = [
            # Row 1
            ('C', 0, 0, 'clr'), ('CE', 0, 1, 'clr_entry'), ('sqrt', 0, 2, 'func'), ('pow', 0, 3, 'op'),
            # Row 2
            ('7', 1, 0, 'num'), ('8', 1, 1, 'num'), ('9', 1, 2, 'num'), ('/', 1, 3, 'op'),
            # Row 3
            ('4', 2, 0, 'num'), ('5', 2, 1, 'num'), ('6', 2, 2, 'num'), ('*', 2, 3, 'op'),
            # Row 4
            ('1', 3, 0, 'num'), ('2', 3, 1, 'num'), ('3', 3, 2, 'num'), ('-', 3, 3, 'op'),
            # Row 5
            ('0', 4, 0, 'num'), ('.', 4, 1, 'num'), ('=', 4, 2, 'eq'), ('+', 4, 3, 'op'),
            # Row 6 (Advanced functions)
            ('log', 5, 0, 'func'), ('log10', 5, 1, 'func'), ('sin', 5, 2, 'func'), ('cos', 5, 3, 'func'),
            # Row 7
            ('tan', 6, 0, 'func'), ('(', 6, 1, 'char'), (')', 6, 2, 'char'), ('π', 6, 3, 'const')
        ]
        
        button_font = ('Arial', 16) # Slightly larger and consistent font
        button_bold_font = ('Arial', 16, 'bold')

        # Create and place buttons in the button_frame
        for i, btn_info in enumerate(buttons):
            text, r, c, btn_type = btn_info[:4]
            
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


            # Override styles if provided in btn_info (optional feature, not used in current buttons list)
            if len(btn_info) > 4 and btn_info[4]:
                bg_color = btn_info[4]
            if len(btn_info) > 5 and btn_info[5]:
                font_style = btn_info[5]

            # Consistent padding and make buttons expand
            # relief=tk.RAISED for a bit of 3D effect on buttons
            button = tk.Button(button_frame, text=text, font=font_style, fg=fg_color, bg=bg_color,
                               relief=tk.RAISED, bd=2,
                               command=lambda t=text, bt=btn_type: self.on_button_click(t, bt))
            # Using consistent padx/pady for the grid cells within button_frame
            button.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)


        # Configure column and row weights for button_frame for uniform button sizing
        # Now we have 4 columns of buttons
        for i in range(4): 
            button_frame.grid_columnconfigure(i, weight=1)
        # And 7 rows of buttons
        for i in range(7): 
            button_frame.grid_rowconfigure(i, weight=1)
            
        # Configure master window's row weights (display row 0, button_frame row 1)
        master.grid_rowconfigure(0, weight=0) # Display row should not expand as much
        master.grid_rowconfigure(1, weight=1) # Button frame row takes remaining space
        master.grid_columnconfigure(0, weight=1) # Ensure master column expands

        # Initialize display
        self.display_var.set("0")
        self.just_calculated = False # Flag to clear expression on new number input after '='

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
                # Pre-process the expression string for eval()
                eval_expression = self.expression.replace("pow", "**")
                # Ensure 'pi' (from button) is treated as math.pi if not already handled by direct eval_context name
                # This is more robust if 'pi' is part of a larger expression e.g. "pi/2"
                # However, direct mapping 'pi': math.pi in eval_context is generally better.
                # Let's assume 'pi' in expression will be correctly handled by context.
                # If functions like 'sqrt(' are directly in expression, they should map in eval_context.
                
                # Important: Security with eval. Restrict builtins.
                result = eval(eval_expression, {"__builtins__": {}}, self.eval_context)

                # Format result: show as int if it's a whole number float
                if isinstance(result, float) and result.is_integer():
                    result_str = str(int(result))
                else:
                    result_str = f"{result:.10g}" # Format to reasonable precision, remove trailing zeros

                self.display_var.set(result_str)
                self.expression = result_str # Store result for potential further calculation
                self.just_calculated = True
            
            except ZeroDivisionError:
                self.display_var.set("Error: Division by zero")
                messagebox.showerror("Calculation Error", "Cannot divide by zero.")
                self.expression = "" # Clear expression on error
                self.just_calculated = True # Allow starting fresh
            except (SyntaxError, NameError) as e: # NameError if function not in context
                self.display_var.set("Error: Invalid syntax")
                messagebox.showerror("Calculation Error", f"Invalid expression syntax or unknown function: {e}")
                self.expression = ""
                self.just_calculated = True
            except (ValueError, TypeError) as e: # Errors from math functions themselves
                self.display_var.set("Error: Math domain/type")
                messagebox.showerror("Calculation Error", f"Mathematical error: {e}")
                self.expression = ""
                self.just_calculated = True
            except Exception as e:
                self.display_var.set("Error: Unknown")
                messagebox.showerror("Calculation Error", f"An unexpected error occurred: {e}")
                self.expression = ""
                self.just_calculated = True
            return # Skip the final print for '=' button

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

        elif btn_type == 'const': # 'π'
            # Similar to numbers, can start new expression or append
            if self.just_calculated or (current_display_text == "0" and self.expression == "0"): # check self.expression too
                self.expression = "pi" 
            elif self.expression and not self.expression.endswith(tuple(' +/-*().')): # also check for dot
                self.expression += " * pi" 
            else:
                self.expression += "pi" # pi is a name in eval_context
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
