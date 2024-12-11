import tkinter as tk
import customtkinter as ctk


class docFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent,fg_color='transparent',corner_radius=20)
        
        self.svmsmote = ctk.CTkLabel(self,font=('Arial',30), text="wa 3alikom salam ")
        self.svmsmote.place(anchor="center",relx=0.5, rely=0.07)
        
       
        
    