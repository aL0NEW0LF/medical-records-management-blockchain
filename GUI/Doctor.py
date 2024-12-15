import customtkinter as ctk
import tkinter as tk
import os
import Login as lg

class DoctorFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)  
        self.tabview = ctk.CTkTabview(master=self, segmented_button_selected_color=("#8651ff", "#8651ff"), segmented_button_selected_hover_color=("#6940c9", "#6940c9"))
        self.tabview.pack_configure(expand=True, fill="both")
        
        ########## Profile ##########
        self.profile = self.tabview.add("Profile")
        self.FRAME0 = ctk.CTkFrame(master=self.profile, fg_color="transparent")
        self.FRAME0.pack_propagate(False)
        self.FRAME0.pack(pady=(20, 20), padx=(40, 40), expand=1, fill="both")
        self.LABEL1 = ctk.CTkLabel(master=self.FRAME0, text="Profile", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=42, weight="bold"))
        self.LABEL1.pack(pady=(0, 30))
        self.FRAME1 = ctk.CTkFrame(master=self.FRAME0, fg_color="transparent")
        self.FRAME1.pack(expand=True, fill="both", padx=20, pady=20)
        self.LABEL2 = ctk.CTkLabel(master=self.FRAME1, text="Logged in as:", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL2.grid(row=0, column=0, pady=5, sticky="w", padx=10)
        self.LABEL3 = ctk.CTkLabel(master=self.FRAME1, text="0x"+40*"0", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL3.grid(row=0, column=1, pady=5, sticky="w", padx=10)
        self.LABEL4 = ctk.CTkLabel(master=self.FRAME1, text="Name:", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL4.grid(row=1, column=0, pady=5, sticky="w", padx=10)
        self.LABEL5 = ctk.CTkLabel(master=self.FRAME1, text="John Doe", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL5.grid(row=1, column=1, pady=5, sticky="w", padx=10)
        self.LABEL6 = ctk.CTkLabel(master=self.FRAME1, text="Date of Birth:", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL6.grid(row=2, column=0, pady=5, sticky="w", padx=10)
        self.LABEL7 = ctk.CTkLabel(master=self.FRAME1, text="01/01/2000", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL7.grid(row=2, column=1, pady=5, sticky="w", padx=10)
        self.LABEL8 = ctk.CTkLabel(master=self.FRAME1, text="Phone Number:", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL8.grid(row=3, column=0, pady=5, sticky="w", padx=10)
        self.LABEL9 = ctk.CTkLabel(master=self.FRAME1, text="0123456789", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL9.grid(row=3, column=1, pady=5, sticky="w", padx=10)
        self.LABEL10 = ctk.CTkLabel(master=self.FRAME1, text="Gender:", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL10.grid(row=4, column=0, pady=5, sticky="w", padx=10)
        self.LABEL11 = ctk.CTkLabel(master=self.FRAME1, text="Male/Female", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL11.grid(row=4, column=1, pady=5, sticky="w", padx=10)
        self.LABEL12 = ctk.CTkLabel(master=self.FRAME1, text="Specialization:", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL12.grid(row=5, column=0, pady=5, sticky="w", padx=10)
        self.LABEL13 = ctk.CTkLabel(master=self.FRAME1, text="Cardiologist", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL13.grid(row=5, column=1, pady=5, sticky="w", padx=10)
        self.LABEL14 = ctk.CTkLabel(master=self.FRAME1, text="License Number:", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL14.grid(row=6, column=0, pady=5, sticky="w", padx=10)
        self.LABEL15 = ctk.CTkLabel(master=self.FRAME1, text="123456789", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL15.grid(row=6, column=1, pady=5, sticky="w", padx=10)
        self.FRAME1.grid_columnconfigure(1, weight=1)
        self.BUTTON1 = ctk.CTkButton(master=self.FRAME0, text="Logout", fg_color="#8651ff", hover_color="#6940c9", command=lambda: self.controller.show_main_frame(lg.LoginFrame))
        self.BUTTON1.pack(pady=(20, 0))
        
        ########## Doctor Medical Records ##########
        self.medical_records = self.tabview.add("My Medical Records")
        self.FRAME2 = ctk.CTkFrame(master=self.medical_records, fg_color="transparent")
        self.FRAME2.pack_propagate(False)
        self.FRAME2.pack(pady=(20, 20), padx=(40, 40), expand=1, fill="both")
        self.LABEL16 = ctk.CTkLabel(master=self.FRAME2, text="My Medical Records", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=42, weight="bold"))
        self.LABEL16.pack(pady=(0, 30))
        self.SCROLLABLE_FRAME1 = ctk.CTkScrollableFrame(master=self.FRAME2)
        self.SCROLLABLE_FRAME1.pack(pady=10, padx=20, fill="both", expand=True)
        style = tk.ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Custom.Treeview.Heading",
                        background="#8651ff",
                        foreground="white",
                        relief="flat")
        style.map("Custom.Treeview.Heading",
                    background=[('active', '#6940c9')])
        self.TABLE1 = tk.ttk.Treeview(self.SCROLLABLE_FRAME1, style="Custom.Treeview", selectmode='browse')
        self.TABLE1['columns'] = ('IPFS Hash', 'File Name')
        self.TABLE1.column('#0', width=0, stretch=tk.NO)
        self.TABLE1.column('IPFS Hash', anchor=tk.CENTER, width=200)
        self.TABLE1.column('File Name', anchor=tk.CENTER, width=200)
        self.TABLE1.heading('#0', text='', anchor=tk.CENTER)
        self.TABLE1.heading('IPFS Hash', text='IPFS Hash', anchor=tk.CENTER)
        self.TABLE1.heading('File Name', text='File Name', anchor=tk.CENTER)
        self.TABLE1.pack(pady=10, padx=20, fill="both", expand=True)
        self.FRAME3 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME3.pack(pady=10, fill="x")
        self.BUTTON2 = ctk.CTkButton(master=self.FRAME3, text="Download Selected", 
               fg_color="#4CAF50", hover_color="#45a049", 
               command=lambda: self.download_file(self.get_selected_row()),
               state="disabled", text_color=("gray10", "#000000"))
        self.BUTTON2.pack(side="left", padx=5, expand=True)
        self.BUTTON3 = ctk.CTkButton(master=self.FRAME3, text="Delete Selected", 
             fg_color="#ff4444", hover_color="#cc0000", 
             command=lambda: self.delete_file(self.get_selected_row()),
             state="disabled", text_color=("gray10", "#000000"))
        self.BUTTON3.pack(side="left", padx=5, expand=True)
        self.TABLE1.bind('<<TreeviewSelect>>', self.on_table_click)
    
        ########## Patient's Medical Records ##########
        self.patient_records = self.tabview.add("Patient's Medical Records")
        self.FRAME4 = ctk.CTkFrame(master=self.patient_records, fg_color="transparent")
        self.FRAME4.pack_propagate(False)
        self.FRAME4.pack(pady=(20, 20), padx=(40, 40), expand=1, fill="both")
        self.LABEL17 = ctk.CTkLabel(master=self.FRAME4, text="Patient's Medical Records", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=42, weight="bold"))
        self.LABEL17.pack(pady=(0, 30))
        self.FRAME5 = ctk.CTkFrame(master=self.FRAME4, fg_color="transparent")
        self.FRAME5.pack(fill="x", padx=20)
        self.FRAME5.grid_columnconfigure(0, weight=3)  # Entry takes 3/4 of space
        self.FRAME5.grid_columnconfigure(1, weight=1)  # Button takes 1/4 of space
        self.ENTRY1 = ctk.CTkEntry(master=self.FRAME5, placeholder_text="Enter Patient's Address")
        self.ENTRY1.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.BUTTON4 = ctk.CTkButton(master=self.FRAME5, text="Search Records", 
                         fg_color="#8651ff", hover_color="#6940c9",
                         command=self.get_patient_records)
        self.BUTTON4.grid(row=0, column=1, sticky="ew")

        self.SCROLLABLE_FRAME2 = ctk.CTkScrollableFrame(master=self.FRAME4)
        self.SCROLLABLE_FRAME2.pack(pady=10, padx=20, fill="both", expand=True)

        self.TABLE2 = tk.ttk.Treeview(self.SCROLLABLE_FRAME2, style="Custom.Treeview", selectmode='browse')
        self.TABLE2['columns'] = ('IPFS Hash', 'File Name')
        self.TABLE2.column('#0', width=0, stretch=tk.NO)
        self.TABLE2.column('IPFS Hash', anchor=tk.CENTER, width=200)
        self.TABLE2.column('File Name', anchor=tk.CENTER, width=200)
        self.TABLE2.heading('#0', text='', anchor=tk.CENTER)
        self.TABLE2.heading('IPFS Hash', text='IPFS Hash', anchor=tk.CENTER)
        self.TABLE2.heading('File Name', text='File Name', anchor=tk.CENTER)
        self.TABLE2.pack(pady=10, padx=20, fill="both", expand=True)

        self.FRAME6 = ctk.CTkFrame(master=self.FRAME4, fg_color="transparent")
        self.FRAME6.pack(pady=10, fill="x")
        self.BUTTON5 = ctk.CTkButton(master=self.FRAME6, text="Download Selected", 
                                            fg_color="#4CAF50", hover_color="#45a049",
                                            state="disabled", text_color=("gray10", "#000000"),
                                            command=lambda: self.download_file(self.get_patient_selected_row()))
        self.BUTTON5.pack(side="left", padx=5, expand=True)
        self.BUTTON6 = ctk.CTkButton(master=self.FRAME6, text="Upload File", 
                                         fg_color="#8651ff", hover_color="#6940c9",
                                         text_color=("gray10", "#000000"),
                                         command=self.upload_file_to_patient)
        self.BUTTON6.pack(side="left", padx=5, expand=True)
        self.TABLE2.bind('<<TreeviewSelect>>', self.on_patient_table_click)
    
        self.web3 = self.controller.web3
        self.doctor_contract = self.controller.doctor_contract
        self.audit_contract = self.controller.audit_contract
    
    def on_table_click(self, event):
        selected_items = self.TABLE1.selection()
        if selected_items:
            self.BUTTON3.configure(state="normal")
            self.BUTTON2.configure(state="normal")
        else:
            self.BUTTON3.configure(state="disabled") 
            self.BUTTON2.configure(state="disabled")
    
    def get_selected_row(self):
        selected_items = self.TABLE1.selection()
        if not selected_items:
            return None
        item = selected_items[0]
        return self.TABLE1.item(item)['values']
    
    def on_patient_table_click(self, event):
        selected_items = self.TABLE2.selection()
        if selected_items:
            self.BUTTON5.configure(state="normal")
        else:
            self.BUTTON5.configure(state="disabled")
    
    def get_patient_selected_row(self):
        selected_items = self.TABLE2.selection()
        if not selected_items:
            return None
        item = selected_items[0]
        return self.TABLE2.item(item)['values']
    
    def update_doctor_frame(self):
        try:
            name, dob, phone, gender, speciality, license_number = self.doctor_contract.functions.getDoctorInfo(self.web3.account).call({'from': self.web3.account})
            medical_files = self.doctor_contract.functions.getDoctorMedicalFiles().call({'from': self.web3.account})
            for item in self.TABLE1.get_children():
                self.TABLE1.delete(item)
            for item in self.TABLE2.get_children():
                self.TABLE2.delete(item)
            for file in medical_files:
                if file[0] == "" or file[1] == "":
                    continue
                self.TABLE1.insert('', 'end', values=(file[0], file[1]))
            self.LABEL3.configure(text=self.web3.account)
            self.LABEL5.configure(text=name)
            self.LABEL7.configure(text=dob)
            self.LABEL9.configure(text=phone)
            self.LABEL11.configure(text=gender)
            self.LABEL13.configure(text=speciality)
            self.LABEL15.configure(text=license_number)
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            print(e)
            return
    
    def get_patient_records(self):
        patient_address = self.ENTRY1.get()
        if not self.web3.is_address(patient_address):
            tk.messagebox.showerror('Error', "Invalid address. Please enter a valid Ethereum address.")
            return
        try:
            patient_address = self.web3.to_checksum_address(patient_address.lower())
            medical_files = self.doctor_contract.functions.getPatientMedicalFiles(patient_address).call({'from': self.web3.account})
            for item in self.TABLE2.get_children():
                self.TABLE2.delete(item)
            for file in medical_files:
                if file[0] == "" or file[1] == "":
                    continue
                self.TABLE2.insert('', 'end', values=(file[0], file[1]))
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
    
    
    def download_file(self, row):
        try:
            file_content = self.controller.ipfs_client.cat(row[0])
            file_path = os.path.join(ctk.filedialog.askdirectory(), row[1])
            with open(file_path, 'wb') as f:
                f.write(file_content)
            tk.messagebox.showinfo('Success', f"File downloaded successfully to: {file_path}")
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
    
    def delete_file(self, row):
        try:
            self.doctor_contract.functions.deleteOwnMedicalFile(row[0]).transact({'from': self.web3.account})
            self.TABLE1.delete(self.TABLE1.selection())
            self.controller.ipfs_client.pin.rm(row[0])
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
        
    def upload_file_to_patient(self):
        file_path = ctk.filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            try:
                with open(file_path, 'rb') as f:
                    file_content = f.read()#
                file_name = os.path.basename(file_path)
                patient_address = self.ENTRY1.get()
                if not self.web3.is_address(patient_address):
                    tk.messagebox.showerror('Error', "Invalid address. Please enter a valid Ethereum address.")#
                    return
                if patient_address == self.web3.account:
                    tk.messagebox.showerror('Error', "You cannot upload files to your own account.")
                    return
                if patient_address == "":
                    tk.messagebox.showerror('Error', "Please enter the patient's address.")
                    return
                patient_address = self.web3.to_checksum_address(patient_address.lower())
                ipfs_hash = self.controller.ipfs_client.add_bytes(file_content)
                tx_hash = self.doctor_contract.functions.uploadMedicalFile(patient_address, ipfs_hash, file_name).transact({'from': self.web3.account})
                receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
                if receipt['status'] == 0:
                    tk.messagebox.showerror('Error', "Transaction failed. Please try again.")
                    return
                tx_hash = self.audit_contract.functions.logDoctorMedicalFileUpload(self.web3.account, patient_address).transact({'from': self.web3.account})
                receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
                self.TABLE1.insert('', 'end', values=(ipfs_hash, file_name))
                self.TABLE2.insert('', 'end', values=(ipfs_hash, file_name))
                tk.messagebox.showinfo('Success', 'File uploaded successfully')
            except Exception as e:
                tk.messagebox.showerror('Python Error', str(e))
                return
            
        else:
            tk.messagebox.showerror('Error', "Please select a file to upload.")
            return