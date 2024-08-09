from tkinter import *
from random import randint
from tkinter import messagebox

FONT = ("Arial", 10)
password = ''

window = Tk()
window.title("Password Saver")
window.config(pady=50, padx=50)


# -------------------- GENERATE & ADD METHODS ------------------------- #

def generate_password():
    global password
    password = [chr(randint(48, 122)) for i in range(12)]
    password = "".join(password)
    password_entry.insert(0, password)


def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror("error", "Please enter all the fields")
    else:
        is_ok = messagebox.askokcancel("are you sure of these infos?",
                                       f"website: {website} \npassword: {password} \nemail: {email}")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.writelines(f"{website} , {password} , {email}\n")
                messagebox.showinfo("Accepted", "your information has been saved successfully")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(END, "@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, columnspan=2)

website_label = Label(text="website:")
website_label.grid(row=1, column=0, sticky=E, pady=5)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W, pady=5)
website_entry.focus()

email_label = Label(text="email/UserName:")
email_label.grid(row=2, column=0, sticky=E, pady=5)

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W, pady=5)
email_entry.insert(0, "@gmail.com")

password_label = Label(text="password:")
password_label.grid(row=3, column=0, sticky=E, pady=5)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W, pady=5)
password_entry.insert(0, password)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky=W, pady=5)

add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
