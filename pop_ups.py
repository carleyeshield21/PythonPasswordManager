from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # retrieving data using the get method
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Creating a message box after executing this function
    # messagebox.showinfo(title='Mensahe', message='Mesayds sent')

    # Creating conditions to check that the entries are not empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Teka lang...', message='Dapat walang blangko')
    else:
        # Creating a boolean value from the message box yes or no
        is_ok = messagebox.askokcancel(title=website, message=f'You have entered the follolwing details:\nE-mail:'
                                                      f'{email}\nPassword:{password}\nSave?')

        # nesting the open and append file in an if statement
        if is_ok:
            with open('data.txt', 'a') as data_file:
                # after retrieving the data, we append it to the data_file file
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

gen_password_btn = Button(text='Generate Password',width=13)
gen_password_btn.grid(row=3,column=2)

add_password_btn = Button(text='Add',width=36,command=save)
add_password_btn.grid(row=4,column=1,columnspan=2)



bintana.mainloop()