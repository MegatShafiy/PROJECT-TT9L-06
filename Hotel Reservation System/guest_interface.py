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

        # Room Availability Button
        self.room_availability_button = ttk.Button(self.main_frame, text="ROOM AVAILABILITY", style='Guest.TButton', command=self.show_room_availability)
        self.room_availability_button.pack(pady=10)

        # Separator
        self.separator = ttk.Separator(self.main_frame, orient=HORIZONTAL)
        self.separator.pack(fill=X, pady=20)

        # Exit Button
        self.exit_button = ttk.Button(self.main_frame, text="EXIT", style='Guest.TButton', command=self.exit_app)
        self.exit_button.pack(pady=10)

    def show_feedback(self):
        feedback.feedback_ui()  # Call feedback_ui function from feedback.py file

    def show_booking_history(self):
        booking_history.booking_history_ui()  # Call booking_history_ui function from booking_history.py file

    def show_room_availability(self):
        room_availability.room_availability_ui()  # Call room_availability_ui function from room_availability.py file

    def exit_app(self):
        self.root.destroy()

# Create the main application window
root = Tk()
app = GuestInterface(root)
root.mainloop()
