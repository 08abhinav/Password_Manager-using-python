from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

BLUE = "#e6ffff"
PINK = "#ffe5e5"
FONT = ("Arial", 16, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator 
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_letters = [choice(letters) for i in range(randint(8, 10))]
    list_numbers = [choice(symbols) for j in range(randint(2, 4))]
    list_symbols = [choice(numbers) for k in range(randint(2, 4))]

    password_list = list_symbols + list_numbers + list_letters
    shuffle(password_list)

    password = "".join(password_list)
    if entry_web.get() == "":
        messagebox.showwarning(title='Incomplete data', message="Incomplete information")
    else:
        entry_pass.insert(0, password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = entry_web.get()
    user = entry_user.get()
    passw = entry_pass.get()
    dic = {
        web: {
            "email": user,
            "password": passw
        }
    }
    error = entry_web.get() == "" or entry_pass.get() == ""
    if error:
        messagebox.showwarning(title="Error", message="Please fill mandatory fields")
    else:
        try:
            with open("data.json", 'r') as pws:
                data = json.load(pws)
        except FileNotFoundError:
            with open("data.json", 'w') as pws:
                json.dump(dic, pws, indent=4)
        else:
            data.update(dic)

            with open("data.json", 'w') as pws:
                json.dump(data, pws, indent=4)
        finally:
            entry_web.delete(0, END)
            entry_pass.delete(0, END)


# ---------------------------- SEARCH --------------------------------- #

def search():
    web = entry_web.get()
    try:
        with open('data.json') as data:
            content = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No file found")
    else:
        if web in content:
            email = content[web]['email']
            passw = content[web]['password']
            messagebox.showinfo(title=web, message=f"Email: {email}\n Password: {passw}")
        else:
            messagebox.showerror(title='Error', message=f"No details for {web} found.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=BLUE)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.config(bg=BLUE)
canvas.create_image(100, 100, image=img)
canvas.grid(row=2, column=2)

# Labels
website = Label(text="Website:", font=FONT)
website.grid(row=3, column=1)
website.config(bg=BLUE)

username = Label(text="Email/Username:", font=FONT)
username.grid(row=4, column=1)
username.config(bg=BLUE)

password = Label(text="Password:", font=FONT)
password.grid(row=5, column=1)
password.config(bg=BLUE)

# Entries
entry_web = Entry(width=35)
entry_web.grid(row=3, column=2, columnspan=2)
entry_web.get()
entry_web.focus()

entry_user = Entry(width=35)
entry_user.grid(row=4, column=2, columnspan=2)
entry_user.insert(0, 'example@gmail.com')
entry_user.get()

entry_pass = Entry(width=21)
entry_pass.grid(row=5, column=2)
entry_pass.get()

entry_user.get()
entry_web.get()
entry_pass.get()
# Buttons
Generate_button = Button(text="Generate Password", command=generate_password)
Generate_button.grid(row=5, column=4)
Generate_button.config(bg=PINK)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=6, column=2, columnspan=2)
add_button.config(bg=PINK)

search_button = Button(text="Search", width=10, command=search)
search_button.grid(row=3, column=3)
search_button.config(bg=PINK)
window.mainloop()
