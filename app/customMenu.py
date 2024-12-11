import customtkinter as ctk
import tkinter as tk
from typing import Literal


class Menu:
    """
    Custom Menu Class.
    When initializing the menu, make sure there's upper window space for the menu bar,
    menu is packed like so: `pack(side="top", fill="x")`
    """

    def __init__(self, root: ctk.CTk) -> None:
        self._root = root
        self._menu_bar = ctk.CTkFrame(self._root, cursor="hand2")
        self._menu_bar.pack(side="top", fill="x")
        self._menu_widgets: list[tk.Widget] = []  # Updated to include buttons, not just Menubuttons
        ctk.AppearanceModeTracker.add(self.set_appearance_mode)

    def menu_bar(self, text: str, **kwargs) -> tk.Menu:
        """
        Creates a dropdown menu on the menu bar.
        """
        menu = tk.Menubutton(self._menu_bar, text=text, font=('Arial', 13))
        menu.menu = tk.Menu(menu, **kwargs, font=('Arial', 13))
        menu["menu"] = menu.menu
        menu.pack(side="left")
        self._menu_widgets.append(menu)
        self.set_appearance_mode()
        return menu.menu

    def menu_button(self, text: str, command=None, **kwargs) -> tk.Menubutton:
        """
        Creates a button on the menu bar styled like a menu button.
        """
        button = tk.Menubutton(self._menu_bar, text=text, font=('Arial', 13), cursor="hand2", relief="flat", **kwargs)
        button.configure(activebackground="darkgray", activeforeground="white", bd=0)
        button.bind("<Button-1>", lambda e: command() if command else None)  # Simulate button click
        button.pack(side="left", padx=5, pady=2)
        self._menu_widgets.append(button)
        self.set_appearance_mode(theme_mode=None)  # Apply appearance settings
        return button


    def set_appearance_mode(self, theme_mode: Literal["Light", "Dark"] = None):
        """
        Updates the appearance of menu widgets based on the theme mode.
        """
        theme = (
            "#252526"
            if (theme_mode or ctk.get_appearance_mode()) == "Dark"
            else "#E9E9E9"
        )
        text_color = "white" if theme == "#252526" else "black"

        self._menu_bar.configure(fg_color=theme)
        for widget in self._menu_widgets:
            widget.configure(
                bg=theme,
                fg=text_color,
                activebackground="darkgray" if theme == "#252526" else "lightgray",
                activeforeground=text_color,
            )
            