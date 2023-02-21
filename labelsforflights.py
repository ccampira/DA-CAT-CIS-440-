from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from classes import BookHotel
from os import path
import time
import json




def button_click():
    username = user_name.get()
    password = pass_word.get()
    if username in user_accounts:
        if password != user_accounts[username]['Password']:
            results_lbl.config(text=username + ', the password is incorrect')
        else:
            results_lbl.config(text=username + ', the password is correct')
            bg_label.grid_forget()
            box1.grid_forget()
            page_two.grid()
            page_two.columnconfigure(0, weight=1)



    else:
        results_lbl.config(text='Username/Password is incorrect')


def contact():
    bg_label.grid_forget()
    box1.grid_forget()
    page_two.grid_forget()
    page_three.grid_forget()
    contact_page.grid()
    contact_page.grid()
    contact_page.columnconfigure(0, weight=2)
    bg_label3.grid(rowspan=4, columnspan=1)
    box2.grid(row=0, column=0)



def back():
    contact_page.grid_forget()
    bg_label3.grid_forget()
    box2.grid_forget()
    bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    box1.grid(row=0, column=0)

def close():
    window.destroy()

def next_button_click():
    page_two.grid_forget()
 #   box3.grid_forget()
    page_three.grid()
    page_three.columnconfigure(0, weight=3)


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









file_handle = open('users.json')
user_accounts = json.load(file_handle)
file_handle.close()

window = Tk()
window.state('zoomed')
window.geometry('1920x1080')  # left number is width, right number is height
window.title('DA CAT')
window.config(bg='#30D6FF')  # we are using rgb color
window.resizable(1, 0)

menubar = Menu(window)  # add a menu to window object/instance

filemenu = Menu(menubar)  # add File menu and commands
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Close')
filemenu.add_command(label='Exit', command=window.quit)

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

window.attributes('-fullscreen', True)
window.overrideredirect(True)

window.columnconfigure(0, weight=1)

# background Image
bg_img = Image.open('wallpaper.jpg')
new_width = 1920
new_height = 1080
wallpaper = bg_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
wallpaper.save('wallpaper.jpg')
bg = ImageTk.PhotoImage(wallpaper)
bg_label = Label(window, image=bg)
bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)




# PAGE 3
page_three = Frame(window, bg='light blue', width=1920, height=1080, borderwidth=2)

# ADD CUSTOMER FRAME
contact_page = Frame(window, width=1920, height=1080)

# #window.columnconfigure(0, weight=1) contact frame
# add_contact = Frame(window, bg='tan', width=1920, height=1080, borderwidth=2)


#REFRESH PAGE
refresh_page = Frame(window, bg='light blue', width=1920, height=1080, borderwidth=2)


# ADD CUSTOMER PAGE----------------------------------------------------------------------------------------
bg3_img = Image.open('wallpaper3.jpg')
new_width3 = 1920
new_height3 = 1080
wallpaper3 = bg3_img.resize((new_width3, new_height3), Image.Resampling.LANCZOS)
wallpaper3.save('wallpaper3.jpg')
bg3 = ImageTk.PhotoImage(wallpaper3)
bg_label3 = Label(contact_page, image=bg3)



# refresh_frame = Frame(bg_label3, bg='white', width=1920, height=1080, borderwidth=1)
# refresh_frame.grid(row=3, column=0)

# Configure variables
user_name = StringVar()
user_name.set("Type 'dacat' for username")
pass_word = StringVar()
pass_word.set("type 'hotel' for password")


# logo_label.place(r0elx=.396, rely=.1)

# FRAME WITH USERNAME & PASSWORD
box1 = Frame(window, bg='white', width=310, height=200, borderwidth=2, relief=RAISED)
box1.grid(row=0, columnspan=3)

box2 = Frame(contact_page, bg='white', width=310, height=200, borderwidth=2, relief=RAISED)




# LOGO IMAGE
logo = Image.open('thecat.png')
new_width = 300
new_height = 225
img = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
img.save('thecat.png')
logo = ImageTk.PhotoImage(img)
logo_label = Label(box1, image=logo)
logo_label.grid(row=0, column=2, columnspan=3)

# LOG IN TO YOUR ACCOUNT MESSAGE
Login_label = Label(box1, text='Login to your Account', width=20, font=('Impact', 20), fg='black', bg= 'white')
Login_label.grid(columnspan=2, row=1, column=2)

# label for username and password
username_label = Label(box1, text='Username', fg='black', font=('Impact', 20), bg='white')
username_label.grid(columnspan=1, row=2, column=2, padx=50, pady=20)
user_password = Label(box1, font=('Impact', 20), text='Password', bg='white')
user_password.grid(columnspan=1, row=4, column=2, padx=50, pady=20)

# BOX 1, USER & PASSWORD ENTRY BOXES
username_entry = Entry(box1, textvariable=user_name, justify=LEFT, width=30, font=('Verdana', 11))
username_entry.grid(columnspan=1, row=2, column=3, padx=20, pady=20)
password_entry = Entry(box1, textvariable=pass_word, justify=LEFT, width=30, font=('Verdana', 11))
password_entry.grid(columnspan=1, row=4, column=3, padx=20, pady=20)

results_lbl = Label(box1, justify=CENTER, font=('Verdana', 11), bg='white')
results_lbl.grid(columnspan=2, row=5, column=2)


# Submit button
submit_button = Button(box1, command=button_click, font=('Impact', 20), text='Log In',
                       relief=GROOVE, bg='black', fg='white')
submit_button.grid(row=6, column=2, columnspan=3)

#contact button
contact_button = Button(box1, command=contact, font=('Impact', 20), text='Contact',
                       relief=GROOVE, bg='black', fg='white')
# contact_button.place(relx=.32, rely=.63)
contact_button.grid(row=6, column=3, columnspan=3)

#back button
back_button = Button(box2, command=back, font=('Impact', 20), text='Home',
                       relief=GROOVE, bg='black', fg='white')
# back_button.place(relx=.375, rely=.6)
back_button.grid(row=6, column=3, columnspan=3)

co_lbl = Label(box2, text='Welcome to DaCat Support', width=60, bg='gray',
                 font=('Arial', 20), fg='white')
co_lbl.grid(row=5, column=3, columnspan=3)
# co_lbl.place(relx=.15, rely=.4)

service_lbl = Label(box2, text=f'Email: DaCatSupport@Gmail.com', width=60, bg='gray',
                    font=('Arial', 20), fg='white')
service_lbl.grid(row=4,column=3,columnspan=3)
# service_lbl.place(relx=.15, rely=.45)

info_lbl = Label(box2, text='Phone: 1-800-888-8888', width=60, bg='gray',
                 font=('Arial', 20), fg='white')
info_lbl.grid(row=3, column=3, columnspan=3)
# info_lbl.place(relx=.15, rely=.5)

############################################################################################################ PAGE 2
page_two = Frame(window, bg='black', width=1920, height=1080, borderwidth=1)

# Background IMAGE
bg2_img = Image.open('wallpaper2.jpg')
new_width2 = 1920
new_height2 = 1080
wallpaper2 = bg2_img.resize((new_width2, new_height2), Image.Resampling.LANCZOS)
wallpaper2.save('wallpaper2.jpg')
bg2 = ImageTk.PhotoImage(wallpaper2)
bg_label2 = Label(page_two, image=bg2)
bg_label2.grid(rowspan=4, columnspan=1)
bg_label2.grid_propagate(False)

box3 = Frame(page_two, bg='white', width=450, height=300, borderwidth=2, relief=RAISED)
box3.grid(row=0, column=0)

houston = Image.open('Houston.jpeg')
new_width4 = 300
new_height4 = 250
houston2 = houston.resize((new_width4, new_height4), Image.Resampling.LANCZOS)
houston2.save('Houston.jpeg')
texas = ImageTk.PhotoImage(houston)

chicago = Image.open('chicago.jpeg')
chicago_width = 300
chicago_height = 250
chicago2 = chicago.resize((chicago_width, chicago_height), Image.Resampling.LANCZOS)
chicago2.save('chicago.jpeg')
illinois = ImageTk.PhotoImage(chicago2)

LA = Image.open('LA.jpeg')
LA_width = 300
LA_height = 250
LA2 = LA.resize((LA_width, LA_height), Image.Resampling.LANCZOS)
LA2.save('LA.jpeg')
california = ImageTk.PhotoImage(LA2)

miami = Image.open('Miami.jpeg')
miami_width = 300
miami_height = 250
miami2 = miami.resize((miami_width, miami_height), Image.Resampling.LANCZOS)
miami2.save('Miami.jpeg')
florida = ImageTk.PhotoImage(miami2)

vegas = Image.open('vegas.jpeg')
vegas_width = 300
vegas_height = 250
vegas2 = vegas.resize((vegas_width, vegas_height), Image.Resampling.LANCZOS)
vegas2.save('vegas.jpeg')
nevada = ImageTk.PhotoImage(vegas2)

phx = Image.open('PHX.PNG')
phx_width = 300
phx_height = 250
phx2 = phx.resize((phx_width, phx_height), Image.Resampling.LANCZOS)
phx2.save('PHX.png')
arizona = ImageTk.PhotoImage(phx2)

ny = Image.open('NY.jpeg')
ny_width = 300
ny_height = 250
ny2 = ny.resize((ny_width, ny_height), Image.Resampling.LANCZOS)
ny2.save('NY.jpeg')
newyork = ImageTk.PhotoImage(ny2)

portland = Image.open('portland.jpeg')
portland_width = 300
portland_height = 250
portland2 = portland.resize((portland_width, portland_height), Image.Resampling.LANCZOS)
portland2.save('portland.jpeg')
oregon = ImageTk.PhotoImage(portland2)

seattle = Image.open('Seattle.jpeg')
seattle_width = 300
seattle_height = 250
seattle2 = seattle.resize((seattle_width, seattle_height), Image.Resampling.LANCZOS)
seattle2.save('Seattle.jpeg')
washington = ImageTk.PhotoImage(seattle2)

Philly = Image.open('Philly.jpeg')
Philly_width = 300
Philly_height = 250
Philly2 = Philly.resize((Philly_width, Philly_height), Image.Resampling.LANCZOS)
Philly2.save('Philly.jpeg')
pennsylvania = ImageTk.PhotoImage(Philly2)

var = IntVar()
r1= Radiobutton(box3, text='Houston', variable=var, value=1, image=texas, font=('Impact', 40))
r1.grid(row=3, column=0, sticky=W)
houston_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='HOUSTON')
houston_lbl.grid(row=4, column=0, sticky=W, padx=90)
r2= Radiobutton(box3, text='Chicago', variable=var, value=2, image=illinois, font=('Impact', 40))
r2.grid(row=3, column=0, sticky=W, padx=300)
chicago_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='CHICAGO')
chicago_lbl.grid(row=4, column=0, sticky=W, padx=390)
r3= Radiobutton(box3, text='Los Angeles', variable=var, value=3, image=california, font=('Impact', 40))
r3.grid(row=3, column=0, sticky=W, padx=600)
losAngeles_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='LOS ANGELES')
losAngeles_lbl.grid(row=4, column=0, sticky=W, padx=670)
r4= Radiobutton(box3, text='Miami', variable=var, value=4, image=florida, font=('Impact', 40))
r4.grid(row=3, column=0, sticky=W, padx=900)
miami_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='MIAMI')
miami_lbl.grid(row=4, column=0, sticky=W, padx=1010)
r5= Radiobutton(box3, text='Las Vegas', variable=var, value=5, image=nevada, font=('Impact', 40))
r5.grid(row=3, column=0, sticky=W, padx=1200)
lasVegas_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='LAS VEGAS')
lasVegas_lbl.grid(row=4, column=0, sticky=W, padx=1290)
r6= Radiobutton(box3, text='PHX', variable=var, value=6, image=arizona, font=('Impact', 40))
r6.grid(row=6, column=0, sticky=W)
phoenix_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='PHOENIX')
phoenix_lbl.grid(row=7, column=0, sticky=W, padx=90)
r7= Radiobutton(box3, text='NY', variable=var, value=7, image=newyork, font=('Impact', 40))
r7.grid(row=6, column=0, sticky=W, padx=300)
ny_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='New York')
ny_lbl.grid(row=7, column=0, sticky=W, padx=400)
r8= Radiobutton(box3, text='portland', variable=var, value=8, image=oregon, font=('Impact', 40))
r8.grid(row=6, column=0, sticky=W, padx=600)
portland_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='Portland')
portland_lbl.grid(row=7, column=0, sticky=W, padx=700)
r9= Radiobutton(box3, text='Seattle', variable=var, value=9, image=washington, font=('Impact', 40))
r9.grid(row=6, column=0, sticky=W, padx=900)
seattle_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='Seattle')
seattle_lbl.grid(row=7, column=0, sticky=W, padx=1000)
r10= Radiobutton(box3, text='Philly', variable=var, value=10, image=pennsylvania, font=('Impact', 40))
r10.grid(row=6, column=0, sticky=W, padx=1200)
philly_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='Philadelphia')
philly_lbl.grid(row=7, column=0, sticky=W, padx=1300)

# Welcome Label
welcome_label = Label(box3, text=f'WELCOME TO DACAT HOTEL & FLIGHT BOOKING SERVICES.', font=('Impact', 40),
                      bg='white')
welcome_label.grid(row=0, column=0,sticky=W)
info_label = Label(box3, text=f'Pick your next destination down below', font=('Verdana', 20), bg='white')
info_label.grid(row=2, column=0, sticky=W)
############################################################################################################ PAGE 3
page_three = Frame(window, bg='black', width=1920, height=1080, borderwidth=1)
# Next button
next_button = Button(box3, command=next_button_click, font=('Impact', 20), text='Next',
                       relief=GROOVE, bg='black', fg='white')
next_button.grid(row=9, column=0, columnspan=3)

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
v = StringVar(window, "1")


canvas = Canvas(page_three, width=90, height=90, bg='green')
canvas.grid(columnspan=2, pady=0)






# labels
#title_label = Label(box3, text="DACAT Hotel Bookings", justify=CENTER, font=('Arial', 18),
#                   bg='black', fg='white', width=300)
#title_label.grid(row=1, column=0, pady=3, ipady=0)

# frame
box0 = Frame(page_three, bg='green', width=600, height=50,
             borderwidth=5)
box0.grid(row=4, column=0, columnspan=3, pady=3)
box0.grid_propagate(False)
box0.columnconfigure(0, weight=1)
box0.columnconfigure(1, weight=1)
box0.columnconfigure(2, weight=1)


box5 = Frame(page_three, bg='green', width=600, height=80,
             borderwidth=5)
box5.grid(row=5, column=0, columnspan=3, pady=5)
box5.grid(row=5, column=0, columnspan=3, pady=5)
box5.grid_propagate(False)
box5.columnconfigure(0, weight=1)
box5.columnconfigure(1, weight=1)
box5.columnconfigure(2, weight=1)

box6 = Frame(page_three, bg='green', width=600, height=100,
             borderwidth=5)
box6.grid(row=6, column=0, columnspan=3, pady=5)
box6.grid_propagate(False)
box6.columnconfigure(0, weight=1)
box6.columnconfigure(1, weight=1)
box6.columnconfigure(2, weight=1)


box4 = Frame(page_three, bg='green', width=600, height=100,
             borderwidth=5)
box4.grid(row=7, column=0, columnspan=3, pady=5)
box4.grid_propagate(False)
box4.columnconfigure(0, weight=1)
box4.columnconfigure(1, weight=1)
scrollbar = ttk.Scrollbar(box4, orient="vertical")

# listbox
custom_box = Listbox(page_three, width=100, height=5, borderwidth=3)
custom_box.grid(row=10, column=0, columnspan=3, pady=5)
custom_box.bind('<Double-Button-1>', doubleclick_to_delete)


hotel_label = Label(box5, text='Hotel', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
hotel_label.grid(row=1, column=0, pady=5, padx=10, sticky=W)
hotel_box = ttk.Combobox(box5, values=hotel)
hotel_box.grid(row=2, column=0, pady=2, padx=10, sticky=EW)
hotel_box.set('Select a Hotel')

rooms_label = Label(box5, text='Room', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
rooms_label.grid(row=1, column=1, pady=5, sticky=W)
rooms_box = ttk.Combobox(box5, values=rooms)
rooms_box.grid(row=2, column=1, pady=2, sticky=EW)
rooms_box.set('Select Number of Rooms')

guests_label = Label(box5, text='Guests', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
guests_label.grid(row=1, column=2, pady=5, padx=10, sticky=W)
guests_box = ttk.Combobox(box5, values=guests)
guests_box.grid(row=2, column=2, pady=5, padx=10, sticky=EW)
guests_box.set('Select Number of Guests')

addon_label = Label(box6, text='Room Type', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
addon_label.grid(row=1, columnspan=3, pady=5, sticky=EW)

single = Radiobutton(box6, text="Single Room",
                     variable=v, value='Single Room(s)',    highlightthickness=0, background="green")
single.grid(row=2, column=1, padx=10, sticky=EW)

double = Radiobutton(box6, text="Double Room",
                     variable=v, value='Double Room(s)',    highlightthickness=0, background="green")
double.grid(row=3, column=1, padx=10, sticky=EW)

name_label = Label(box0, text='Enter Name: ', justify=CENTER, font=('Arial', 12), bg='green', fg='black')
name_label.grid(row=1, column=0, pady=5, padx=50, sticky=W, columnspan=2)
name_textbox = Entry(box0, justify=LEFT, font=('Arial', 12))
name_textbox.grid(row=1, column=0, pady=1, padx=10, sticky=E, columnspan=2)
confirmation_label = Label(box4, textvariable=confirmation, width=60, bg='green', font=('Arial', 8), fg='white')
confirmation_label.grid(row=1, column=1, pady=0, sticky=W)
order_label = Label(box4, text='Booking Details will be displayed here', width=60, bg='green', font=('Arial', 8), fg='white')
order_label.grid(row=2, column=0, pady=0, padx=12, sticky=EW, columnspan=2)

menu_label = Label(page_three, text='Hotel Confirmation (Double-Click to Cancel)', justify=CENTER, font=('Arial', 12),
                   bg='black', fg='white')
menu_label.grid(row=9, column=0, pady=3, padx=0, sticky=EW, columnspan=3)

# buttons
reset_button = Button(box0, font=("Arial", 10), text='Reset', width=10, command=reset)
# reset_button.grid(column=0, row=8, pady=2, padx=300, columnspan=2, sticky=W)
reset_button.grid(column=3, row=1, pady=2, padx=5, sticky=W)
custom_button = Button(box4, font=("Arial", 10), text='Book Hotel', width=20, command=add_custom_drink)
custom_button.grid(column=0, row=0, pady=2, padx=0, columnspan=2)
exit_button2 = Button(box0, command=close,
                     font=("Arial", 8), text='LOGOUT', width=5)
exit_button2.grid(column=0, row=0, padx=50, pady=0, sticky=E, ipady=5, ipadx=20)

#contact button
contact_button2 = Button(box0, command=contact, font=('Arial', 8), text='Contact')
contact_button2.grid(column=0, row=0, padx=50, pady=0, sticky=W, ipady=5, ipadx=20)


window.config(menu=menubar)
window.mainloop()