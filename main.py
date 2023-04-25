# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(0, nr_letters)]
    password_symbols = [random.choice(numbers) for _ in range(0, nr_symbols)]
    password_numbers = [random.choice(symbols) for _ in range(0, nr_numbers)]

    password_list = password_numbers + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter
from tkinter import messagebox
import json


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="All fields must be filled.")
    else:
        try:
            with open("my_data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("my_data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("my_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

def find_password():
    website = website_entry.get()
    try:
        with open("my_data.json") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="No website", message="This website is not added yet.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")


canvas = tkinter.Canvas(width=180, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website: ", padx=10)
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = tkinter.Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "haris@gmail.com")

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
search_button = tkinter.Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, columnspan=1)

gen_pass = tkinter.Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
