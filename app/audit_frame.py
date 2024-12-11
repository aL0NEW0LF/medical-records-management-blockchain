import tkinter as tk
import customtkinter as ctk
from web3 import Web3
import json
from datetime import datetime

# Connect to the local Ethereum node using Web3
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))  # Replace with your provider URL

# Load ABI from the contract JSON file
try:
    with open('artifacts/contracts/AuditInterface.sol/AuditInterface.json', 'r') as f:
        contract_json = json.load(f)
        abi = contract_json['abi']  # Extract the ABI from the JSON
except FileNotFoundError as fnf_error:
    print(f"Error loading contract ABI: {fnf_error}")
    exit(1)
except json.JSONDecodeError as json_error:
    print(f"Error decoding contract ABI: {json_error}")
    exit(1)

contract_address = "0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9"  # Replace with your deployed contract address

# Set up the contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

class auditFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent, fg_color='transparent', corner_radius=20)
        
        self.current_frame = None  # Store the current active frame
        
        self.add_doctor_frame()  # Set default to doctor registration frame

        # Button to switch to Add Doctor Frame
        self.add_doctor_button = ctk.CTkButton(self, text="Add Doctor", command=self.add_doctor_frame)
        self.add_doctor_button.place(relx=0.05, rely=0.02)

        # Button to switch to Add Patient Frame
        self.add_patient_button = ctk.CTkButton(self, text="Add Patient", command=self.add_patient_frame)
        self.add_patient_button.place(relx=0.25, rely=0.02)

    def add_doctor_frame(self):
        """Show the frame for adding a doctor"""
        self.clear_frame()
        
        self.tts_label = ctk.CTkLabel(self, font=('Arial', 30), text="Doctor Registration")
        self.tts_label.place(anchor="center", relx=0.5, rely=0.07)

        # First Name Field
        self.name_label = ctk.CTkLabel(self, font=('Arial', 17), text="First Name: ")
        self.name_label.place(anchor="center", relx=0.177, rely=0.2)
        self.name_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="First Name")
        self.name_entry.place(relx=0.35, rely=0.21, anchor="center")

        # Last Name Field
        self.dob_label = ctk.CTkLabel(self, font=('Arial', 17), text="Last Name: ")
        self.dob_label.place(anchor="center", relx=0.177, rely=0.3)
        self.dob_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="Last Name")
        self.dob_entry.place(relx=0.35, rely=0.31, anchor="center")

        # Specialty Field
        self.specialty_label = ctk.CTkLabel(self, font=('Arial', 17), text="Specialty: ")
        self.specialty_label.place(anchor="center", relx=0.177, rely=0.4)
        self.specialty_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="Specialty")
        self.specialty_entry.place(relx=0.35, rely=0.41, anchor="center")

        # Experience Field
        self.experience_label = ctk.CTkLabel(self, font=('Arial', 17), text="Experience (years): ")
        self.experience_label.place(anchor="center", relx=0.177, rely=0.5)
        self.experience_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="Experience")
        self.experience_entry.place(relx=0.35, rely=0.51, anchor="center")

        # Submit Button
        self.submit_button = ctk.CTkButton(self, text="Add Doctor", command=self.add_doctor)
        self.submit_button.place(relx=0.35, rely=0.6, anchor="center")

    def add_patient_frame(self):
        """Show the frame for adding a patient"""
        self.clear_frame()
        
        self.tts_label = ctk.CTkLabel(self, font=('Arial', 30), text="Patient Registration")
        self.tts_label.place(anchor="center", relx=0.5, rely=0.07)

        # First Name Field
        self.name_label = ctk.CTkLabel(self, font=('Arial', 17), text="First Name: ")
        self.name_label.place(anchor="center", relx=0.177, rely=0.2)
        self.name_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="First Name")
        self.name_entry.place(relx=0.35, rely=0.21, anchor="center")

        # Last Name Field
        self.dob_label = ctk.CTkLabel(self, font=('Arial', 17), text="Last Name: ")
        self.dob_label.place(anchor="center", relx=0.177, rely=0.3)
        self.dob_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="Last Name")
        self.dob_entry.place(relx=0.35, rely=0.31, anchor="center")

        # Date of Birth Field
        self.dob_label = ctk.CTkLabel(self, font=('Arial', 17), text="Date of Birth: ")
        self.dob_label.place(anchor="center", relx=0.177, rely=0.4)
        self.dob_entry = ctk.CTkEntry(self, width=190, height=30, placeholder_text="YYYY-MM-DD")
        self.dob_entry.place(relx=0.35, rely=0.41, anchor="center")

        # Submit Button
        self.submit_button = ctk.CTkButton(self, text="Add Patient", command=self.add_patient)
        self.submit_button.place(relx=0.35, rely=0.5, anchor="center")

    def add_doctor(self):
        """Handle adding a doctor"""
        first_name = self.name_entry.get()
        last_name = self.dob_entry.get()
        specialty = self.specialty_entry.get()
        experience = self.experience_entry.get()

        try:
            # Web3 Transaction to call the contract method for adding a doctor
            tx_hash = contract.functions.createDoctor(first_name, last_name, specialty, int(experience)).transact({
                'from': w3.eth.accounts[0]  # Set the correct account address
            })
            w3.eth.waitForTransactionReceipt(tx_hash)
            print("Doctor added successfully!")
        except Exception as e:
            print(f"Error adding doctor: {e}")

    def add_patient(self):
        """Handle adding a patient"""
        first_name = self.name_entry.get()
        last_name = self.dob_entry.get()
        dob = self.dob_entry.get()

        # Convert the date of birth to a timestamp (uint256)
        try:
            dob_timestamp = int(datetime.strptime(dob, '%Y-%m-%d').timestamp())
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

        # Ensure doctor exists before adding patient
        doctor_address = self.get_selected_doctor_address()
        if not doctor_address:
            print("No doctor assigned. Please add a doctor first.")
            return

        try:
            # Web3 Transaction to call the contract method for adding a patient
            tx_hash = contract.functions.createPatient(first_name, last_name, dob_timestamp, doctor_address).transact({
                'from': w3.eth.accounts[0]  # Set the correct account address
            })
            w3.eth.waitForTransactionReceipt(tx_hash)
            print("Patient added successfully!")
        except Exception as e:
            print(f"Error adding patient: {e}")

    def get_selected_doctor_address(self):
        """Get the address of the selected doctor"""
        # For simplicity, assume the address is entered manually or selected from a list
        return "0xDoctorAddress"  # Replace with actual logic to get doctor address

    def clear_frame(self):
        """Clears the current frame"""
        for widget in self.winfo_children():
            widget.place_forget()
