from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_label = Label(text='E-mail/Username')
email_label.grid(row=2,column=0)

email_entry = Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)

password_label = Label(text='Password')
password_label.grid(row=3,column=0)

password_entry = Entry(width=24)
password_entry.grid(row=3,column=1,columnspan=1)

gen_password_btn = Button(text='Generate Password',width=13)
gen_password_btn.grid(row=3,column=2)

add_password_btn = Button(text='Add',width=36)
add_password_btn.grid(row=4,column=1,columnspan=2)



bintana.mainloop()