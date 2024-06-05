import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.app = root
        self.app.title('Login')
        self.app.geometry('450x360')
        self.app.config(bg='#001220')

        self.font1 = ('Helvetica', 25, 'bold')
        self.font2 = ('Arial', 17, 'bold')
        self.font3 = ('Arial', 13, 'bold')
        self.font4 = ('Arial', 13, 'bold', 'underline')

        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users(
                username TEXT NOT NULL,
                password TEXT NOT NULL)'''
        )

        self.setup_signup_screen()

    def setup_signup_screen(self):
        self.frame1 = customtkinter.CTkFrame(self.app, bg_color='#001220', fg_color='#001220', width=500, height=500)
        self.frame1.place(x=0, y=0)

        self.image1 = PhotoImage(file="PROJECT-TT9L-06/Images/download.png")
        self.image1_label = Label(self.frame1, image=self.image1, bg='#001220', width=250, height=500)
        self.image1_label.place(x=0, y=0)

        self.signup_label = customtkinter.CTkLabel(self.frame1, font=self.font1, text='Sign Up', text_color='#fff', bg_color='#001220')
        self.signup_label.place(x=280, y=20)

        self.username_entry = customtkinter.CTkEntry(self.frame1, font=self.font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                            border_color='#004780', border_width=3, placeholder_text='Username',
                                            placeholder_text_color='#a3a3a3', width=200, height=50)
        self.username_entry.place(x=230, y=80)

        self.password_entry = customtkinter.CTkEntry(self.frame1, font=self.font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                            border_color='#004780', border_width=3, placeholder_text='Password',
                                            placeholder_text_color='#a3a3a3', width=200, height=50)
        self.password_entry.place(x=230, y=150)

        self.signup_button = customtkinter.CTkButton(self.frame1, command=self.signup, font=self.font2, text_color='#fff', text='Sign Up', fg_color='#00965d',
                                            hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5,
                                            width=120)
        self.signup_button.place(x=230, y=220)

        self.login_label = customtkinter.CTkLabel(self.frame1, font=self.font3, text='Already have an account?', text_color='#fff', bg_color='#001220')
        self.login_label.place(x=230, y=250)

        self.login_button = customtkinter.CTkButton(self.frame1, command=self.setup_login_screen, font=self.font4, text_color='#00bf77', text='Login', fg_color='#001220',
                                            hover_color='#001220', cursor='hand2', width=40)
        self.login_button.place(x=395, y=250)

    def setup_login_screen(self):
        self.frame1.destroy()
        self.frame2 = customtkinter.CTkFrame(self.app, bg_color='#001220', fg_color='#001220', width=470, height=360)
        self.frame2.place(x=0, y=0)

        self.image1 = PhotoImage(file="PROJECT-TT9L-06/Images/download.png")
        self.image1_label = Label(self.frame2, image=self.image1, bg='#001220', width=250, height=500)
        self.image1_label.place(x=0, y=0)
        self.frame2.image1 = self.image1

        self.login_label2 = customtkinter.CTkLabel(self.frame2, font=self.font1, text='Log in', text_color='#fff', bg_color='#001220')
        self.login_label2.place(x=280, y=20)

        self.username_entry2 = customtkinter.CTkEntry(self.frame2, font=self.font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                             border_color='#004780', border_width=3, placeholder_text='Username',
                                             placeholder_text_color='#a3a3a3', width=200, height=50)
        self.username_entry2.place(x=230, y=80)

        self.password_entry2 = customtkinter.CTkEntry(self.frame2, font=self.font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                             border_color='#004780', border_width=3, placeholder_text='Password',
                                             placeholder_text_color='#a3a3a3', width=200, height=50)
        self.password_entry2.place(x=230, y=150)

        self.login_button2 = customtkinter.CTkButton(self.frame2, command=self.login_account, font=self.font2, text_color='#fff', text='Log In', fg_color='#00965d',
                                            hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5,
                                            width=120)
        self.login_button2.place(x=230, y=220)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username != '' and password != '':
            self.cursor.execute('SELECT username FROM users WHERE username=?', [username])  
            if self.cursor.fetchone() is not None:
                messagebox.showerror('Error', 'Username already exists')
            else:
                encoded_password = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                self.cursor.execute('INSERT INTO users VALUES(?, ?)', [username, hashed_password])
                self.conn.commit()
                messagebox.showinfo('Success', 'Account created successfully')
                self.setup_login_screen()  
        else:
            messagebox.showerror('Error', 'Please fill all the fields')

    def login_account(self):
        username = self.username_entry2.get()
        password = self.password_entry2.get()
        if username != '' and password != '':
            self.cursor.execute('SELECT password FROM users WHERE username=?', [username])  
            result = self.cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                    messagebox.showinfo('Success', 'Logged in successfully.')
                else:
                    messagebox.showerror('Error', 'Invalid password')
            else:
                messagebox.showerror('Error', 'Invalid username')
        else:
            messagebox.showerror('Error', 'Please fill all the fields')

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = App(root)
    root.mainloop()
