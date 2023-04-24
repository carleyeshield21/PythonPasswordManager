from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
bintana = Tk()
bintana.title('Password Manager')
bintana.config(padx=20,pady=20)

kangbas = Canvas(width=200,height=200)
password_img = PhotoImage(file='logo.png')

kangbas.create_image(100,100,image=password_img)
kangbas.grid()

bintana.mainloop()