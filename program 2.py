import tkinter as tk

services = { "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Fluid": 100.00,
    "Inspection": 35.00,
    "Muffler Replacement": 200.00,
    "Tire Rotation": 20.00}

def calculate_total():
    total = 0.0
    for service, var in service_vars.items():
        if var.get():
            total += services[service]
    label_total.config(text=f"Total Charges: ${total:.2f}")

window = tk.Tk()
window.title("Joe's Automotive")
window.geometry("300x350")

tk.Label(window, text="Select Services:", font=("Arial", 12, "bold")).pack(pady=5)

service_vars = {}
for service, price in services.items():
    var = tk.BooleanVar()
    chk = tk.Checkbutton(window, text=f"{service} - ${price:.2f}", variable=var)
    chk.pack(anchor='w')
    service_vars[service] = var

tk.Button(window, text="Calculate Total", command=calculate_total).pack(pady=10)

label_total = tk.Label(window, text="Total Charges: $0.00", font=("Arial", 10, "bold"))
label_total.pack(pady=5)

window.mainloop()
