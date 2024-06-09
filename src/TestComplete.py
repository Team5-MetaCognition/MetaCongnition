import tkinter as tk
from BaseImage import BaseImage

class TestComplete(BaseImage):  
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 컨트롤러는 주 창(App 클래스)
        self.set_background("src/assets/test_complete_bg.png")

        self.test_complete_btn = tk.Button(self, text="결과 보기", command=self.move_ResultScreen,height=3, width=20,font=("나눔고딕", 14))
        self.test_complete_btn.place(x=650, y=650)

    def move_ResultScreen(self):
        self.controller.switch_frame("ResultScreen") #사용자정보입력 페이지로 넘어가기