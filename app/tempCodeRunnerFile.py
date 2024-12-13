def show_main_frame(self, cont):
        """
        Shows the main frame.

        Args:
            cont: The frame to show.
        """
        current_frame = self.frames[cont]
        current_frame.configure(fg_color="#101010")
        current_frame.tkraise()