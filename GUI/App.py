import platform
import ctypes
import customtkinter as ctk
import tkinter as tk
from web3 import Web3
import dotenv
import os
import Login as lg
import Register as rg
import Patient as pt
import Doctor as dt
import Audit as at
import ipfshttpclient


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.myappid = 'heh' # arbitrary string
        self.title("Medical Records Management")
        self.geometry("1000x600")
        self.configure(fg_color=['gray92', 'gray14'])
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.iconbitmap(os.path.join(current_dir, "Assets", "cardiogram.ico"))
        if platform.system() == "Windows":
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.myappid)
        try:
            dotenv.load_dotenv()
            self.web3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
            self.doctor_contract = self.load_doctor_contract()
            self.patient_contract = self.load_patient_contract()
            self.audit_contract = self.load_audit_contract()
            self.role_contract = self.load_role_contract()
            self.ipfs_client = ipfshttpclient.connect(os.getenv("IPFS_URL"))
        except Exception as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
            
        container = ctk.CTkFrame(self)
        container.configure(fg_color=['gray92', 'gray14'])
        container.pack(side="top", expand=True, fill="both")
        
        self.frames = {}
        
        for F in [lg.LoginFrame, rg.RegisterFrame, pt.PatientFrame, dt.DoctorFrame, at.AuditFrame]:
            frame = F(container, self)
            self.frames[F] = frame
            frame.pack(fill="both", expand=True)
            frame.pack_forget()
        
        # Show the login frame initially
        self.frames[lg.LoginFrame].pack(fill="both", expand=True)
    
    def load_doctor_contract(self):
        contract_abi = os.getenv("DOCTOR_CONTRACT_ABI")
        contract_address = self.web3.to_checksum_address(os.getenv("DOCTOR_CONTRACT_ADDRESS"))
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)
    
    def load_patient_contract(self):
        contract_abi = os.getenv("PATIENT_CONTRACT_ABI")
        contract_address = self.web3.to_checksum_address(os.getenv("PATIENT_CONTRACT_ADDRESS"))
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)
    
    def load_audit_contract(self):
        contract_abi = os.getenv("AUDIT_CONTRACT_ABI")
        contract_address = self.web3.to_checksum_address(os.getenv("AUDIT_CONTRACT_ADDRESS"))
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)
    
    def load_role_contract(self):
        contract_abi = os.getenv("ROLE_CONTRACT_ABI")
        contract_address = self.web3.to_checksum_address(os.getenv("ROLE_CONTRACT_ADDRESS"))
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)
    
    def show_main_frame(self, cont):
        current_frame = self.frames[cont]
        current_frame.configure(fg_color="#101010")
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        # Show the current frame
        current_frame.pack(fill="both", expand=True)
        
ctk.set_default_color_theme("green")
app = App()
app.protocol("WM_DELETE_WINDOW", app.quit)
app.mainloop()
