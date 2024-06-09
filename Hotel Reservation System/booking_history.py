from tkinter import *
from tkinter import ttk

class BookingHistoryPage:
    def __init__(self, root):
        self.root = root
        self.root.title("K I N G S T O N  H O T E L - BOOKING HISTORY")
        self.root.geometry("800x600")
        self.root.configure(bg="#c9c1a7")

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title label
        self.label = Label(self.main_frame, text="Booking History", font=('Times', 30, 'bold'), fg="#725700", bg="#c9c1a7")
        self.label.pack(pady=20)

        # Treeview for displaying booking history
        self.tree = ttk.Treeview(self.main_frame, columns=("Booking ID", "Customer Name", "Room Number", "Check-in Date", "Check-out Date"), show="headings")
        self.tree.heading("Booking ID", text="Booking ID")
        self.tree.heading("Customer Name", text="Customer Name")
        self.tree.heading("Room Number", text="Room Number")
        self.tree.heading("Check-in Date", text="Check-in Date")
        self.tree.heading("Check-out Date", text="Check-out Date")
        self.tree.pack(fill=BOTH, expand=True)

        # Back Button
        self.back_button = ttk.Button(self.main_frame, text="BACK", command=self.back_to_main)
        self.back_button.pack(pady=10)

        # Load booking history
        self.load_booking_history()

    

        
        
        
        
