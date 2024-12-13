import customtkinter as ctk
import tkinter as tk
from PIL import Image
from web3 import Web3
import dotenv
import random
import json
import os
from eth_account.messages import encode_defunct
from hexbytes import HexBytes
import Register as rg
class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)
            
        self.FRAME0 = ctk.CTkFrame(master=self, fg_color="transparent")
        self.FRAME0.pack_propagate(True)
        self.FRAME0.pack(pady=(5, 5), expand=1, fill="both", padx=(5, 0), side="left")
        medical_icon = r"GUI/Assets/medical-history_881760.png"
        self.LABEL19 = ctk.CTkLabel(master=self.FRAME0, text="", anchor="w", text_color=("gray10", "#FFFFFF"), image=ctk.CTkImage(Image.open(medical_icon), size=(48, 48)), font=ctk.CTkFont(size=15))
        self.LABEL19.pack(pady=(20, 0), fill="x", padx=(20, 0))
        self.LABEL18 = ctk.CTkLabel(master=self.FRAME0, text="Welcome\nBack !", justify="left", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=82))
        self.LABEL18.pack(padx=(30, 0), expand=1, fill="x")
        self.FRAME2_copy = ctk.CTkFrame(master=self)
        self.FRAME2_copy.pack_propagate(False)
        self.FRAME2_copy.pack(pady=(20, 20), expand=1, fill="both", padx=(5, 20), side="left")
        self.FRAME2 = ctk.CTkFrame(master=self.FRAME2_copy, width=565, height=500, fg_color="transparent")
        self.FRAME2.pack(expand=1, padx=50, pady=50)
        self.LABEL3 = ctk.CTkLabel(master=self.FRAME2, text="Login", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=39))
        self.LABEL3.pack(fill="x")
        self.LABEL5_copy = ctk.CTkLabel(master=self.FRAME2, text="Welcome Back! Please login to your account", anchor="w", text_color=("gray10", "#b4b4b4"), wraplength=332, justify="left", font=ctk.CTkFont(size=14))
        self.LABEL5_copy.pack(pady=(10, 10), fill="x")
        self.FRAME5 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME5.pack(pady=(20, 20), fill="x")
        self.LABEL8_copy = ctk.CTkLabel(master=self.FRAME5, text="Account Address", anchor="w", text_color=("gray10", "#FFFFFF"), font=ctk.CTkFont(size=15))
        self.LABEL8_copy.pack(fill="x")
        self.ENTRY9 = ctk.CTkEntry(master=self.FRAME5, placeholder_text="0x"+40*"0", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"), width=222)
        self.ENTRY9.pack(fill="x")
        self.BUTTON16 = ctk.CTkButton(master=self.FRAME2, text="Login", height=35, text_color=("gray98", "#FFFFFF"), fg_color=("#8651ff", "#8651ff"), hover_color=("#6940c9", "#6940c9"), width=500, corner_radius=3, command=self.login)
        self.BUTTON16.pack(fill="x")
        self.FRAME17 = ctk.CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME17.pack(pady=(10, 0), fill="x")
        self.LABEL18 = ctk.CTkLabel(master=self.FRAME17, text="New User?", text_color=("gray10", "#FFFFFF"))
        self.LABEL18.pack(side="left")
        self.BUTTON19 = ctk.CTkButton(master=self.FRAME17, text="Sign Up", width=70, fg_color="transparent", hover=False, height=0, text_color=("#000000", "#FFFFFF"), command=lambda:self.controller.show_main_frame(rg.RegisterFrame))
        self.BUTTON19.pack(side="left")
    
    def login(self):
        address = self.ENTRY9.get()
        nonce = random.randint(1000000, 99999999999)
        message = f"Login with nonce: {nonce}"
        signable_message = encode_defunct(text=message)
        dialog = ctk.CTkInputDialog(text=f"Please sign this message with your wallet:\n{message}", title="Sign Message", button_text_color=("gray98", "#FFFFFF"), button_fg_color=("#8651ff", "#8651ff"))
        signature = dialog.get_input()
        
        try:
            signature = HexBytes(json.loads(signature)["sig"])
        except json.JSONDecodeError as e:
            tk.messagebox.showerror('Python Error', str(e))
            return
        
        try:
            dotenv.load_dotenv()
            w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
            recovered_address = w3.eth.account.recover_message(signable_message, signature=signature)
            if recovered_address.lower() == address.lower():
                print("Login successful!")
                
            else:
                tk.messagebox.showerror('Python Error', "Login failed. Please try again.")
        except ValueError as e:
            tk.messagebox.showerror('Python Error', str(e))
            return

            
