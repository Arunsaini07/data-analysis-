import tkinter as tk

# Function to update the expression
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function for backspace
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Function to evaluate expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Display
entry = tk.Entry(
    root,
    font=("Arial", 24),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button layout
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["⌫", "0", ".", "="]
]

# Create buttons
for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):

        if text == "=":
            cmd = calculate
        elif text == "C":
            cmd = clear
        elif text == "⌫":
            cmd = backspace
        else:
            cmd = lambda x=text: click(x)

        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            width=5,
            height=2,
            command=cmd
        )

        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Make grid responsive
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
