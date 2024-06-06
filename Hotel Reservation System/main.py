from tkinter import *
from tkinter.font import Font
import _sqlite3
import check_in_ui
import check_out
import get_info
import customer_info
import room_customization
import room_availability
import booking_history
import feedback
import os

class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # set background color
        self.root.configure(bg="#c9c1a7")

         # Initialize the database
        self.initialize_database()

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # display message
        self.label = Label(top, font=('Times', 50, 'bold'), text="K I N G S T O N  HOTEL", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.grid(row=0, column=3)

        # create check-in button
        self.check_in_button = Button(bottom, text="CHECK IN", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                      width=50, fg="#ffe9a1", anchor="center", command=check_in_ui.check_in_ui_fun)
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # create check-out button
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                       width=50, fg="#ffe9a1", anchor="center", command=check_out.check_out_ui)
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # create rooms information button
        self.room_info_button = Button(bottom, text="ROOMS INFORMATION", font=('Times', 20), bg="#948363", relief=RIDGE,
                                       height=2, width=50, fg="#ffe9a1", anchor="center", command=get_info.get_info_ui)
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)

        # create guest information button
        self.get_info_button = Button(bottom, text="GUEST INFORMATION", font=('Times', 20), bg="#948363", relief=RIDGE,
                                      height=2, width=50, fg="#ffe9a1", anchor="center", command=customer_info.customer_info_ui)
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)

        # create room customization button
        self.room_customization_button = Button(bottom, text="ROOM CUSTOMIZATION", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                                width=50, fg="#ffe9a1", anchor="center", command=room_customization.room_customization_ui)
        self.room_customization_button.grid(row=4, column=2, padx=10, pady=10)

        # create room availability button
        self.check_availability_button = Button(bottom, text="CHECK ROOM AVAILABILITY", font=('Times', 20), bg="#948363",
                                                relief=RIDGE, height=2, width=50, fg="#ffe9a1", anchor="center",
                                                command=room_availability.check_availability_ui)
        self.check_availability_button.grid(row=5, column=2, padx=10, pady=10)

        # create booking history button
        self.booking_history_button = Button(bottom, text="BOOKING HISTORY", font=('Times', 20), bg="#948363",
                                             relief=RIDGE, height=2, width=50, fg="#ffe9a1", anchor="center",
                                             command=booking_history.booking_history_ui)
        self.booking_history_button.grid(row=6, column=2, padx=10, pady=10)

        # create feedback button
        self.feedback_button = Button(bottom, text="LEAVE FEEDBACK", font=('Times', 20), bg="#948363", relief=RIDGE,
                                      height=2, width=50, fg="#ffe9a1", anchor="center", command=feedback.feedback_ui)
        self.feedback_button.grid(row=7, column=2, padx=10, pady=10)

        # button to exit the program
        self.exit_button = Button(bottom, text="EXIT", font=('Times', 20), bg="#948363", relief=RIDGE, height=2, width=50,
                                  fg="#ffe9a1", anchor="center", command=self.root.quit)
        self.exit_button.grid(row=8, column=2, padx=10, pady=10)

def initialize_database(self):
        conn = sqlite3.connect('Hotel.db')  #Connect to the SQLite database
        try:
            cursor = conn.cursor()
            #Create the Hotel table if it does not exist
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT, Address TEXT, MobileNumber TEXT, NumberOfDays INT, room_number NUMBER)'
            )
            #Create the Amount table if it does not exist
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Amount (ID INTEGER PRIMARY KEY AUTOINCREMENT, room_number NUMBER, amount_people NUMBER)'
            )
            conn.commit()  # Commit the changes
        finally:
            conn.close()  # Close the connection

def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()

if __name__ == '__main__':
    home_ui()
