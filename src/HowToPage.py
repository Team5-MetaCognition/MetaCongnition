import tkinter as tk
from BaseImage import BaseImage
import customtkinter as ctk

class HowToPage(BaseImage):  
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 컨트롤러는 주 창(App 클래스)
        self.set_background("src/assets/how_to_test.png")
        
        self.start_test_btn = ctk.CTkButton(self, text="테스트 시작", command=self.start,width=150, height=50, fg_color="#fae375", hover_color="#b09307",text_color="#000000", font=("나눔고딕", 14, "bold"))
        self.start_test_btn.place(x=650, y=750)

    def start(self):
        self.controller.switch_frame("UserInfo") #사용자정보입력 페이지로 넘어가기