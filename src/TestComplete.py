import tkinter as tk
from BaseImage import BaseImage
import customtkinter as ctk

class TestComplete(BaseImage):  
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 컨트롤러는 주 창(App 클래스)
        self.set_background("src/assets/test_complete_bg.png")

        self.test_complete_btn = ctk.CTkButton(self, text="결과 보기", command=self.move_ResultScreen,font=("나눔고딕", 15, "bold"), width=150, height=50, fg_color="#fae375", hover_color="#b09307",text_color="#000000")
        self.test_complete_btn.place(x=650, y=650)

    def move_ResultScreen(self):
        self.controller.switch_frame("ResultScreen") #사용자정보입력 페이지로 넘어가기