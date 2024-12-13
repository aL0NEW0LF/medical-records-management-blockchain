import platform
import ctypes
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
import Login as lg
import Register as rg

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.myappid = 'heh' # arbitrary string
        self.title("Medical Records Management")
        self.geometry("1000x600")
        self.configure(fg_color=['gray92', 'gray14'])
        
        container = ctk.CTkFrame(self)
        container.configure(fg_color=['gray92', 'gray14'])
        container.pack(side="top", expand=True, fill="both")
        
        self.frames = {}
        
        for F in [lg.LoginFrame, rg.RegisterFrame]:
            frame = F(container, self)
            self.frames[F] = frame
            frame.pack(fill="both", expand=True)
            frame.pack_forget()
        
        # Show the login frame initially
        self.frames[lg.LoginFrame].pack(fill="both", expand=True)
    
    def show_main_frame(self, cont):
        current_frame = self.frames[cont]
        current_frame.configure(fg_color="#101010")
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        # Show the current frame
        current_frame.pack(fill="both", expand=True)


    def show_frame(self, frame, main):
        frames = {
            "LoginFrame": self.frames[lg.LoginFrame],
            "RegisterFrame": self.frames[rg.RegisterFrame]
        }
        self.show_main_frame(main)
        frame_to_show = frames.get(frame)
        if frame_to_show is None:
            return
        
    def login_patient(self):
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
       
ctk.set_default_color_theme("green")
app = App()
app.protocol("WM_DELETE_WINDOW", app.quit)
app.mainloop()
