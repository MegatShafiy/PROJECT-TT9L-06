from tkinter import *
import sqlite3
import main

class GetInfo:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("CUSTOMER INFORMATION")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        self.root.configure(bg="#c9c1a7")

        top = Frame(self.root, bg="#c9c1a7")
        top.pack(side="top")

        bottom = Frame(self.root, bg="#c9c1a7")
        bottom.pack(side="top")

        info_frame = Frame(self.root)
        info_frame.pack(side="top")

        button_frame = Frame(self.root, bg="#c9c1a7")
        button_frame.pack(side="top")

        # display message
        self.label = Label(top, font=('Times', 50, 'bold'), text="K I N G S T O N  H O T E L", fg="#725700",
                           anchor="center", bg="#c9c1a7")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # room no label
        self.room_no_label = Label(bottom, font=('Times', 20, 'bold'), text="ENTER ROOM NUMBER :", fg="#ffe9a1",
                                   anchor="center", bg="#948363")
        self.room_no_label.grid(row=2, column=2, padx=10, pady=10)

        self.room_number = IntVar()
        self.room_no_entry = Entry(bottom, width=5, text=self.room_number)
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=10)

        self.info_label = Label(bottom, font=('Times', 20, 'bold'), text="CUSTOMER INFORMATION HERE :", fg="#ffe9a1",
                                anchor="center", bg="#948363")
        self.info_label.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

        self.get_info_entry = Text(info_frame, height=15, width=90)
        self.get_info_entry.grid(row=1, column=1, padx=10, pady=10)

        def get_info():
            room_number1 = int(self.room_no_entry.get())
            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT,room_number NUMBER)')
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Amount (ID INTEGER PRIMARY KEY AUTOINCREMENT, room_number NUMBER, amount_people NUMBER)')
            conn.commit()
            with conn:
                cursor.execute("SELECT room_number FROM Hotel")
                ans = cursor.fetchall()
                room = []
                for i in ans:
                    room.append(i[0])
                if room_number1 in room:
                    with conn:
                        cursor.execute("SELECT * FROM Hotel")
                        ans = cursor.fetchall()
                        for i in ans:
                            if room_number1 == int(i[4]):
                                self.get_info_entry.insert(INSERT,
                                                           'NAME: ' + str(i[0]) + '\nADDRESS: ' + str(
                                                               i[1]) + '\nMOBILE NUMBER:  ' + str(
                                                               i[2]) + '\nNUMBER OF DAYS: ' + str(
                                                               i[3]) + '\nROOM NUMBER: ' + str(i[4]) + '\n')
                else:
                    self.get_info_entry.insert(INSERT, "\nPLEASE ENTER VALID ROOM NUMBER")

        # create submit button
        self.submit_button = Button(button_frame, text="SUBMIT", font=('Times', 15), bg="#948363", relief=RIDGE, height=2,
                                    width=15, fg="#ffe9a1", anchor="center", command=get_info)
        self.submit_button.grid(row=8, column=2, padx=10, pady=10)

        # create back button
        self.back_button = Button(button_frame, text="BACK", font=('Times', 15), bg="#948363", relief=RIDGE, height=2,
                                  width=15, fg="#ffe9a1", anchor="center", command=self.go_back)
        self.back_button.grid(row=8, column=3, padx=10, pady=10)

    def go_back(self):
        self.root.destroy()
        main.home_ui()

def get_info_ui():
    root = Tk()
    application = GetInfo(root)
    root.mainloop()





