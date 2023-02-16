from tkinter import *
from PIL import Image, ImageTk
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
            box1.place_forget()
            page_two.grid()
            logo_label.place(relx=1, rely=1)
            welcome_label.grid(row=0, column=0)
            info_label.grid(row=1, column=0)
    else:
        results_lbl.config(text='Username/Password is incorrect')


def close():
    window.destroy()




file_handle = open('users.json')
user_accounts = json.load(file_handle)
file_handle.close()

window = Tk()
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

window.columnconfigure(0, weight=1)

# background Image
bg_img = Image.open('wallpaper.jpg')
new_width = 1920
new_height = 1080
wallpaper = bg_img.resize((new_width, new_height), Image.ANTIALIAS)
wallpaper.save('wallpaper.jpg')
bg = ImageTk.PhotoImage(wallpaper)
bg_label = Label(window, image=bg)
bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
bg_label.grid_propagate(False)

# PAGE 2
page_two = Frame(window, bg='black', width=1920, height=1080, borderwidth=1)

# PAGE 3
page_three = Frame(window, bg='light blue', width=1920, height=1080, borderwidth=2)

# ADD CUSTOMER FRAME
add_frame = Frame(window, width=1920, height=1080, borderwidth=2)



#REFRESH PAGE
refresh_page = Frame(window, bg='light blue', width=1920, height=1080, borderwidth=2)



# page_two - Customer LIST
bg2_img = Image.open('wallpaper2.jpg')
new_width2 = 1920
new_height2 = 1080
wallpaper2 = bg2_img.resize((new_width2, new_height2), Image.ANTIALIAS)
wallpaper2.save('wallpaper2.jpg')
bg2 = ImageTk.PhotoImage(wallpaper2)
bg_label2 = Label(page_two, image=bg2)
bg_label2.grid(row=0, column=0)
bg_label2.grid_propagate(False)



# Welcome Label
welcome_label = Label(bg_label2, text=f'WELCOME TO DACAT HOTEL & FLIGHT BOOKING SERVICES.', font=('Impact', 40),
                      bg='white')

info_label = Label(bg_label2, text=f'Pick your next destination down below', font=('Verdana', 20), bg='white')




# ADD CUSTOMER PAGE----------------------------------------------------------------------------------------
bg3_img = Image.open('wallpaper3.jpg')
new_width3 = 1920
new_height3 = 1080
wallpaper3 = bg2_img.resize((new_width3, new_height3), Image.ANTIALIAS)
wallpaper3.save('wallpaper3.jpg')
bg3 = ImageTk.PhotoImage(wallpaper3)
bg_label3 = Label(add_frame, image=bg3)
bg_label3.grid(column=0, row=0)
bg_label3.grid_propagate(False)

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

# LOGO IMAGE
logo = Image.open('thecat.png')
new_width = 300
new_height = 225
img = logo.resize((new_width, new_height), Image.ANTIALIAS)
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

window.config(menu=menubar)
window.mainloop()  # this displays the GUI


#NOTE:
# I had big expectations for my project, I wanted it to add, and remove, and edit all the customers in the CSV file
# UNfortunately I could not figure out how to remove rows from a csv file or even edit each row of the CSV file
# THE COMMENTED OUT CODE is code that I was planning on using for this problem but I did not have the time to implement
# I plan on finishing my code during the summer to make this program fully funcitonal for EXNAR DIGITAL LLC


# customer_list = []
# Project Functions

# def remove_customer():
#     lines = list()
#     memberName = 'carlos'
#     with open('exnar_customer.csv', 'r') as readFile:
#         customers = csv.reader(readFile)
#         for row in customers:
#             lines.append(row)
#             for field in row:
#                 if field == memberName:
#                     lines.remove(row)
#
#     with open('exnar_customer.csv', 'w') as writeFile:
#         writer = csv.writer(writeFile)
#         writer.writerows(lines)
#
#     with open('exnar_customer.csv') as fp:
#         data = csv.reader(fp)
#         for row in data:
#             customer_labels = Label(refresh_frame, text=f'{row[0]:<50}{row[1]:<45}{row[2]:<50}{row[3]:>25}',
#                                     font=('Verdana', 11), bg="white", justify=LEFT, relief=RAISED)
#             customer_labels.grid()
#
#
# def refresh():
#     page_two.grid_forget()
#     refresh_page.grid()
#     remove_customer()

# #REMOVE BUTTON
# remove_customer_button = Button(actions_frame, text='Remove Customer', font=("Arial", 11), width=15)
# remove_customer_button.grid(row=1, column=0)
# #EDIT BUTTON
# edit_customer_button = Button(actions_frame, text='Edit Customer', font=("Arial", 11), width=15)
# edit_customer_button.grid(row=2, column=0)