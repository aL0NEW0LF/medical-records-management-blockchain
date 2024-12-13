# import tkinter as tk
# import customtkinter as ctk
# import patient_frame as pl
# from tkinter import messagebox

# class logpFrame(ctk.CTkFrame):
#     def __init__(self, parent, controller):
#         self.controller = controller
#         ctk.CTkFrame.__init__(self,parent,fg_color='transparent',corner_radius=20)
        
    
#         # Patient Registration Form
#         self.tts_label = ctk.CTkLabel(self, font=('Arial', 30), text="Patient Authentification")
#         self.tts_label.place(anchor="center", relx=0.5, rely=0.3)

#         #Contact Information Field
#         self.contact_entry = ctk.CTkEntry(self, width=300, height=30, placeholder_text="0x.......................")
#         self.contact_entry.place(relx=0.5, rely=0.4, anchor="center")
   
#         # Login Button
#         self.register_button = ctk.CTkButton(self, text="Login",command=lambda:self.show_frame(pl.pFrame))
#         self.register_button.place(relx=0.5, rely=0.48, anchor="center")
#         x= self.contact_entry.get()


#         def show_frame(self, cont):
#             x= self.contact_entry.get()
#             if x=="1":
#                 current_frame = self.controller.frames[cont]
#                 current_frame.configure(fg_color="#101010")
#                 current_frame.tkraise()
#             else:
#                 tk.messagebox.showerror('Python Error', "Please enter a valide key")


import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import patient_frame as pf




class logpFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
            self.controller = controller
            ctk.CTkFrame.__init__(self,parent,fg_color='transparent',corner_radius=20)
            
        
            # Patient Registration Form
            self.tts_label = ctk.CTkLabel(self, font=('Arial', 30), text="Patient Authentification")
            self.tts_label.place(anchor="center", relx=0.5, rely=0.3)

            #Contact Information Field
            self.contact_entry = ctk.CTkEntry(self, width=300, height=30, placeholder_text="Press 1")
            self.contact_entry.place(relx=0.5, rely=0.4, anchor="center")
    
            # Login Button
            self.register_button = ctk.CTkButton(self, text="Login",command=lambda: self.show_main_frame(pf.pFrame))
            self.register_button.place(relx=0.5, rely=0.48, anchor="center")


    def show_main_frame(self, cont):
            x=self.contact_entry.get()
            if x=="1":
                current_frame = self.controller.frames[cont]
                current_frame.configure(fg_color="#101010")
                current_frame.tkraise()
            else:
                tk.messagebox.showerror('Python Error', "Please enter a valide key")
