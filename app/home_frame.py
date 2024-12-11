import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk  # For handling images


class homeFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Set the grid layout
        self.grid_columnconfigure(0, weight=1)  # Left side for image
        self.grid_columnconfigure(1, weight=2)  # Right side for paragraph
        self.grid_rowconfigure(0, weight=1)

        # Load and display the image on the left side
        image_path = "image.jpeg"  # Replace with the path to your image
        self.image = Image.open(image_path)
        self.image = self.image.resize((500, 500))  # Resize the image as needed
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = tk.Label(self, image=self.photo, bg="#101010")
        self.image_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Paragraph on the right side
        paragraph_text = (
            "----------------------------Gestion des Dossiers Médicaux avec Blockchain--------------------------\n\n"
            "Cette application utilise la technologie blockchain pour sécuriser les dossiers médicaux des patients. "
            "Grâce à sa nature décentralisée, elle garantit la confidentialité, la traçabilité et l'intégrité des données. "
            "Les contrats intelligents sur Ethereum assurent une gestion fiable et automatisée, tandis que l'interface utilisateur, "
            "développée en Python, offre une expérience intuitive. Ce système répond aux besoins croissants de sécurité et de transparence "
            "dans le domaine de la santé.\n"
             "--------------------------------------------------------------------------------------------------------------------"
        )
        # Label to display text with adjusted font size
        self.text_label = ctk.CTkLabel(
            self,
            text=paragraph_text,
            wraplength=650,  # Adjust the wraplength to allow larger text blocks
            font=("Arial", 16),  # Increase font size
            justify="left",  # Align the text to the left
            anchor="w",  # Left-align text inside the label
            padx=10,  # Add padding around the text
            pady=10,  # Adjust padding around the text for better alignment
        )

        # Adjust the grid and use sticky="nsew" for full expansion
        self.text_label.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Ensure both rows and columns can expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
