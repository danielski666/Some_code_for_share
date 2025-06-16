import json
import tkinter as tk
import pyperclip
from tkinter.constants import END
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Info", message="Password copied to the clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    mail = entry_username.get()
    password = entry_password.get()
    new_data = {website:
                    {"email": mail,
                     "password": password
                     }
                }

    if website and mail and password:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()
    else:
        messagebox.showwarning("Oooops", "Please, fill all fields!")


# ---------------------------- Search creds ------------------------------- #
def search_password():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title="Your Credentials", message=f"Your credentials for {website}:\n"
                                                                  f"e-mail: {data[website]['email']}\n"
                                                                  f"password: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    except KeyError:
        messagebox.showerror(title="No saved website", message=f"No details for the website: {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = tk.Canvas(width=200, height=200)
logo_image = tk.PhotoImage(file="logo.png")
canvas.config(highlightthickness=0)  # instead of border = 0
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

label_website = tk.Label(text="Website:")
label_website.grid(row=1, column=0)

label_username = tk.Label(text="Email/Username")
label_username.grid(row=2, column=0)

label_password = tk.Label(text="Password")
label_password.grid(row=3, column=0)

entry_website = tk.Entry(width=23)
entry_website.grid(row=1, column=1, columnspan=2, sticky="w")
entry_website.focus()

entry_username = tk.Entry(width=43)
entry_username.grid(row=2, column=1, columnspan=2, sticky="w")
entry_username.insert(0, "example@gmail.com")

entry_password = tk.Entry(width=23)
entry_password.grid(row=3, column=1, sticky="w")

button_generate = tk.Button(text=" Generate Password ", command=generate_password)
button_generate.grid(row=3, column=1, columnspan=2, sticky="e")

button_add = tk.Button(text="Add", justify="center", width="36", command=save)
button_add.grid(row=5, column=1, columnspan=2, sticky="w")

button_search = tk.Button(text="Search", width=15, command=search_password)
button_search.grid(row=1, column=1, columnspan=2, sticky="e")

window.mainloop()
