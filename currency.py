import tkinter as tk
from tkinter import ttk
import requests

API_KEY = 'fca_live_1LM6l5w2yrNhXUYnSxx3VPXPgkMZi01GcoiEP3mp'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(amount, base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try: 
        response = requests.get(url)
        data = response.json()
        rates = data["data"]
        converted_values = {ticker: value * amount for ticker, value in rates.items()}
        return converted_values
    except:
        print("Invalid currency or amount.")
        return None

def on_convert():
    try:
        amount = float(amount_entry.get())
        base = currency_var.get()
        data = convert_currency(amount, base)
        if data:
            result_text.set("\n".join([f"{ticker}: {value}" for ticker, value in data.items()]))
    except ValueError:
        print("Invalid amount.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Set a custom style for the widgets
style = ttk.Style()
style.configure("My.TLabel", font=("Helvetica", 16), foreground="#333")

# Create and place widgets
title_label = ttk.Label(root, text="Karla's First Python Project: Currency Converter", style="My.TLabel")
title_label.pack(pady=10)

amount_label = ttk.Label(root, text="Enter the Amount:", style="My.TLabel")
amount_label.pack(pady=10)

amount_var = tk.StringVar()
amount_entry = ttk.Entry(root, textvariable=amount_var, font=("Helvetica", 14))
amount_entry.insert(0, "Enter amount")  # Placeholder text
amount_entry.pack(pady=10)

label = ttk.Label(root, text="Select the Base Currency:", style="My.TLabel")
label.pack(pady=10)

currency_var = tk.StringVar()
currency_dropdown = ttk.Combobox(root, textvariable=currency_var, values=CURRENCIES, font=("Helvetica", 14))
currency_dropdown.pack(pady=10)
currency_dropdown.set(CURRENCIES[0])  # Set the default value

convert_button = ttk.Button(root, text="Convert", command=on_convert, style="TButton")
convert_button.pack(pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, font=("Helvetica", 14), wraplength=400)
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
