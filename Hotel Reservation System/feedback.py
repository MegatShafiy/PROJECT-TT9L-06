from tkinter import *
from tkinter import ttk

class FeedbackPage:
    def __init__(self, root):
        self.root = root
        self.root.title("K I N G S T O N  H O T E L - FEEDBACK")
        self.root.geometry("600x400")
        self.root.configure(bg="#c9c1a7")

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title label
        self.label = Label(self.main_frame, text="Feedback", font=('Times', 30, 'bold'), fg="#725700", bg="#c9c1a7")
        self.label.pack(pady=20)

        # Name Label and Entry
        self.name_label = Label(self.main_frame, text="Name:", font=('Times', 20), fg="#725700", bg="#c9c1a7")
        self.name_label.pack(pady=5, anchor=W)
        self.name_entry = Entry(self.main_frame, font=('Times', 18), width=30)
        self.name_entry.pack(pady=5)

        # Feedback Label and Text
        self.feedback_label = Label(self.main_frame, text="Feedback:", font=('Times', 20), fg="#725700", bg="#c9c1a7")
        self.feedback_label.pack(pady=5, anchor=W)
        self.feedback_text = Text(self.main_frame, font=('Times', 18), width=50, height=10)
        self.feedback_text.pack(pady=5)

        # Button styles
        self.button_style = ttk.Style()
        self.button_style.configure('Feedback.TButton', font=('Times', 18), background="#948363", foreground="#ffe9a1")

        # Submit Button
        self.submit_button = ttk.Button(self.main_frame, text="SUBMIT", style='Feedback.TButton', command=self.submit_feedback)
        self.submit_button.pack(pady=10)

        # Back Button
        self.back_button = ttk.Button(self.main_frame, text="BACK", style='Feedback.TButton', command=self.back_to_main)
        self.back_button.pack(pady=10)

    def submit_feedback(self):
        name = self.name_entry.get()
        feedback = self.feedback_text.get("1.0", END).strip()
        print(f"Feedback received from {name}:\n{feedback}\n")

        # Clear the entries after submission
        self.name_entry.delete(0, END)
        self.feedback_text.delete("1.0", END)

        # Show confirmation message
        self.confirmation_label = Label(self.main_frame, text="Thank you for your feedback!", font=('Times', 20), fg="green", bg="#c9c1a7")
        self.confirmation_label.pack(pady=10)

    def back_to_main(self):
        self.root.destroy()

def feedback_ui():
    feedback_root = Tk()
    app = FeedbackPage(feedback_root)
    feedback_root.mainloop()
