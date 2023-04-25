from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # retrieving data using the get method
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # first way to create a file to append to
    # data_file = open('data.txt', 'a')

    # second way is better because it allows us to close the file automatically without using the [filename].close,
    # we use the 'a' append mode to open the file to append data
    with open('data.txt', 'a') as data_file:
        # after retrieving the data, we append it to the data_file file
        data_file.write(f'{website} | {email} | {password}\n')

        # deleting the entries after appending to the file, the first argument is the first index of the string,
        # the second entry is up to what index will be deleted, if we use the argument END, it will delete the whole
        # string
        website_entry.delete(0,END)
        password_entry.delete(0,END)


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
# Using the focus method to place the cursor automatically in the first position of the entry
website_entry.focus()

email_label = Label(text='E-mail/Username')
email_label.grid(row=2,column=0)

email_entry = Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
# Using the insert method to put a specific text automatically in the entry field
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