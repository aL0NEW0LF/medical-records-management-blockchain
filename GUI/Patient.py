import customtkinter as ctk
import tkinter as tk
import os
import Login as lg
import re

class PatientFrame(ctk.CTkFrame):
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
        self.LABEL1 = ctk.CTkLabel(master=self.FRAME0, text="Profile", anchor="n", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=42, weight="bold"))
        self.LABEL1.pack(pady=(0, 30))
        self.FRAME1 = ctk.CTkFrame(master=self.FRAME0, fg_color="transparent")
        self.FRAME1.pack(pady=10, fill="x")
        self.LABEL2 = ctk.CTkLabel(master=self.FRAME1, text="Logged in as:", anchor="center", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL2.pack(fill="x")
        self.LABEL3 = ctk.CTkLabel(master=self.FRAME1, text="0x"+40*"0", anchor="center", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL3.pack(fill="x")
        self.FRAME2 = ctk.CTkFrame(master=self.FRAME0, fg_color="transparent")
        self.FRAME2.pack(pady=10, fill="x")
        self.LABEL4 = ctk.CTkLabel(master=self.FRAME2, text="Name:", anchor="center", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL4.pack(fill="x")
        self.LABEL41 = ctk.CTkLabel(master=self.FRAME2, text="John Doe", anchor="center", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL41.pack(fill="x")
        self.FRAME3 = ctk.CTkFrame(master=self.FRAME0, fg_color="transparent")
        self.FRAME3.pack(pady=10, fill="x")
        self.LABEL5 = ctk.CTkLabel(master=self.FRAME3, text="Date of Birth:", anchor="center", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL5.pack(fill="x")
        self.LABEL51 = ctk.CTkLabel(master=self.FRAME3, text="01/01/2000", anchor="center", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL51.pack(fill="x")
        self.FRAME4 = ctk.CTkFrame(master=self.FRAME0, fg_color="transparent")
        self.FRAME4.pack(pady=10, fill="x")
        self.LABEL6 = ctk.CTkLabel(master=self.FRAME4, text="Phone Number:", anchor="center", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL6.pack(fill="x")
        self.LABEL61 = ctk.CTkLabel(master=self.FRAME4, text="0123456789", anchor="center", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL61.pack(fill="x")
        self.FRAME5 = ctk.CTkFrame(master=self.FRAME0, fg_color="transparent")
        self.FRAME5.pack(pady=10, fill="x")
        self.LABEL62 = ctk.CTkLabel(master=self.FRAME5, text="Gender:", anchor="center", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=16, weight="bold"))
        self.LABEL62.pack(fill="x")
        self.LABEL621 = ctk.CTkLabel(master=self.FRAME5, text="Male/Female", anchor="center", text_color=("gray40", "#AAAAAA"), font=ctk.CTkFont(size=15))
        self.LABEL621.pack(fill="x")
        self.BUTTON1 = ctk.CTkButton(master=self.FRAME0,text="Logout",fg_color="#8651ff",hover_color="#6940c9",command=lambda: self.controller.show_main_frame(lg.LoginFrame))
        self.BUTTON1.pack(pady=(20, 0))
        
        ########## Grant/Revoke Access ##########
        self.grant_revoke = self.tabview.add("Grant/Revoke Access")
        self.FRAME6 = ctk.CTkFrame(master=self.grant_revoke, fg_color="transparent")
        self.FRAME6.pack_propagate(False)
        self.FRAME6.pack(pady=(20, 20), padx=(40, 40), expand=1, fill="both")
        self.LABEL7 = ctk.CTkLabel(master=self.FRAME6, text="Grant/Revoke Access", anchor="n", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=42, weight="bold"))
        self.LABEL7.pack(pady=(0, 30))
        
        self.grant_frame = ctk.CTkFrame(master=self.FRAME6, fg_color="transparent")
        self.grant_frame.pack(side="left", padx=20, expand=True, fill="both")
        self.grant_label = ctk.CTkLabel(master=self.grant_frame, text="Grant Access", font=ctk.CTkFont(size=20, weight="bold"))
        self.grant_label.pack(pady=10, anchor="center")
        self.grant_entry = ctk.CTkEntry(master=self.grant_frame, placeholder_text="Doctor's Address")
        self.grant_entry.pack(pady=10, fill="x", padx=20)
        self.grant_button = ctk.CTkButton(master=self.grant_frame, text="Grant Access", fg_color="#8651ff", hover_color="#6940c9")
        self.grant_button.pack(pady=10, anchor="center")

        self.revoke_frame = ctk.CTkFrame(master=self.FRAME6, fg_color="transparent")
        self.revoke_frame.pack(side="right", padx=20, expand=True, fill="both")
        self.revoke_label = ctk.CTkLabel(master=self.revoke_frame, text="Revoke Access", font=ctk.CTkFont(size=20, weight="bold"))
        self.revoke_label.pack(pady=10, anchor="center")
        self.revoke_entry = ctk.CTkEntry(master=self.revoke_frame, placeholder_text="Doctor's Address")
        self.revoke_entry.pack(pady=10, fill="x", padx=20)
        self.revoke_button = ctk.CTkButton(master=self.revoke_frame, text="Revoke Access", fg_color="#8651ff", hover_color="#6940c9")
        self.revoke_button.pack(pady=10, anchor="center")
        
        ########## Medical Records ##########
        
        self.medical_records = self.tabview.add("Medical Records")
        self.FRAME7 = ctk.CTkFrame(master=self.medical_records, fg_color="transparent")
        self.FRAME7.pack_propagate(False)
        self.FRAME7.pack(pady=(20, 20), padx=(40, 40), expand=1, fill="both")
        self.LABEL8 = ctk.CTkLabel(master=self.FRAME7, text="Medical Records", anchor="n", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=42, weight="bold"))
        self.LABEL8.pack(pady=(0, 30))
        
        self.SCROLLABLE_FRAME1 = ctk.CTkScrollableFrame(master=self.FRAME7)
        self.SCROLLABLE_FRAME1.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Create Treeview
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

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading",
                    background=[('active', '#3484F0')])
        
        self.TABLE1 = tk.ttk.Treeview(self.SCROLLABLE_FRAME1, style="Custom.Treeview", selectmode='browse')
        self.TABLE1['columns'] = ('IPFS Hash', 'File Name')
        
        # Configure columns
        self.TABLE1.column('#0', width=0, stretch=tk.NO)
        self.TABLE1.column('IPFS Hash', anchor=tk.CENTER, width=200)
        self.TABLE1.column('File Name', anchor=tk.CENTER, width=200)
        
        # Configure headers
        self.TABLE1.heading('#0', text='', anchor=tk.CENTER)
        self.TABLE1.heading('IPFS Hash', text='IPFS Hash', anchor=tk.CENTER)
        self.TABLE1.heading('File Name', text='File Name', anchor=tk.CENTER)
        
        self.TABLE1.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.button_frame = ctk.CTkFrame(master=self.FRAME7, fg_color="transparent")
        self.button_frame.pack(pady=10, fill="x")
        
        self.delete_button = ctk.CTkButton(master=self.button_frame, text="Delete Selected", 
             fg_color="#8651ff", hover_color="#6940c9", 
             command=lambda: self.delete_file(self.get_selected_row()),
             state="disabled")
        self.delete_button.pack(side="left", padx=5, expand=True)
        
        self.download_button = ctk.CTkButton(master=self.button_frame, text="Download Selected", 
               fg_color="#8651ff", hover_color="#6940c9", 
               command=lambda: self.download_file(self.get_selected_row()),
               state="disabled")
        self.download_button.pack(side="left", padx=5, expand=True)
        
        self.BUTTON2 = ctk.CTkButton(master=self.FRAME7, text="Upload File to IPFS", 
            fg_color="#8651ff", hover_color="#6940c9", 
            command=self.upload_file)
        self.BUTTON2.pack(pady=10, anchor="center")
        
        self.TABLE1.bind('<<TreeviewSelect>>', self.on_table_click)
        self.web3 = self.controller.web3
        self.patient_contract = self.controller.patient_contract
        
    def on_table_click(self, event):
        selected_items = self.TABLE1.selection()
        if selected_items:
            self.delete_button.configure(state="normal")
            self.download_button.configure(state="normal")
        else:
            self.delete_button.configure(state="disabled") 
            self.download_button.configure(state="disabled")

    def get_selected_row(self):
        selected_items = self.TABLE1.selection()
        if not selected_items:
            return None
        item = selected_items[0]
        return self.TABLE1.item(item)['values']
    
    def delete_file(self, row):
        try:
            self.patient_contract.functions.deleteMedicalFile(row[1]).transact({'from': self.web3.account})
            self.TABLE1.delete(self.TABLE1.selection())
            self.controller.ipfs_client.pin.rm(row[1])
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
        
    def download_file(self, row):
        try:
            file_content = self.controller.ipfs_client.cat(row[1])
            file_path = os.path.join(ctk.filedialog.askdirectory(), row[0])
            with open(file_path, 'wb') as f:
                f.write(file_content)
            tk.messagebox.showinfo('Success', f"File downloaded successfully to: {file_path}")
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
    
    def upload_file(self):
        file_path = ctk.filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            try:
                with open(file_path, 'rb') as file:
                    file_content = file.read()
                    response = self.controller.ipfs_client.add_bytes(file_content)
                    ipfs_hash = response
                    tx_hash = self.patient_contract.functions.addMedicalFile(file_name, ipfs_hash).transact({'from': self.web3.account})
                    self.web3.eth.wait_for_transaction_receipt(tx_hash)
                    self.TABLE1.insert('', 'end', values=(file_name, ipfs_hash))
                    
            except Exception as e:
                tk.messagebox.showerror('Python Error', str(e))
                return
            
    def update_patient_frame(self):
        try:
            name, dob, phone, gender = self.controller.patient_contract.functions.getPatientInfo().call({'from': self.web3.account})
            medical_files = self.controller.patient_contract.functions.getOwnMedicalFiles().call({'from': self.web3.account})
            for item in self.TABLE1.get_children():
                self.TABLE1.delete(item)
            for file in medical_files:
                if file[0] == "" or file[1] == "":
                    continue
                self.TABLE1.insert('', 'end', values=(file[0], file[1]))
            self.LABEL41.configure(text=name)
            self.LABEL51.configure(text=dob) 
            self.LABEL61.configure(text=phone)
            self.LABEL621.configure(text=gender)
            self.LABEL3.configure(text=self.web3.account)
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            print(e)
            return