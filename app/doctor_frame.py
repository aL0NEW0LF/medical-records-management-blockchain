import tkinter as tk
import customtkinter as ctk
import logind_frame as lf

class docFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent,fg_color='transparent',corner_radius=20)
        
        self.svmsmote = ctk.CTkLabel(self,font=('Arial',30), text="wa 3alikom salam ")
        self.svmsmote.place(anchor="center",relx=0.5, rely=0.07)
        
       
        # Register Button
        self.register_button = ctk.CTkButton(self, text="Log Out", command=lambda:self.log_out(lf.logdFrame))
        self.register_button.place(relx=0.92, rely=0.95, anchor="center")
            
    def log_out(self, cont):
                current_frame = self.controller.frames[cont]
                current_frame.configure(fg_color="#101010")
                current_frame.tkraise()
 
    