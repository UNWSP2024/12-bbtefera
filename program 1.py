import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(entry_gallons.get())
        miles = float(entry_miles.get())
        if gallons <= 0:
            raise ValueError("Gallons must be greater than 0.")
        mpg = miles / gallons
        label_result.config(text=f"MPG: {mpg:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

window = tk.Tk()
window.title("MPG Calculator")
window.geometry("300x200")

tk.Label(window, text="Gallons of Gas:").pack(pady=5)
entry_gallons = tk.Entry(window)
entry_gallons.pack()

tk.Label(window, text="Miles on Full Tank:").pack(pady=5)
entry_miles = tk.Entry(window)
entry_miles.pack()

tk.Button(window, text="Calculate MPG", command=calculate_mpg).pack(pady=10)

label_result = tk.Label(window, text="MPG: ")
label_result.pack(pady=5)

window.mainloop()
