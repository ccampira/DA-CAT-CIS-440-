from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.title('Da Cat')
win.geometry('400x650')
win.config(bg='beige')

## ADDED MENUBAR TO PROGRAM -> CARLOS
menubar = Menu(win)  # add a menu to window object/instance

filemenu = Menu(menubar)  # add File menu and commands
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Close')
filemenu.add_command(label='Exit', command=win.quit)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=False)  # if tearoff = false then it will be glued to the menu bar.
# If tearoff = true then it will allow you to move it.
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

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

win.config(menu=menubar)
win.mainloop()
