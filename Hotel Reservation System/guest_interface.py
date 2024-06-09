from tkinter import *
from tkinter import ttk
import feedback
import booking_history
import room_availability

class GuestInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("K I N G S T O N  H O T E L - GUEST INTERFACE")
        self.root.geometry("800x600")
        self.root.configure(bg="#c9c1a7")

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True)

        # Title label
        self.label = Label(self.main_frame, text="Guest", font=('Times', 50, 'bold'), fg="#725700", bg="#c9c1a7")
        self.label.pack(pady=20)

        # Button styles
        self.button_style = ttk.Style()
        self.button_style.configure('Guest.TButton', font=('Times', 20), background="#948363", foreground="#ffe9a1")

        # Feedback Button
        self.feedback_button = ttk.Button(self.main_frame, text="FEEDBACK", style='Guest.TButton', command=self.show_feedback)
        self.feedback_button.pack(pady=10)

        # Booking History Button
        self.booking_history_button = ttk.Button(self.main_frame, text="BOOKING HISTORY", style='Guest.TButton', command=self.show_booking_history)
        self.booking_history_button.pack(pady=10)

        