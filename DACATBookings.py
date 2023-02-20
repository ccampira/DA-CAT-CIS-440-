# Devonne Le, CIS 440

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from classes import BookHotel
from os import path
import time

win = Tk()
win.title('DACAT Bookings')
win.geometry('1000x1000')
win.columnconfigure(0, weight=1)
win.config(bg='black')

# functions
def add_custom_drink():
    global name, custom_list, details
    if not path.isfile('DACAT-HotelRecords.txt'):
        file = open('DACAT-HotelRecords.txt', 'w')
        file.write("DACAT Booking records: \n")
        file.close()

    name = name_textbox.get()
    hotel_custom = hotel_box.get()
    rooms_custom = rooms_box.get()
    guests_custom = guests_box.get()
    roomtype_custom = v.get()

    # total_price = (len(addons) * .50) + 5
    total_price = 500
    # number_of_addons = len(addons)
    # custom1 = BookHotel(name, variety_custom, size_custom, flavor_custom, number_of_addons, total_price)
    Booking1 = BookHotel(name, hotel_custom, rooms_custom, guests_custom, roomtype_custom, total_price)

    file = open('DACAT-HotelRecords.txt', 'a')
    # file.writelines(f'{time.ctime()}, {name}, {variety_custom}, {size_custom}, {flavor_custom}, {addons}, ${total_price:.2f}\n')
    file.writelines(
        f'{time.ctime()}, {name}, {hotel_custom}, {rooms_custom}, {guests_custom}, {roomtype_custom} ${total_price:.2f}\n')
    confirmation.set(Booking1.custom_confirmation())
    custom_box.insert(END, Booking1)

    order_label.config(text=Booking1.order_details())

    custom_list.append(Booking1)

    clear_fields()


def doubleclick_to_delete(event):
    global details
    clear_fields()
    confirmation.set('The selected booking has been canceled')
    custom_box.delete(custom_box.curselection()[0])
    # order_index = custom_box.curselection()[0]
    # view_order = custom_list[order_index]
    # order_label.config(text=view_order)


def reset():
    clear_fields()
    confirmation.set('')
    order_label.config(text='Booking Details will be displayed here!')



def clear_fields():
    global name
    # c1.deselect()
    # c2.deselect()
    # c3.deselect()
    # c4.deselect()
    # c5.deselect()
    # c6.deselect()
    hotel_box.set('Select a Hotel')
    rooms_box.set('Select Number of Rooms')
    guests_box.set('Select Number of Guests')
    v.set(None)
    name_textbox.delete(0, END)

def close():
    win.quit()

# variables
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()
checkvar5 = IntVar()
checkvar6 = IntVar()
checkvar7 = IntVar()
checkvar8 = IntVar()
name = StringVar()
confirmation = StringVar()
custom_list = []
hotel = ['Marriott', 'Hyatt', 'Hilton', 'Four Seasons']
rooms = ['1', '2', '3']
guests = ['1', '2', '3', '4', '5']

# Dictionary to create multiple buttons
values = {"RadioButton 1": "1",
          "RadioButton 2": "2",
          "RadioButton 3": "3",
          "RadioButton 4": "4",
          "RadioButton 5": "5"}
# Tkinter string variable
# able to store any string value
v = StringVar(win, "1")


canvas = Canvas(win, width=90, height=90, bg='green')
canvas.grid(columnspan=2, pady=0)

logo = Image.open('thecat.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0, pady=10, ipady=0)

logo = Image.open('thecat.png')
new_width = 90
new_height = 90
img = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
img.save('thecat.png')
logo = ImageTk.PhotoImage(img)

# labels
title_label = Label(win, text="DACAT Hotel Bookings", justify=CENTER, font=('Arial', 18),
                    bg='black', fg='white', width=300)
title_label.grid(row=1, column=0, pady=3, ipady=0)

# frame
box0 = Frame(win, bg='green', width=600, height=50,
             borderwidth=5)
box0.grid(row=4, column=0, columnspan=3, pady=3)
box0.grid_propagate(False)
box0.columnconfigure(0, weight=1)
box0.columnconfigure(1, weight=1)
box0.columnconfigure(2, weight=1)


box1 = Frame(win, bg='green', width=600, height=80,
             borderwidth=5)
box1.grid(row=5, column=0, columnspan=3, pady=5)
box1.grid_propagate(False)
box1.columnconfigure(0, weight=1)
box1.columnconfigure(1, weight=1)
box1.columnconfigure(2, weight=1)

box2 = Frame(win, bg='green', width=600, height=100,
             borderwidth=5)
box2.grid(row=6, column=0, columnspan=3, pady=5)
box2.grid_propagate(False)
box2.columnconfigure(0, weight=1)
box2.columnconfigure(1, weight=1)
box2.columnconfigure(2, weight=1)


box3 = Frame(win, bg='green', width=600, height=100,
             borderwidth=5)
box3.grid(row=7, column=0, columnspan=3, pady=5)
box3.grid_propagate(False)
box3.columnconfigure(0, weight=1)
box3.columnconfigure(1, weight=1)
scrollbar = ttk.Scrollbar(box3, orient="vertical")

# listbox
custom_box = Listbox(win, width=100, height=5, borderwidth=3)
custom_box.grid(row=10, column=0, columnspan=3, pady=5)
custom_box.bind('<Double-Button-1>', doubleclick_to_delete)


hotel_label = Label(box1, text='Hotel', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
hotel_label.grid(row=1, column=0, pady=5, padx=10, sticky=W)
hotel_box = ttk.Combobox(box1, values=hotel)
hotel_box.grid(row=2, column=0, pady=2, padx=10, sticky=EW)
hotel_box.set('Select a Hotel')

rooms_label = Label(box1, text='Room', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
rooms_label.grid(row=1, column=1, pady=5, sticky=W)
rooms_box = ttk.Combobox(box1, values=rooms)
rooms_box.grid(row=2, column=1, pady=2, sticky=EW)
rooms_box.set('Select Number of Rooms')

guests_label = Label(box1, text='Guests', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
guests_label.grid(row=1, column=2, pady=5, padx=10, sticky=W)
guests_box = ttk.Combobox(box1, values=guests)
guests_box.grid(row=2, column=2, pady=5, padx=10, sticky=EW)
guests_box.set('Select Number of Guests')

addon_label = Label(box2, text='Room Type', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
addon_label.grid(row=1, columnspan=3, pady=5, sticky=EW)

single = Radiobutton(box2, text="Single Room",
                     variable=v, value='Single Room(s)',    highlightthickness=0, background="green")
single.grid(row=2, column=1, padx=10, sticky=EW)

double = Radiobutton(box2, text="Double Room",
                     variable=v, value='Double Room(s)',    highlightthickness=0, background="green")
double.grid(row=3, column=1, padx=10, sticky=EW)


# c1 = Checkbutton(box2, text="Spa Pass", variable=checkvar1,
#                  font=('Arial', 10), onvalue=1, offvalue=0,  bg='green')
# c1.grid(row=2, column=0, padx=10, sticky=EW)
# c2 = Checkbutton(box2, text="Oat-Milk", variable=checkvar2,
#                  font=('Arial', 10), onvalue=2, offvalue=0, bg='green')
# c2.grid(row=3, column=0, padx=10, sticky=EW)
# c3 = Checkbutton(box2, text="Syrup", variable=checkvar3,
#                  font=('Arial', 10), onvalue=3, offvalue=0, bg='green')
# c3.grid(row=2, column=1, padx=10, sticky=EW)
# c4 = Checkbutton(box2, text="Cream", variable=checkvar4,
#                  font=('Arial', 10), onvalue=4, offvalue=0, bg='green')
# c4.grid(row=3, column=1, padx=10, sticky=EW)
# c5 = Checkbutton(box2, text="Sugar", variable=checkvar5,
#                  font=('Arial', 10), onvalue=5, offvalue=0, bg='green')
# c5.grid(row=2, column=2, padx=10, sticky=EW)
# c6 = Checkbutton(box2, text="Cold-Foam", variable=checkvar6,
#                  font=('Arial', 10), onvalue=6, offvalue=0, bg='green')
# c6.grid(row=3, column=2, padx=10, sticky=EW)

name_label = Label(box0, text='Enter Name: ', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
name_label.grid(row=1, column=0, pady=5, padx=50, sticky=W, columnspan=2)
name_textbox = Entry(box0, justify=LEFT, font=('Arial', 12))
name_textbox.grid(row=1, column=0, pady=1, padx=10, sticky=E, columnspan=2)
confirmation_label = Label(box3, textvariable=confirmation, width=60, bg='green', font=('Arial', 8), fg='white')
confirmation_label.grid(row=1, column=1, pady=0, sticky=W)
order_label = Label(box3, text='Booking Details will be displayed here', width=60, bg='green', font=('Arial', 8), fg='white')
order_label.grid(row=2, column=0, pady=0, padx=12, sticky=EW, columnspan=2)

menu_label = Label(win, text='Hotel Confirmation (Double-Click to Cancel)', justify=CENTER, font=('Arial', 12),
                   bg='black', fg='white')
menu_label.grid(row=9, column=0, pady=3, padx=0, sticky=EW, columnspan=3)

# buttons
reset_button = Button(box0, font=("Arial", 10), text='Reset', width=10, command=reset)
# reset_button.grid(column=0, row=8, pady=2, padx=300, columnspan=2, sticky=W)
reset_button.grid(column=3, row=1, pady=2, padx=5, sticky=W)
custom_button = Button(box3, font=("Arial", 10), text='Book Hotel', width=20, command=add_custom_drink)
custom_button.grid(column=0, row=0, pady=2, padx=0, columnspan=2)
exit_button = Button(win, command=close,
                     font=("Arial", 8), text='LOGOUT', width=5)
exit_button.grid(column=0, row=0, padx=50, pady=0, sticky=E, ipady=5, ipadx=20)

#contact button
contact_button = Button(win, command=close, font=('Arial', 8), text='Contact')
contact_button.grid(column=0, row=0, padx=50, pady=0, sticky=W, ipady=5, ipadx=20)


win.mainloop()