import tkinter as tk
from tkinter import messagebox
from MainPage import MainPage
from db import db


class LoginPage:
    def __init__(self, master):
        self.root = master

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        self.root.geometry('300x180')

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.username.set('admin')
        self.password.set('123456')

        self.create_page()

    def create_page(self):
        tk.Label(self.login_frame, width=15).grid(row=0, column=0)

        tk.Label(self.login_frame, text='Account').grid(row=1, column=0)
        tk.Entry(self.login_frame, textvariable=self.username).grid(
            row=1, column=1)

        tk.Label(self.login_frame, text='Password').grid(row=2, column=0)
        tk.Entry(self.login_frame, textvariable=self.password).grid(
            row=2, column=1)

        tk.Button(self.login_frame, text='Login',
                  command=self.login_function).grid(row=3, column=0)
        tk.Button(self.login_frame, text='Exit',
                  command=self.root.quit).grid(row=3, column=1)

    def login_function(self):
        username = self.username.get()
        password = self.password.get()
        flag, message = db.check_login(username, password)
        if flag:
            self.login_frame.destroy()

            # Switch to Main page
            MainPage(self.root)
        else:
            messagebox.showwarning(
                title='Warning', message=message)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('SIS v0.0.5')

    LoginPage(master=root)

    root.mainloop()
