import tkinter as tk


def button_clicked():
    # my_label["text"] = "I got clicked."
    km = round(1.609 * float(entry.get()), 2)
    calculated_label.config(text=km)


window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(250, 150)
window.config(padx=20, pady=20)

# label:
equal_label = tk.Label(text="is equal to", font=("Arial", 10))
equal_label.grid(column=0, row=1)
miles_label = tk.Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)
km_label = tk.Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)
calculated_label = tk.Label(text="0", font=("Arial", 10))
calculated_label.grid(column=1, row=1)


# Button

button = tk.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry

entry = tk.Entry(width=10)
entry.grid(row=0, column=1)

window.mainloop()
