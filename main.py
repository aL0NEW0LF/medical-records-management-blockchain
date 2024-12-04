from tkinter import *
from tkinter import ttk
import tkinter as tk


def dummy_function():
    pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))
        self.title("Medical Record System - Login")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.account_label = tk.Label(self, text="Account Key")
        self.account_label.pack()
        self.account_entry = tk.Entry(self)
        self.account_entry.pack()
        self.login_button = tk.Button(self, text="Login", command=dummy_function)
        self.login_button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
