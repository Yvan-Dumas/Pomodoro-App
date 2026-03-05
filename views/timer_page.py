import customtkinter as ctk

class TimerPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="transparent")
        self.timer = ctk.CTkLabel(self, text="00:25")
        self.timer.pack()