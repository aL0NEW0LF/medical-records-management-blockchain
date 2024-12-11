import tkinter as tk
import customtkinter as ctk


class patFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self,parent,fg_color='transparent',corner_radius=20)
        
    
        # Patient Registration Form
        self.tts_label = ctk.CTkLabel(self, font=('Arial', 30), text="A salaamo 3alaykom")
        self.tts_label.place(anchor="center", relx=0.5, rely=0.3)

       

    