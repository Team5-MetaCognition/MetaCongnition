import tkinter as tk
from ResultScreen import ResultScreen
from BaseImage import BaseImage
import customtkinter as ctk

class EnterWord(BaseImage):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.set_background("src/assets/EnterWord_bg.png")
        self.second=120
        self.add_second_after = None 
    
        self.timer_label = tk.Label(self, text="120초 (남은 시간)", bg="white", font=("나눔고딕", 18))
        self.timer_label.place(x=670, y=160)

        self.entry = tk.Entry(self, width=15,font=("나눔고딕", 24))
        self.entry.place(x=620, y=480)
        self.entry.bind("<Return>", self.on_enter)

        self.confirm_button = ctk.CTkButton(self, text="모두 입력 완료", command=self.confirm_btn, font=("나눔고딕", 30, "bold"), width=150, height=50, fg_color="#fae375", hover_color="#b09307",text_color="#000000")
        self.confirm_button.place(x=650,y=650)

    def add_second(self):
        if self.second > 0:
            self.timer_label.config(text=f"{self.second}초 (남은 시간)")
            self.second -= 1
            self.add_second_after=self.after(1000, self.add_second)
        else:
            self.after_cancel(self.add_second_after)
            self.controller.switch_frame("TestComplete")

    def start_timer(self):
        self.add_second()
        
    def on_enter(self, event):
        word = self.entry.get()
        self.controller.user.inputWord(word)
        self.entry.delete(0, tk.END)

    def confirm_btn(self):
        self.after_cancel(self.add_second_after)
        self.controller.switch_frame("TestComplete")