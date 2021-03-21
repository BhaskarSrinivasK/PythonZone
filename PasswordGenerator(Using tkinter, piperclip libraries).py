# importing Libraries

from tkinter import *
import random, string
import pyperclip

#initialsing a playground (Window)

window = Tk()
window.resizable(0, 0)
window.geometry("400x400")
window.title("SwagKBS - PASSWORD GENERATOR")

# heading
heading = Label(window, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(window, text='KBS', font='arial 15 bold').pack(side=BOTTOM)

###select password length
pass_label = Label(window, text='PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(window, from_=8, to_=32, textvariable=pass_len, width=15).pack()

#####define function

pass_str = StringVar()


def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


###button

Button(window, text="GENERATE PASSWORD", command=Generator).pack(pady=5)

Entry(window, textvariable=pass_str).pack()


########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())


Button(window, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

# loop to run program
window.mainloop()
