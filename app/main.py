import tkinter as tk
from tkinter import messagebox, simpledialog
import math
import matplotlib.pyplot as plt

def on_button_press(event):
    event.widget.config(bg="light grey")

def on_button_release(event):
    event.widget.config(bg="SystemButtonFace")  # Default button color on Windows

def on_main_button_release(event):
    on_button_release(event)
    click(event)

def evaluate_expression(expr):
    try:
        return eval(expr)
    except Exception:
        return "Error"

def advanced_operation(expr, op, exponent=None):
    try:
        value = float(expr)
        if op == "x²":
            return str(value ** 2)
        elif op == "√x":
            return str(math.sqrt(value))
        elif op == "1/x":
            return str(1 / value)
        elif op == "xʸ":
            if exponent is not None:
                return str(value ** exponent)
            else:
                return "Error"
        else:
            return "Error"
    except Exception:
        return "Error"

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_var.set("")
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

def open_advanced_functions():
    advanced_window = tk.Toplevel(root)
    advanced_window.title("Advanced Functions")
    advanced_window.geometry("300x400")

    def advanced_click(event):
        global expression
        text = event.widget.cget("text")
        try:
            if text == "x²":
                result = str(float(expression) ** 2)
            elif text == "√x":
                result = str(math.sqrt(float(expression)))
            elif text == "1/x":
                result = str(1 / float(expression))
            elif text == "xʸ":
                exponent = simpledialog.askfloat("Exponent", "Enter the exponent (y):")
                if exponent is not None:
                    result = str(float(expression) ** exponent)
                else:
                    return
            else:
                result = "Error"
            input_var.set(result)
            expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_var.set("")

    def on_advanced_button_release(event):
        on_button_release(event)
        advanced_click(event)

    def plot_graph():
        try:
            function = simpledialog.askstring("Input", "Enter a function of x (e.g., x**2, math.sin(x)):")
            if not function:
                messagebox.showerror("Error", "No function entered")
                return
            x = [i / 10 for i in range(-100, 101)]
            y = [eval(function.replace("x", f"({i})")) for i in x]
            plt.figure("Graph")
            plt.plot(x, y, label=f"y = {function}")
            plt.axhline(0, color="black", linewidth=0.5)
            plt.axvline(0, color="black", linewidth=0.5)
            plt.grid(color="gray", linestyle="--", linewidth=0.5)
            plt.legend()
            plt.title("Graph")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid function: {e}")

    advanced_buttons = [
        "x²", "√x", "1/x", "xʸ", "Graph"
    ]

    row = 0
    col = 0
    for button in advanced_buttons:
        btn = tk.Button(advanced_window, text=button, font="Arial 15", relief="ridge", height=2, width=5)
        btn.grid(row=row, column=col, padx=5, pady=5)
        btn.bind("<ButtonPress-1>", on_button_press)
        if button == "Graph":
            btn.config(command=plot_graph)
            btn.bind("<ButtonRelease-1>", on_button_release)
        else:
            btn.bind("<ButtonRelease-1>", on_advanced_button_release)
        col += 1
        if col > 2:
            col = 0
            row += 1

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""
input_var = tk.StringVar()

entry = tk.Entry(root, textvar=input_var, font="Arial 20", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 0
col = 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15", relief="ridge", height=2, width=5)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<ButtonPress-1>", on_button_press)
    btn.bind("<ButtonRelease-1>", on_main_button_release)
    col += 1
    if col > 3:
        col = 0
        row += 1

advanced_button = tk.Button(root, text="Advanced", font="Arial 15", relief="ridge", height=2, width=10, command=open_advanced_functions)
advanced_button.pack(pady=10)

root.mainloop()