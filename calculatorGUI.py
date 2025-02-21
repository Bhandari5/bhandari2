import tkinter as tk 
from tkinter import messagebox #tkinter provides GUI components (buttons, input fields, etc.)
#messagebox is used to display error messages (e.g., division by zero).


class Calculator:#Calculator is a class that represents my calculator.
    def __init__(self, root):#__init__(self, root) is the constructor. It initializes the GUI when we create an instance of the Calculator class.
        """Initialize the calculator GUI"""
        self.root = root 
        self.root.title(" Calculator of Sijan Bhandari ")# set the tittle of the window
        self.root.geometry("400x500")# set the geometry 
        self.root.resizable(False, False) #makes the window non-resizable, so users cannot change its size.

        self.expression = ""   # Stores the mathematical equation as a string.
        self.input_text = tk.StringVar()  #is a Tkinter variable that links to the input field and displays the expression.

        
        self.root.bind("<Key>", self.keyboard_input)#This line binds keyboard keys to specific actions.
#When you press any key, it calls the keyboard_input() method to handle the key.

    
        entry_frame = tk.Frame(self.root)#is a frame that holds the input field.
        entry_frame.pack()
        input_field = tk.Entry(entry_frame, textvariable=self.input_text, font=('Arial', 24),
                               justify='right', bd=10, relief=tk.SUNKEN, width=20)
        input_field.grid(row=0, column=0, ipadx=8, ipady=10, columnspan=4)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        buttons = [
            ("7", 1, 0, "blue"), ("8", 1, 1, "blue"), ("9", 1, 2, "blue"), ("/", 1, 3, "white"),
            ("4", 2, 0, "blue"), ("5", 2, 1, "blue"), ("6", 2, 2, "blue"), ("*", 2, 3, "pink"),
            ("1", 3, 0, "blue"), ("2", 3, 1, "blue"), ("3", 3, 2, "blue"), ("-", 3, 3, "yellow"),
            ("0", 4, 0, "blue"), (".", 4, 1, "blue"), ("C", 4, 2, "red"), ("+", 4, 3, "blue"),
            ("=", 5, 0, 4, "green")
        ]

        for button_data in buttons:#create_button_callback(text) ensures that when a button is clicked, the corresponding action (digit or operator) is processed.

            text, row, col, *extras = button_data
            colspan = extras[0] if len(extras) > 1 else 1
            color = extras[-1] if extras else "lightgray"
            button = tk.Button(button_frame, text=text, font=('Arial', 18), width=5, bg=color,
                               command=self.create_button_callback(text))
            button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

    def create_button_callback(self, char):#Ensures each button press is processed correctly by avoiding late binding issues.
        """Fixes lambda late binding"""
        return lambda: self.on_button_click(char)

    def keyboard_input(self, event):
        """Handles keyboard input"""
        key = event.char
        if key in "0123456789+-*/.=":
            self.on_button_click(key)
        elif key == "\r":  # Enter key for "="
            self.on_button_click("=")
        elif key == "\x09":  # Backspace key to delete last character
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)

    def on_button_click(self, char):
        """Handles button clicks and updates display"""
        if char == "=":
            self.calculate_result()
        elif char == "C":
            self.clear_display()
        else:
            # Prevent consecutive operators (like ++ or //)
            if char in "+-*/" and (not self.expression or self.expression[-1] in "+-*/"):
                return
            self.expression += str(char)
            self.input_text.set(self.expression)

    def calculate_result(self):
        """Evaluates the entered expression"""
        try:
            result = eval(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.clear_display()
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            self.clear_display()

    def clear_display(self):
        """Clears the display and resets expression"""
        self.expression = ""
        self.input_text.set("")

# Run the Calculator App
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()#Keeps the GUI running with root.mainloop().


