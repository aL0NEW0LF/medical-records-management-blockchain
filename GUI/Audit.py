import customtkinter as ctk
import tkinter as tk
import os
import Login as lg
import datetime

class AuditFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)
        self.tabview = ctk.CTkTabview(master=self, segmented_button_selected_color=("#8651ff", "#8651ff"), segmented_button_selected_hover_color=("#6940c9", "#6940c9"))
        self.tabview.pack_configure(expand=True, fill="both")
        
        ########## Audit Trail ##########
        self.profile = self.tabview.add("Audit Trail")
        self.FRAME0 = ctk.CTkFrame(master=self.profile, fg_color="transparent")
        self.FRAME0.pack_propagate(False)
        self.FRAME0.pack(pady=(20, 20), padx=(40, 40), expand=1, fill="both")
        self.LABEL1 = ctk.CTkLabel(master=self.FRAME0, text="Audit Trail", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=42, weight="bold"))
        self.LABEL1.pack(pady=(0, 30))
        self.SCROLLABLE_FRAME1 = ctk.CTkScrollableFrame(master=self.FRAME0)
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
        self.TABLE1['columns'] = ('Timestamp', 'Actor Address', 'Event Type', 'Description')
        self.TABLE1.column('#0', width=0, stretch=tk.NO)
        self.TABLE1.column('Timestamp', anchor=tk.CENTER, width=150)
        self.TABLE1.column('Actor Address', anchor=tk.CENTER, width=200)
        self.TABLE1.column('Event Type', anchor=tk.CENTER, width=150)
        self.TABLE1.column('Description', anchor=tk.CENTER, width=300)
        self.TABLE1.heading('#0', text='', anchor=tk.CENTER)
        self.TABLE1.heading('Timestamp', text='Timestamp', anchor=tk.CENTER)
        self.TABLE1.heading('Actor Address', text='Actor Address', anchor=tk.CENTER)
        self.TABLE1.heading('Event Type', text='Event Type', anchor=tk.CENTER)
        self.TABLE1.heading('Description', text='Description', anchor=tk.CENTER)
        self.TABLE1.pack(pady=10, padx=20, fill="both", expand=True)
        self.FRAME1 = ctk.CTkFrame(master=self.FRAME0, fg_color="transparent")
        self.FRAME1.pack(pady=10, fill="x")
        self.BUTTON1 = ctk.CTkButton(master=self.FRAME1, text="Refresh Logs", fg_color="#8651ff", hover_color="#6940c9", command=self.refresh_logs)
        self.BUTTON1.pack(side="left", padx=10, expand=True)
        self.BUTTON2 = ctk.CTkButton(master=self.FRAME1, text="Logout", fg_color="#ff5151", hover_color="#cc4141", command=lambda: self.controller.show_main_frame(lg.LoginFrame))
        self.BUTTON2.pack(side="right", padx=10, expand=True)
        
        ########## Add Auditors / Auditor Table ##########
        self.add_auditors = self.tabview.add("Add Auditors")
        self.FRAME2 = ctk.CTkFrame(master=self.add_auditors, fg_color="transparent")
        self.FRAME2.pack_propagate(False)
        self.FRAME2.pack(pady=(20, 20), padx=(40, 40), expand=1, fill="both")
        self.LABEL2 = ctk.CTkLabel(master=self.FRAME2, text="Add Auditors", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=42, weight="bold"))
        self.LABEL2.pack(pady=(0, 30))
        self.FRAME3 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME3.pack(fill="x", padx=20)
        self.FRAME3.grid_columnconfigure(0, weight=3)  # Entry takes 3/4 of space
        self.FRAME3.grid_columnconfigure(1, weight=1)  # Button takes 1/4 of space
        self.ENTRY1 = ctk.CTkEntry(master=self.FRAME3, placeholder_text="0x"+40*"0")
        self.ENTRY1.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.BUTTON3 = ctk.CTkButton(master=self.FRAME3, text="Add Auditor", fg_color="#8651ff", hover_color="#6940c9", command=self.add_auditor)
        self.BUTTON3.grid(row=0, column=1, sticky="ew")
        self.SCROLLABLE_FRAME2 = ctk.CTkScrollableFrame(master=self.FRAME2)
        self.SCROLLABLE_FRAME2.pack(pady=10, padx=20, fill="both", expand=True)
        self.TABLE2 = tk.ttk.Treeview(self.SCROLLABLE_FRAME2, style="Custom.Treeview", selectmode='browse')
        self.TABLE2['columns'] = ('Address',)
        self.TABLE2.column('#0', width=0, stretch=tk.NO)
        self.TABLE2.column('Address', anchor=tk.CENTER, width=400)
        self.TABLE2.heading('#0', text='', anchor=tk.CENTER)
        self.TABLE2.heading('Address', text='Auditor Address', anchor=tk.CENTER)
        self.TABLE2.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.web3 = self.controller.web3
        self.audit_contract = self.controller.audit_contract
        
    def refresh_logs(self):
        try:
            logs = self.audit_contract.functions.getFullAuditTrail().call({'from': self.web3.account})
            self.TABLE1.delete(*self.TABLE1.get_children())
            for log in logs:
                date = datetime.datetime.fromtimestamp(log[0]).strftime('%Y-%m-%d %H:%M:%S')
                self.TABLE1.insert("", "end", values=(date, log[1], log[2], log[3]))
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
        
    def refresh_auditors(self):
        try:
            auditors = self.audit_contract.functions.getAuditors().call({'from': self.web3.account})
            self.TABLE2.delete(*self.TABLE2.get_children())
            for auditor in auditors:
                self.TABLE2.insert("", "end", values=(auditor))
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
        
    def add_auditor(self):
        address = self.ENTRY1.get()
        if not self.web3.is_address(address):
            tk.messagebox.showerror('Error', "Invalid address. Please enter a valid Ethereum address.")
            return
        try:
            address = self.web3.to_checksum_address(address)
            tx_hash = self.audit_contract.functions.addAuditor(address).transact({'from': self.web3.account})
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status == 0:
                tk.messagebox.showerror('Error', "Transaction failed.")
                return
            self.refresh_auditors()
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
