from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    alpha_lower = list(string.ascii_lowercase)
    alpha_upper = list(string.ascii_uppercase)
    symbols = ['~', ':', '+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
               '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    num_list = [str(num) for num in range(0, 10)]

    alpha_lower_choice = [random.choice(alpha_lower) for low in range(5)]
    alpha_upper_choice = [random.choice(alpha_upper) for upper in range(5)]
    symbols_choice = [random.choice(symbols) for sym in range(random.randint(5, 8))]
    numbers_choice = [random.choice(num_list) for num in range(5)]

    string_gen = alpha_lower_choice + alpha_upper_choice + symbols_choice + numbers_choice
    random.shuffle(string_gen)
    password = ''.join(string_gen)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Teka lang...', message='Dapat walang blangko')
        password_entry.delete(0, END)
        website_entry.delete(0, END)
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'You have entered the following details:\nE-mail:'
                                                      f'{email}\nPassword:{password}\nDo you wish to save?')
        password_entry.delete(0, END)
        website_entry.delete(0, END)

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
bintana = Tk()
bintana.title('Password Manager')
bintana.config(padx=50,pady=50)

kangbas = Canvas(width=200,height=200)
password_img = PhotoImage(file='logo.png')

kangbas.create_image(100,100,image=password_img)
kangbas.grid(row=0,column=1)

website_label = Label(text='Website')
website_label.grid(row=1,column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_label = Label(text='E-mail/Username')
email_label.grid(row=2,column=0)

email_entry = Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, 'carleyeshield@gmail.com')

password_label = Label(text='Password')
password_label.grid(row=3,column=0)

password_entry = Entry(width=24)
password_entry.grid(row=3,column=1,columnspan=1)

gen_password_btn = Button(text='Generate Password',width=13,command=generate_password)
gen_password_btn.grid(row=3,column=2)

add_password_btn = Button(text='Add',width=36,command=save)
add_password_btn.grid(row=4,column=1,columnspan=2)

bintana.mainloop()
