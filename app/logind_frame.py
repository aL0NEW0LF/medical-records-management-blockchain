import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import patient_frame as pf
import doctor_frame as df



class logdFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self,parent,fg_color='transparent',corner_radius=20)
        
    
        # Patient Registration Form
        self.tts_label = ctk.CTkLabel(self, font=('Arial', 30), text="Doctor Authentification")
        self.tts_label.place(anchor="center", relx=0.5, rely=0.3)

        #Contact Information Field
        self.contact_entry = ctk.CTkEntry(self, width=300, height=30, placeholder_text="0x.......................")
        self.contact_entry.place(relx=0.5, rely=0.4, anchor="center")
   
        # Login Button
        self.register_button = ctk.CTkButton(self, text="Login")
        self.register_button.place(relx=0.5, rely=0.48, anchor="center")

        
        
        