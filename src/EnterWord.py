import tkinter as tk
from ResultScreen import ResultScreen
# from Timer import Timer
from BaseImage import BaseImage

class EnterWord(BaseImage):
    second=120

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.set_background("src/assets/main_background-3rd.png")

    
        self.timer_label = tk.Label(self, text="120초 (남은 시간)")
        self.timer_label.pack(expand=True)

        self.input_label = tk.Label(self, text="외운 단어들을 입력하세요")
        self.input_label.pack(expand=True)

        self.entry = tk.Entry(self)
        self.entry.pack(expand=True)
        self.entry.bind("<Return>", self.on_enter)

        self.confirm_button = tk.Button(self, text="완료", command=self.confirm_btn,height=3, width=10,font=("Helvetica", 24))
        self.confirm_button.pack(expand=True)

    def addSecond(self):
        if self.second > 0:
            self.timer_label.config(text=f"{self.second}초 (남은 시간)")
            self.second -= 1
            self.after(1000, self.addSecond)
        else:
            self.controller.switch_frame("TestComplete")

    def start_timer(self):
        self.addSecond()
        
    def on_enter(self, event):
        word = self.entry.get()
        self.controller.user.inputWord(word)
        self.entry.delete(0, tk.END)

    def confirm_btn(self):
        self.controller.switch_frame("TestComplete")