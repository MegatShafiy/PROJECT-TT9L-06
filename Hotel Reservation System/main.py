from tkinter import *
import pygame
from tkinter.font import Font
import check_in_ui
import check_out
import get_info
import customer_info
import room_type
import os
import booking_history
import feedback


class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # set background color
        self.root.configure(bg="#c9c1a7")

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        self.label = Label(top, font=('Times', 50, 'bold'), text="K I N G S T O N  HOTEL", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.grid(row=0, column=3)

        # create check in button
        self.check_in_button = Button(bottom, text="CHECK IN", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                      width=50,
                                      fg="#ffe9a1", anchor="center",
                                      command=check_in_ui.check_in_ui_fun)  # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # create check out button
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                       width=50, fg="#ffe9a1", anchor="center",
                                       command=check_out.check_out_ui)  # call check_out_ui function from check_out.py file
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # create feedback button
        self.feedback_button = Button(bottom, text="FEEDBACK", font=('Times', 20), bg="#948363", relief=RIDGE,
                                        height=2, width=50, fg="#ffe9a1", anchor="center", command=self.feedback)
        self.feedback_button.grid(row=3, column=2, padx=10, pady=10)

        # create booking history button
        self.booking_history_button = Button(bottom, text="BOOKING HISTORY", font=('Times', 20), bg="#948363", relief=RIDGE,
                                        height=2, width=50, fg="#ffe9a1", anchor="center", command=self.booking_history)
        self.booking_history_button.grid(row=4, column=2, padx=10, pady=10)

        # button to exit 
        self.exit_button = Button(bottom, text="EXIT", font=('Times', 20), bg="#948363", relief=RIDGE, height=2, width=50,
                                  fg="#ffe9a1",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=3, column=2, padx=10, pady=10)

        # Hide Customer Information and List of Customer buttons
        self.room_info_button = Button(bottom, text="CUSTOMER INFORMATION 🔒", font=('Times', 20), bg="#948363", relief=RIDGE,
                                       height=2,
                                       width=50, fg="#ffe9a1", anchor="center",
                                       command=get_info.get_info_ui, state=DISABLED)  # Disabled state
        self.room_info_button.grid(row=4, column=2, padx=10, pady=10)

        self.get_info_button = Button(bottom, text="LIST OF CUSTOMER 🔒", font=('Times', 20), bg="#948363",
                                      relief=RIDGE,
                                      height=2, width=50, fg="#ffe9a1", anchor="center",
                                      command=customer_info.customer_info_ui, state=DISABLED)  # Disabled state
        self.get_info_button.grid(row=5, column=2, padx=10, pady=10)

    def check_in(self):
        check_in_ui.check_in_ui_fun()

    def check_out(self):
        check_out.check_out_ui()

    def feedback(self):
        feedback.feedback_ui()

    def booking_history(self):
        booking_history.booking_history_ui()

    def show_customer_info(self):
        get_info.get_info_ui()

    def show_customer_list(self):
        customer_info.customer_info_ui()

    def exit(self):
        self.root.destroy()

    def play_music(self):
        pygame.mixer.music.load("hotel_music.mp3")  
        pygame.mixer.music.play(loops=-1)  


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()


