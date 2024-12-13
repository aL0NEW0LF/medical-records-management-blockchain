import tkinter as tk
import customtkinter as ctk
from web3 import Web3
import json
from datetime import datetime

# Connect to the local Ethereum node using Web3
# w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))  # Replace with your provider URL

# # Load ABI from the contract JSON file
# try:
#     with open('artifacts/contracts/AuditInterface.sol/AuditInterface.json', 'r') as f:
#         contract_json = json.load(f)
#         abi = contract_json['abi']  # Extract the ABI from the JSON
# except FileNotFoundError as fnf_error:
#     print(f"Error loading contract ABI: {fnf_error}")
#     exit(1)
# except json.JSONDecodeError as json_error:
#     print(f"Error decoding contract ABI: {json_error}")
#     exit(1)

# contract_address = "0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9"  # Replace with your deployed contract address

# # Set up the contract instance
# contract = w3.eth.contract(address=contract_address, abi=abi)

class auditFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent, fg_color='transparent', corner_radius=20)
        
        self.tts_label = ctk.CTkLabel(self, font=('Arial', 30), text="Hamid")
        self.tts_label.place(anchor="center", relx=0.5, rely=0.2)

        

      
    