from tkinter import *
from tkinter import messagebox

def room_customization_ui():
    # Create a new window for room customization
    customization_window = Toplevel()
    customization_window.title("Room Customization")
    customization_window.geometry("600x400")
    customization_window.configure(bg="#c9c1a7")

    # Title label
    title_label = Label(customization_window, text="Room Customization", font=('Times', 30, 'bold'), bg="#c9c1a7", fg="#725700")
    title_label.pack(pady=20)

    # Options for room customization
    def apply_customization():
        # Function to apply customization
        selected_bed = bed_var.get()
        selected_view = view_var.get()
        selected_extras = extras_var.get()
        messagebox.showinfo("Customization Applied", f"Bed Type: {selected_bed}\nView: {selected_view}\nExtras: {selected_extras}")

    bed_var = StringVar(value="King Size")
    view_var = StringVar(value="Sea View")
    extras_var = StringVar(value="None")

    # Bed type options
    bed_label = Label(customization_window, text="Select Bed Type:", font=('Times', 20), bg="#c9c1a7", fg="#725700")
    bed_label.pack(anchor=W, padx=20, pady=5)
    bed_options = ["King Size", "Queen Size", "Single Bed"]
    for option in bed_options:
        Radiobutton(customization_window, text=option, variable=bed_var, value=option, font=('Times', 15), bg="#c9c1a7", fg="#725700").pack(anchor=W, padx=40)

    # View options
    view_label = Label(customization_window, text="Select View:", font=('Times', 20), bg="#c9c1a7", fg="#725700")
    view_label.pack(anchor=W, padx=20, pady=5)
    view_options = ["Sea View", "City View", "Garden View"]
    for option in view_options:
        Radiobutton(customization_window, text=option, variable=view_var, value=option, font=('Times', 15), bg="#c9c1a7", fg="#725700").pack(anchor=W, padx=40)

    # Extras options
    extras_label = Label(customization_window, text="Select Extras:", font=('Times', 20), bg="#c9c1a7", fg="#725700")
    extras_label.pack(anchor=W, padx=20, pady=5)
    extras_options = ["None", "Breakfast Included", "Airport Shuttle", "Spa Access"]
    for option in extras_options:
        Radiobutton(customization_window, text=option, variable=extras_var, value=option, font=('Times', 15), bg="#c9c1a7", fg="#725700").pack(anchor=W, padx=40)

    # Apply button
    apply_button = Button(customization_window, text="Apply Customization", font=('Times', 20), bg="#948363", fg="#ffe9a1", command=apply_customization)
    apply_button.pack(pady=20)

# Example call to room_customization_ui to test it independently
if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the root window
    room_customization_ui()
    root.mainloop()
