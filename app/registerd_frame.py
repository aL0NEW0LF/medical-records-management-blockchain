import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import re




class regdFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent, fg_color='transparent', corner_radius=20)
        
    
        # Doctor Registration Form
        self.tts_label = ctk.CTkLabel(self, font=('Arial', 30), text="Doctor Authantification")
        self.tts_label.place(anchor="center", relx=0.5, rely=0.07)

        # Name Field
        self.name_label = ctk.CTkLabel(self, font=('Arial', 17), text="Full name : ")
        self.name_label.place(anchor="center", relx=0.388, rely=0.2)
        self.name_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="Full name")
        self.name_entry.place(relx=0.56, rely=0.21, anchor="center")

        # Date of Birth Field
        self.dob_label = ctk.CTkLabel(self, font=('Arial', 17), text="Date of Birth : ")
        self.dob_label.place(anchor="center", relx=0.388, rely=0.3)
        self.dob_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="YYYY-MM-DD")
        self.dob_entry.place(relx=0.56, rely=0.31, anchor="center")

        # Contact Information Field
        self.contact_label = ctk.CTkLabel(self, font=('Arial', 17), text="Contact Information : ")
        self.contact_label.place(anchor="center", relx=0.388, rely=0.4)
        self.contact_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="06xxxxxxxx")
        self.contact_entry.place(relx=0.56, rely=0.41, anchor="center")

        # Gender Selection
        self.gender_label = ctk.CTkLabel(self, font=('Arial', 17), text="Gender : ")
        self.gender_label.place(anchor="center", relx=0.388, rely=0.5)
        self.gender_optMenu = ctk.CTkOptionMenu(self, width=190, height=30, values=["Male", "Female"])
        self.gender_optMenu.configure(fg_color="#200E3A")
        self.gender_optMenu.place(relx=0.56, rely=0.5, anchor="center")
        
        #Prof Information Field
        self.contact_label = ctk.CTkLabel(self, font=('Arial', 17), text="Dotor speciality : ")
        self.contact_label.place(anchor="center", relx=0.388, rely=0.6)
        self.contact_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="speciality")
        self.contact_entry.place(relx=0.56, rely=0.6, anchor="center")
        
        

        #Contact Information Field
        self.contact_label = ctk.CTkLabel(self, font=('Arial', 17), text="Licence Number: ")
        self.contact_label.place(anchor="center", relx=0.388, rely=0.7)
        self.contact_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="Licence Number")
        self.contact_entry.place(relx=0.56, rely=0.7, anchor="center")

        # Register Button
        self.register_button = ctk.CTkButton(self, text="Register", command=self.register_patient)
        self.register_button.place(relx=0.5, rely=0.8, anchor="center")

    def validate_dob(self, dob):
        # Validate Date of Birth (YYYY-MM-DD format)
        date_pattern = r"^(20[0-2][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
        if not re.match(date_pattern, dob):
            return False
        year, month, day = map(int, dob.split('-'))
        if year > 2024:
            return False
        if month > 12 or day > 31:
            return False
        return True

    def validate_phone(self, phone):
        # Validate Phone Number (must be 10 digits, starting with 06 or 07)
        if len(phone) != 10 or not phone.isdigit():
            return False
        if not (phone.startswith("06") or phone.startswith("07")):
            return False
        return True

    def register_patient(self):
        # Collect data from the form
        name = self.name_entry.get()
        dob = self.dob_entry.get()
        contact = self.contact_entry.get()
        gender = self.gender_optMenu.get()

        # Validate Date of Birth
        if not self.validate_dob(dob):
            messagebox.showerror("Invalid Date of Birth", "Please enter a valid date in the format YYYY-MM-DD.")
            return
        
        # Validate Phone Number
        if not self.validate_phone(contact):
            messagebox.showerror("Invalid Phone Number", "Please enter a valid phone number.")
            return

        # Example logic to register the patient (you can integrate blockchain logic here)
        print(f"Name: {name}, Date of Birth: {dob}, Contact Info: {contact}, Gender: {gender}")
        
        # Example message box for confirmation
        messagebox.showinfo("Patient Registration", f"Patient {name} registered successfully!")