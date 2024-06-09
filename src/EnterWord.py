import tkinter as tk

class EnterWord(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
    
    def timer(self):
        self.second = 0