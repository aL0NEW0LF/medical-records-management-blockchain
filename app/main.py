"""
This script represents the main application for the ML Toolkit project.
It imports necessary modules and defines the main application class.
The class creates a GUI window and sets up the menu bar and frames for different functionalities.
"""

import platform
import tkinter as tk
import customtkinter as ctk
import customMenu
import os
import ctypes
import home_frame as hf
import audit_frame as af
import register_frame as rf
import loginp_frame as lpf
import doctor_frame as df
import registerd_frame as rdf
import logind_frame as ldf
import patient_frame as pl


# import visualization.vizualization_frame as vsf
# import import_frame as imf
# import docs as dcs

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
            

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        """
        Initializes the main application class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("DOSSIER MEDICAL")
        self.geometry(f"{1300}x{720}")
        self.myappid = 'heh' # arbitrary string
        if platform.system() == "Windows":
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.myappid)
        menu = customMenu.Menu(self)

        
        
        home_button = menu.menu_button(text="Home", command=lambda:self.show_main_frame(hf.homeFrame))
        # patient_button = menu.menu_button(text="Patient", command=lambda: self.show_main_frame("patient",pf.patFrame))
        
        Model_menu = menu.menu_bar(text="Patient", tearoff=0,)
        Model_menu.add_command(label="Login",command=lambda:self.show_main_frame(lpf.logpFrame))
        Model_menu.add_command(label="Register",command=lambda:self.show_main_frame(rf.regFrame))
        
        # doctor_button = menu.menu_button(text="Doctor",command=lambda: self.show_main_frame("doctor", df.docFrame))
        
        Model_menu = menu.menu_bar(text="doctor", tearoff=0,)
        Model_menu.add_command(label="Login",command=lambda:self.show_main_frame(ldf.logdFrame))
        Model_menu.add_command(label="Register",command=lambda:self.show_main_frame(rdf.regdFrame))
        
        audit_button = menu.menu_button(text="Audit",command=lambda: self.show_main_frame(af.auditFrame))
        about_menu = menu.menu_button(text="About", command=lambda:tk.messagebox.showinfo("About", "ML Toolkit - V1.0\nCreated by:\n\n- Ahmed Samady | @Samashi47\n- Fahd Chibani | @Dhafahd\n- hamid | @hamid"))
        
           
        container = ctk.CTkFrame(self, width=self.winfo_width(), height=self.winfo_height())
        self.resizable(False, False)
        container.configure(fg_color="#101010")
        container.pack(side="top", expand=True, fill="both")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (pl.pFrame,hf.homeFrame,lpf.logpFrame,df.docFrame,af.auditFrame,rf.regFrame,rdf.regdFrame,ldf.logdFrame,df.docFrame):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_main_frame(hf.homeFrame)
    
    def show_main_frame(self, cont):
        """
        Shows the main frame.

        Args:
            cont: The frame to show.
        """
        current_frame = self.frames[cont]
        current_frame.configure(fg_color="#101010")
        current_frame.tkraise()


app = App()
app.protocol("WM_DELETE_WINDOW", app.quit)
app.mainloop()