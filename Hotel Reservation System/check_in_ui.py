import sqlite3
from tkinter import *
from tkinter import messagebox
import random

import main

room_number_taken = []


class CheckIN:

    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("CHECK IN")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        #changed border color to brown
        self.root.configure(borderwidth=3, highlightbackground="#948363", highlightcolor="#948363")

        self.root['bg'] = 'brown'

        self.root.configure(bg="#c9c1a7")

        self.top = LabelFrame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root, bg="#c9c1a7")
        self.bottom.pack(side="top")

        self.checkbox = Frame(self.root)
        self.checkbox.pack(side="top")


        # fix the border
        self.label = Label(self.top, font=('Times', 50, 'bold'), text="CHECK IN", fg="#ffe9a1", anchor="center",
                   bg="#725700", borderwidth=3, relief="solid")
        self.label.grid(row=0, column=3, padx=10, pady=10)


        self.name_var = StringVar()

        self.name_entry = Entry(self.bottom, width=50, textvar=self.name_var)
        


        self.name_label = Label(self.bottom, font=('Times', 20, 'bold'), bg="#948363", text="ENTER YOUR NAME :", fg="#ffe9a1",
                                   anchor="w")
        self.name_label.grid(row=2, column=2, padx=10, pady=10)

        self.name_var = StringVar()
        self.name_entry = Entry(self.bottom, width=50, textvar=self.name_var)
        self.name_entry.grid(row=2, column=3, padx=10, pady=10)

        # address label
        self.address_label = Label(self.bottom, font=('Times', 20, 'bold'), bg="#948363", text="ENTER YOUR ADDRESS :", fg="#ffe9a1",
                                   anchor="w")
        self.address_label.grid(row=3, column=2, padx=10, pady=10)

        self.address_var = StringVar()
        self.address_entry = Entry(self.bottom, width=50, textvar=self.address_var)
        self.address_entry.grid(row=3, column=3, padx=10, pady=10)

        # mobile label

        self.mobile_label = Label(self.bottom, font=('Times', 20, 'bold'), bg="#948363", text="ENTER YOUR MOBILE NUMBER :",
                                  fg="#ffe9a1",
                                  anchor="w")
        self.mobile_label.grid(row=4, column=2, padx=10, pady=10)


        self.mobile_var = IntVar()
        self.mobile_entry = Entry(self.bottom, width=50, text=self.mobile_var)
        self.mobile_entry.grid(row=4, column=3, padx=10, pady=10)

        # number of days label
        self.days_label = Label(self.bottom, font=('Times', 20, 'bold'), bg="#948363", text="ENTER NUMBER OF DAYS TO STAY :",
                                fg="#ffe9a1",
                                anchor="w")
        self.days_label.grid(row=5, column=2, padx=10, pady=10)

        self.days_var = IntVar()
        self.days_entry = Entry(self.bottom, width=50, text=self.days_var)
        self.days_entry.grid(row=5, column=3, padx=10, pady=10)

        # room number label
        self.room_number_label = Label(self.bottom, font=('Times', 20, 'bold'), bg="#948363", text="ROOM NUMBER: ",
                                       fg="#ffe9a1",
                                       anchor="w")
        self.room_number_label.grid(row=6, column=2, padx=10, pady=10)

        roomnumber = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
        self.room_number_var = random.choice(roomnumber)

        self.room_entry = Entry(self.bottom, width=50)
        self.room_entry.insert(INSERT, self.room_number_var)
        self.room_entry.grid(row=6, column=3, padx=10, pady=10)

        def submit_info():
            global ans
            name = self.name_entry.get()
            address = self.address_entry.get()
            room = self.room_number_var

            while True:
                self.h = str(self.mobile_entry.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    mobile = self.h
                    ans = TRUE
                    break
                else:
                    ans = False
                    messagebox.showerror("ERROR", "PLEASE ENTER 10 DIGIT MOBILE NUMBER")
                    break

            while True:
                self.h = str(self.days_entry.get())
                if self.h.isdigit():
                    days = self.h
                    ans1 = True
                    break
                else:
                    ans1 = False
                    messagebox.showerror("ERROR", "NUMBER OF DAYS CANNOT BE VARIABLE")
                    break

            if ans == TRUE and ans1 == True:
                conn = sqlite3.connect('Hotel.db')
                with conn:
                    cursor = conn.cursor()
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT,Address TEXT,mobile_number NUMBER,number_days '
                    'NUMBER,room_number NUMBER)')
                cursor.execute('INSERT INTO Hotel (FullName,Address,mobile_number,number_days,room_number) '
                               'VALUES(?,?,?,?,?)', (name, address, mobile, days, room))
                conn.commit()
                with conn:
                    cursor.execute("SELECT * FROM Hotel")
                    print(cursor.fetchall())
            room_number()
            self.name_var.set('')
            self.address_var.set('')
            self.days_var.set('')
            self.mobile_var.set('')

        def room_number():
            room_number_taken.append(self.room_number_var)
            print(room_number_taken)

        def reset():
            self.room_number_var = random.choice(roomnumber)
            self.room_entry.delete(0, END)
            self.room_entry.insert(0, self.room_number_var)

            self.name_entry.delete(0, END)
            self.name_entry.insert(0, "")

            self.mobile_entry.delete(0, END)
            self.mobile_entry.insert(0, "")

            self.address_entry.delete(0, END)
            self.address_entry.insert(0, "")

            self.days_entry.delete(0, END)
            self.days_entry.insert(0, "")

        # create submit button
        self.submit_button = Button(self.checkbox, text="SUBMIT", font=('', 15), bg="#948363", relief=RIDGE, height=2,
                                    width=15,
                                    fg="#ffe9a1", anchor="center", command=submit_info)
        self.submit_button.grid(row=5, column=1, padx=10, pady=10)

        # back to home page
        self.back_home_button = Button(self.checkbox, text="HOME", font=('', 15), bg="#948363", relief=RIDGE, height=2,
                                       width=15,
                                       fg="#ffe9a1", anchor="center", command=main.home_ui)
        self.back_home_button.grid(row=5, column=2, padx=10, pady=10)

        Button(self.checkbox, text="RESET", font=('', 15), bg="#948363", relief=RIDGE, height=2, width=15, fg="#ffe9a1",
               anchor="center", command=reset).grid(row=5, column=3, padx=10, pady=10)


def check_in_ui_fun():
    root = Tk()
    application = CheckIN(root)
    root.mainloop()