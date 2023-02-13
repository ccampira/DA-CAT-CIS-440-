from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.title('Da Cat')
win.geometry('400x650')
win.config(bg='beige')
canvas = Canvas(win, width=300, height=180, bg='beige')
canvas.grid(columnspan=3, pady=10)

logo = Image.open('thecat.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0, pady=20, padx=20)

name = StringVar()
password = StringVar()
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()
dep = StringVar()
checkvar22 = IntVar()
checkvar23 = IntVar()
checkvar24 = IntVar()
checkvar21 = IntVar()


def register_click():
    global orders
    orders = [checkvar1.get(), checkvar2.get(), checkvar3.get(), checkvar4.get()]
    orders = list(filter(None, orders))

    order_frame.grid_forget()


order_frame = Frame(win, width=360, height=400, bg='beige')

order_frame.grid(columnspan=3)

shop_lbl = Label(order_frame, text='Da Cat Hotel & Flight Bookings', width=30, bg='beige',
                 font=('Arial', 20), fg='black')
shop_lbl.grid(columnspan=3, row=1)

info_lbl = Label(order_frame, text='Login Form', width=30, bg='beige',
                 font=('Arial', 20), fg='black')
info_lbl.grid(columnspan=3, row=3, pady=5)

name_lbl = Label(order_frame, text='Enter your username: ', width=33, bg='light grey',
                 font=('Arial', 20), fg='black')
name_lbl.grid(columnspan=3, column=0, row=5, pady=10)

name_entry = Entry(order_frame, textvariable=name, justify=CENTER,
                   font=('chalkboard', 16), width=20)
name_entry.grid(columnspan=3, column=0, row=6)

password_lbl = Label(order_frame, text='Enter your password: ', width=33, bg='light grey',
                     font=('Arial', 20), fg='black')
password_lbl.grid(columnspan=3, column=0, row=7, pady=10)

password_entry = Entry(order_frame, textvariable=password, justify=CENTER,
                       font=('chalkboard', 16), width=20)
password_entry.grid(columnspan=3, column=0, row=8)
#
#
register_button = Button(order_frame, command=register_click,
                         font=("Arial", 16), text='Register', width=15)
register_button.grid(column=1, row=10, pady=20, padx=(30, 0), sticky=W)

win.mainloop()
