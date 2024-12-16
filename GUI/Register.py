import customtkinter as ctk
import tkinter as tk
from PIL import Image
from web3 import Web3
import Login as lg
import re
from datetime import datetime
from eth_account.messages import encode_defunct
from hexbytes import HexBytes
import json
import random

class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)
        
        self.tabview = ctk.CTkTabview(master=self, segmented_button_selected_color=("#8651ff", "#8651ff"), segmented_button_selected_hover_color=("#6940c9", "#6940c9"))
        self.tabview.pack_configure(expand=True, fill="both")
        ########## Doctor Registration ##########
        self.DoctorRegister = self.tabview.add("Register as a Doctor")
        self.FRAME0 = ctk.CTkFrame(master=self.DoctorRegister, fg_color="transparent")
        self.FRAME0.pack_propagate(False)
        self.FRAME0.pack(pady=(0, 0), expand=1, fill="both", padx=(0, 0), side="left")
        medical_icon = r"GUI/Assets/medical-history_881760.png"
        self.LABEL1 = ctk.CTkLabel(master=self.FRAME0, text="", anchor="w", text_color=("gray10", "#FFFFFF"), image=ctk.CTkImage(Image.open(medical_icon), size=(48, 48)), font=ctk.CTkFont(size=15))
        self.LABEL1.pack(pady=(20, 0), fill="x", padx=(20, 0))
        doctor_text = "Register as a Doctor\nto securely manage\npatient records and\nCOLLABORATE"
        self.LABEL2 = ctk.CTkLabel(master=self.FRAME0, text=doctor_text, justify="left", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=40))
        self.LABEL2.pack(padx=(30, 0), expand=1, fill="x")
        self.FRAME1 = ctk.CTkFrame(master=self.DoctorRegister)
        self.FRAME1.pack_propagate(False)
        self.FRAME1.pack(pady=(20, 20), expand=1, fill="both", padx=(5, 20), side="left")
        self.FRAME2 = ctk.CTkScrollableFrame(master=self.FRAME1, width=565, height=500, fg_color="transparent")
        self.FRAME2.pack(expand=True, fill="both", padx=20, pady=20)
        self.LABEL3 = ctk.CTkLabel(master=self.FRAME2, text="Register", anchor="n", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=39))
        self.LABEL3.pack(fill="x")
        self.LABEL4 = ctk.CTkLabel(master=self.FRAME2, text="Welcome! Please enter your account details.", anchor="w", text_color=("gray10", "#b4b4b4"), wraplength=332, justify="left", font=ctk.CTkFont(size=14))
        self.LABEL4.pack(pady=(10, 10), fill="x")
        self.FRAME3 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME3.pack(pady=(10, 0), fill="x")
        self.LABEL5 = ctk.CTkLabel(master=self.FRAME3, text="Account Address", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL5.pack(fill="x")
        self.ENTRY1 = ctk.CTkEntry(master=self.FRAME3, placeholder_text="0x"+40*"0", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"), width=222)
        self.ENTRY1.pack(fill="x")
        self.FRAME4 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME4.pack(pady=(10, 0), fill="x")
        self.LABEL6 = ctk.CTkLabel(master=self.FRAME4, text="Full Name", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL6.pack(fill="x")
        self.ENTRY2 = ctk.CTkEntry(master=self.FRAME4, placeholder_text="Dr. John Doe", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"))
        self.ENTRY2.pack(fill="x")
        self.FRAME5 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME5.pack(pady=(10, 0), fill="x")
        self.LABEL7 = ctk.CTkLabel(master=self.FRAME5, text="Date of Birth", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL7.pack(fill="x")
        self.ENTRY3 = ctk.CTkEntry(master=self.FRAME5, placeholder_text="DD/MM/YYYY", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"))
        self.ENTRY3.pack(fill="x")
        self.FRAME6 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME6.pack(pady=(10, 0), fill="x")
        self.LABEL8 = ctk.CTkLabel(master=self.FRAME6, text="Phone Number", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL8.pack(fill="x")
        self.ENTRY4 = ctk.CTkEntry(master=self.FRAME6, placeholder_text="1234567890", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"))
        self.ENTRY4.pack(fill="x")
        self.FRAME7 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME7.pack(pady=(10, 0), fill="x")
        self.LABEL9 = ctk.CTkLabel(master=self.FRAME7, text="Gender", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL9.pack(fill="x")
        self.COMBOBOX1 = ctk.CTkComboBox(master=self.FRAME7, values=["Male", "Female"], height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"),state="readonly")
        self.COMBOBOX1.pack(fill="x")
        self.FRAME8 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME8.pack(pady=(10, 0), fill="x")
        self.LABEL10 = ctk.CTkLabel(master=self.FRAME8, text="Specialization", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL10.pack(fill="x")
        self.ENTRY5 = ctk.CTkEntry(master=self.FRAME8, placeholder_text="Cardiologist", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"))
        self.ENTRY5.pack(fill="x")
        self.FRAME9 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME9.pack(pady=(10, 0), fill="x")
        self.LABEL11 = ctk.CTkLabel(master=self.FRAME9, text="License Number", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL11.pack(fill="x")
        self.ENTRY6 = ctk.CTkEntry(master=self.FRAME9, placeholder_text="1234567890", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"))
        self.ENTRY6.pack(fill="x")
        self.BUTTON1 = ctk.CTkButton(master=self.FRAME2, text="Register", height=35, text_color=("gray98", "#FFFFFF"), fg_color=("#8651ff", "#8651ff"), hover_color=("#6940c9", "#6940c9"), width=500, corner_radius=3, command=self.register_doctor)
        self.BUTTON1.pack(pady=(20, 0), fill="x")
        self.FRAME10 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME10.pack(pady=(10, 0), fill="x")
        self.LABEL12 = ctk.CTkLabel(master=self.FRAME10, text="Already have an Account?", text_color=("gray10", "#FFFFFF"))
        self.LABEL12.pack(side="left")
        self.BUTTON2 = ctk.CTkButton(master=self.FRAME10, text="Login", width=70, fg_color="transparent", hover=False, height=0, text_color=("#000000", "#FFFFFF"), command=lambda:self.controller.show_main_frame(lg.LoginFrame))
        self.BUTTON2.pack(side="left")
        
        ########## Patient Registration ##########
        self.PatientRegister = self.tabview.add("Register as a Patient")
        self.FRAME11 = ctk.CTkFrame(master=self.PatientRegister, fg_color="transparent")
        self.FRAME11.pack_propagate(False)
        self.FRAME11.pack(pady=(0, 0), expand=1, fill="both", padx=(0, 0), side="left")
        medical_icon = r"GUI/Assets/medical-history_881760.png"
        self.LABEL13 = ctk.CTkLabel(master=self.FRAME11, text="", anchor="w", text_color=("gray10", "#FFFFFF"), image=ctk.CTkImage(Image.open(medical_icon), size=(48, 48)), font=ctk.CTkFont(size=15))
        self.LABEL13.pack(pady=(20, 0), fill="x", padx=(20, 0))
        patient_text = "Are you a Patient?\nRegister to share\nyour medical records\nSECURELY"
        self.LABEL14 = ctk.CTkLabel(master=self.FRAME11, text=patient_text, justify="left", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=40))
        self.LABEL14.pack(padx=(30, 0), expand=1, fill="x")
        self.FRAME12 = ctk.CTkFrame(master=self.PatientRegister)
        self.FRAME12.pack_propagate(False)
        self.FRAME12.pack(pady=(20, 20), expand=1, fill="both", padx=(5, 20), side="left")
        self.FRAME13 = ctk.CTkScrollableFrame(master=self.FRAME12, width=565, height=500, fg_color="transparent")
        self.FRAME13.pack(expand=True, fill="both", padx=20, pady=20)
        self.LABEL15 = ctk.CTkLabel(master=self.FRAME13, text="Register", anchor="n", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=39))
        self.LABEL15.pack(fill="x")
        self.LABEL16 = ctk.CTkLabel(master=self.FRAME13, text="Welcome! Please enter your account details.", anchor="w", text_color=("gray10", "#b4b4b4"), wraplength=332, justify="left", font=ctk.CTkFont(size=14))
        self.LABEL16.pack(pady=(10, 10), fill="x")
        self.FRAME14 = ctk.CTkFrame(master=self.FRAME13, fg_color="transparent")
        self.FRAME14.pack(pady=(10, 0), fill="x")
        self.LABEL17 = ctk.CTkLabel(master=self.FRAME14, text="Account Address", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL17.pack(fill="x")
        self.ENTRY7 = ctk.CTkEntry(master=self.FRAME14, placeholder_text="0x"+40*"0", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"), width=222)
        self.ENTRY7.pack(fill="x")
        self.FRAME15 = ctk.CTkFrame(master=self.FRAME13, fg_color="transparent")
        self.FRAME15.pack(pady=(10, 0), fill="x")
        self.LABEL18 = ctk.CTkLabel(master=self.FRAME15, text="Full Name", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL18.pack(fill="x")
        self.ENTRY8 = ctk.CTkEntry(master=self.FRAME15, placeholder_text="John Doe", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"))
        self.ENTRY8.pack(fill="x")
        self.FRAME16 = ctk.CTkFrame(master=self.FRAME13, fg_color="transparent")
        self.FRAME16.pack(pady=(10, 0), fill="x")
        self.LABEL19 = ctk.CTkLabel(master=self.FRAME16, text="Date of Birth", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL19.pack(fill="x")
        self.ENTRY9 = ctk.CTkEntry(master=self.FRAME16, placeholder_text="DD/MM/YYYY", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"))
        self.ENTRY9.pack(fill="x")
        self.FRAME17 = ctk.CTkFrame(master=self.FRAME13, fg_color="transparent")
        self.FRAME17.pack(pady=(10, 0), fill="x")
        self.LABEL20 = ctk.CTkLabel(master=self.FRAME17, text="Phone Number", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL20.pack(fill="x")
        self.ENTRY10 = ctk.CTkEntry(master=self.FRAME17, placeholder_text="1234567890", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"))
        self.ENTRY10.pack(fill="x")
        self.FRAME18 = ctk.CTkFrame(master=self.FRAME13, fg_color="transparent")
        self.FRAME18.pack(pady=(10, 0), fill="x")
        self.LABEL21 = ctk.CTkLabel(master=self.FRAME18, text="Gender", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL21.pack(fill="x")
        self.COMBOBOX2 = ctk.CTkComboBox(master=self.FRAME18, values=["Male", "Female"], height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"),state="readonly")
        self.COMBOBOX2.pack(fill="x")
        self.BUTTON3 = ctk.CTkButton(master=self.FRAME13, text="Register", height=35, text_color=("gray98", "#FFFFFF"), fg_color=("#8651ff", "#8651ff"), hover_color=("#6940c9", "#6940c9"), width=500, corner_radius=3, command=self.register_patient)
        self.BUTTON3.pack(pady=(20, 0), fill="x")
        self.FRAME19 = ctk.CTkFrame(master=self.FRAME13, fg_color="transparent")
        self.FRAME19.pack(pady=(10, 0), fill="x")
        self.LABEL22 = ctk.CTkLabel(master=self.FRAME19, text="Already have an Account?", text_color=("gray10", "#FFFFFF"))
        self.LABEL22.pack(side="left")
        self.BUTTON4 = ctk.CTkButton(master=self.FRAME19, text="Login", width=70, fg_color="transparent", hover=False, height=0, text_color=("#000000", "#FFFFFF"), command=lambda:self.controller.show_main_frame(lg.LoginFrame))
        self.BUTTON4.pack(side="left")
    
        self.web3 = self.controller.web3
        self.doctor_contract = self.controller.doctor_contract
        self.patient_contract = self.controller.patient_contract
        self.audit_contract = self.controller.audit_contract
    
    def validate_private_key(self, private_key):
        if not private_key or not private_key.startswith("0x") or len(private_key) != 66:
            tk.messagebox.showerror("Error", "Invalid private key.")
            return False
        return True
    
    def verify_credentials(self, address, name, dob, phone, gender):
        if address == "" or not Web3.is_address(address):
            tk.messagebox.showerror("Error", "Please enter a valid Ethereum address")
            return False
        if name == "" or re.match(r"/^[a-z ,.'-]+$/i", name):
            tk.messagebox.showerror("Error", "Please enter your full name")
            return False
        if dob == "" or not re.match(r'\d{1,2}\/\d{1,2}\/\d{4}', dob):
            tk.messagebox.showerror("Error", "Please enter date of birth in DD/MM/YYYY format")
            return False
        try:
            day, month, year = map(int, dob.split('/'))
            if month < 1 or month > 12:
                tk.messagebox.showerror("Error", "Month must be between 1 and 12")
                return False
            if day < 1 or day > 31:
                tk.messagebox.showerror("Error", "Day must be between 1 and 31")
                return False
            birth_date = datetime(year, month, day)
            age = (datetime.now() - birth_date).days / 365.25
            if age < 18:
                tk.messagebox.showerror("Error", "You must be at least 18 years old")
                return False
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid date format")
            return False
        
        if phone == "" or not phone.isdigit() or len(phone) < 10:
            tk.messagebox.showerror("Error", "Please enter a valid phone number")
            return False
        
        if gender == "":
            tk.messagebox.showerror("Error", "Please select a gender")
            return False
        
        return True
    
    def get_signature(self, address):
        nonce = random.randint(1000000, 99999999999)
        signable_message = encode_defunct(text=str(nonce))
        dialog = ctk.CTkToplevel()
        dialog.title("Sign Message")
        
        message_label = ctk.CTkLabel(dialog, text="Please sign this message with your wallet:")
        message_label.pack(padx=20, pady=(20, 0))
        
        text_widget = ctk.CTkTextbox(dialog, height=50, width=300)
        text_widget.insert("1.0", str(nonce))
        text_widget.configure(state="disabled")
        text_widget.pack(padx=20, pady=(0, 20))
        
        entry = ctk.CTkEntry(dialog, width=300)
        entry.pack(padx=20, pady=(0, 20))
        
        button = ctk.CTkButton(dialog, text="OK", fg_color=("#8651ff", "#8651ff"),
                            text_color=("gray98", "#FFFFFF"))
        button.pack(padx=20, pady=(0, 20))
        
        signature = None
        def on_ok():
            nonlocal signature
            signature = entry.get()
            dialog.destroy()
        
        button.configure(command=on_ok)
        dialog.wait_window()
        
        try:
            signature = HexBytes(json.loads(signature)["sig"])
            recovered_address = self.web3.eth.account.recover_message(signable_message, signature=signature)
            
            if recovered_address.lower() != address.lower():
                tk.messagebox.showerror('Error', "Signature verification failed")
                return None
                
            return recovered_address
        except (json.JSONDecodeError, ValueError) as e:
            tk.messagebox.showerror('Python Error', str(e))
            return None
    
    def get_doctor_unsigned_tx(self, address, name, dob, phone, gender, specialization, license):
        try:
            checksum_address = self.web3.to_checksum_address(address.lower())
            tx = self.doctor_contract.functions.registerDoctor(
                name, dob, phone, gender, specialization, license
            ).build_transaction({
                'from': checksum_address,
                'nonce': self.web3.eth.get_transaction_count(checksum_address),
                'gas': self.doctor_contract.functions.registerDoctor(
                    name, dob, phone, gender, specialization, license
                ).estimate_gas({'from': checksum_address}),
                'gasPrice': self.web3.eth.gas_price
            })
            
            return tx
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to create transaction: {str(e)}")
            return None
        
    def register_doctor(self):
        address = self.ENTRY1.get()
        name = self.ENTRY2.get()
        dob = self.ENTRY3.get()
        phone = self.ENTRY4.get()
        gender = self.COMBOBOX1.get()
        specialization = self.ENTRY5.get()
        license = self.ENTRY6.get()
        
        valid = self.verify_credentials(address, name, dob, phone, gender)
        
        if valid == False:
            return
        
        if specialization == "":
            tk.messagebox.showerror("Error", "Please enter your specialization")
            return
        
        if license == "" or not license.isdigit():
            tk.messagebox.showerror("Error", "Please enter a valid license number")
            return
        recovered_address = self.get_signature(address)
        if not recovered_address:
            return
        raw_tx = self.get_doctor_unsigned_tx(address, "Dr. "+name, dob, phone, gender, specialization, license)
        if raw_tx is None:
            return
        try:
            tx_hash = self.web3.eth.send_transaction(raw_tx)
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt['status'] == 1:
                tk.messagebox.showinfo("Success", "Doctor registration successful!")
                address = self.web3.to_checksum_address(address.lower())
                tx_hash = self.audit_contract.functions.logDoctorRegistration(address, name).transact({'from': address})
                receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
                self.controller.show_main_frame(lg.LoginFrame)
                self.ENTRY1.delete(0, tk.END)
                self.ENTRY2.delete(0, tk.END)
                self.ENTRY3.delete(0, tk.END)
                self.ENTRY4.delete(0, tk.END)
                self.COMBOBOX1.set("")
                self.ENTRY5.delete(0, tk.END)
                self.ENTRY6.delete(0, tk.END)
            else:
                tk.messagebox.showerror("Error", "Transaction failed")
        except Exception as e:
            print(e)
            tk.messagebox.showerror("Error", f"Failed to broadcast: {str(e)}")
            return
        
    def get_patient_unsigned_tx(self, address, name, dob, phone, gender):
        try:
            checksum_address = self.web3.to_checksum_address(address.lower())
            tx = self.patient_contract.functions.registerPatient(
                name, dob, phone, gender
            ).build_transaction({
                'from': checksum_address,
                'nonce': self.web3.eth.get_transaction_count(checksum_address),
                'gas': self.patient_contract.functions.registerPatient(
                    name, dob, phone, gender
                ).estimate_gas({'from': checksum_address}),
                'gasPrice': self.web3.eth.gas_price
            })
            
            return tx
        
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to create transaction: {str(e)}")
            return None
    
    
    def register_patient(self):
        address = self.ENTRY7.get()
        name = self.ENTRY8.get()
        dob = self.ENTRY9.get()
        phone = self.ENTRY10.get()
        gender = self.COMBOBOX2.get()
        
        valid = self.verify_credentials(address, name, dob, phone, gender)
        if valid == False:
            return
        recovered_address = self.get_signature(address)
        if not recovered_address:
            return
        raw_tx = self.get_patient_unsigned_tx(address, name, dob, phone, gender)
        if raw_tx == None:
            return
        try:
            tx_hash = self.web3.eth.send_transaction(raw_tx)
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt['status'] == 1:
                tk.messagebox.showinfo("Success", "Patient registration successful!")
                address = self.web3.to_checksum_address(address.lower())
                tx_hash = self.audit_contract.functions.logPatientRegistration(address, name).transact({'from': address})
                receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
                self.controller.show_main_frame(lg.LoginFrame)
                self.ENTRY7.delete(0, tk.END)
                self.ENTRY8.delete(0, tk.END)
                self.ENTRY9.delete(0, tk.END)
                self.ENTRY10.delete(0, tk.END)
                self.COMBOBOX2.set("")
            else:
                tk.messagebox.showerror("Error", "Transaction failed")
        except Exception as e:
            print(e)
            tk.messagebox.showerror("Error", f"Failed to broadcast: {str(e)}")
            return