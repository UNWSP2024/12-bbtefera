import tkinter as tk
from tkinter import messagebox

rates = { "Daytime (6:00 AM - 5:59 PM)": 0.02,
    "Evening (6:00 PM - 11:59 PM)": 0.12,
    "Off-Peak (12:00 AM - 5:59 AM)": 0.05}

def calculate_charge():
    try:
        minutes = float(entry_minutes.get())
        if minutes <= 0:
            raise ValueError("Minutes must be a positive number.")
        rate = rates[rate_var.get()]
        charge = minutes * rate
        messagebox.showinfo("Call Charge", f"Total charge: ${charge:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

window = tk.Tk()
window.title("Long-Distance Call Charges")
window.geometry("350x250")

tk.Label(window, text="Select Rate Category:", font=("Arial", 12, "bold")).pack(pady=5)

rate_var = tk.StringVar(value="Daytime (6:00 AM - 5:59 PM)")
for rate_name in rates.keys():
    tk.Radiobutton(window, text=rate_name, variable=rate_var, value=rate_name).pack(anchor='w')

tk.Label(window, text="Enter Call Duration (minutes):").pack(pady=5)
entry_minutes = tk.Entry(window)
entry_minutes.pack()

tk.Button(window, text="Calculate Charge", command=calculate_charge).pack(pady=10)

window.mainloop()
