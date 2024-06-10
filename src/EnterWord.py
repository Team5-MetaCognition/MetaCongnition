import tkinter as tk
from ResultScreen import ResultScreen
# from Timer import Timer
from BaseImage import BaseImage

class EnterWord(BaseImage):
    second=120

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.set_background("src/assets/EnterWord_bg.png")

    
        self.timer_label = tk.Label(self, text="120초 (남은 시간)", bg="white", font=("나눔고딕", 18))
        self.timer_label.place(x=670, y=160)

        # self.input_label = tk.Label(self, text="외운 단어들을 입력하세요")
        # self.input_label.pack(expand=True)

        self.entry = tk.Entry(self, width=15,font=("나눔고딕", 24))
        self.entry.place(x=620, y=480)
        self.entry.bind("<Return>", self.on_enter)

        self.confirm_button = tk.Button(self, text="완료", command=self.confirm_btn,height=3, width=10,font=("나눔고딕", 14))
        self.confirm_button.place(x=670, y=580)

    def add_second(self):
        if self.second > 0:
            self.timer_label.config(text=f"{self.second}초 (남은 시간)")
            self.second -= 1
            self.after(1000, self.add_second)
        else:
            self.destroy()
            self.controller.switch_frame("TestComplete")

    def start_timer(self):
        self.add_second()
        
    def on_enter(self, event):
        word = self.entry.get()
        self.controller.user.inputWord(word)
        self.entry.delete(0, tk.END)

    def confirm_btn(self):
        self.destroy()
        self.controller.switch_frame("TestComplete")
