import tkinter as tk


def button_clicked():
    # my_label["text"] = "I got clicked."
    my_label.config(text=entry.get())


window = tk.Tk()
window.title("Firs GUI program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# label:
my_label = tk.Label(text="I Am a LABEL", font=("Arial", 22))
my_label.grid(column=0, row=0)


# Button

button = tk.Button(text="ClickMe", command=button_clicked)
button.grid(column=1, row=1)

new_button = tk.Button(text="NewButton")
new_button.grid(column=2, row=0)

# Entry

entry = tk.Entry(width=10)
entry.grid(row=2, column=3)

# Text


# Spinbox




window.mainloop()
