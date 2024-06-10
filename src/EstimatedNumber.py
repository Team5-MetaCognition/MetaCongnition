import tkinter as tk
from tkinter import messagebox
from EnterWord import EnterWord
from ReportScreen import ReportScreen
from BaseImage import BaseImage
import customtkinter as ctk

class EstimatedNumber(BaseImage):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.set_background("src/assets/EstimatedNumber_bg.png")
        
        # # "메타인지 테스트" 타이틀 라벨
        # self.title_label = tk.Label(self, text="메타인지 테스트", font=("Helvetica", 48))
        # self.title_label.place(x=400, y=100)

        # # 예상 개수 입력 라벨
        # self.input_label = tk.Label(self, text="예상 개수를 입력하세요:",font=("Helvetica", 24))
        # self.input_label.place(x=200, y=500)

        # 예상 개수 입력 칸
        self.entry = tk.Entry(self, width=30,font=("나눔고딕", 24))
        self.entry.place(x=480, y=500)

        # 확인 버튼
        self.confirm_button = ctk.CTkButton(self, text="확인", command=self.confirm_input, font=("나눔고딕", 24, "bold"), width=150, height=50, fg_color="#fae375", hover_color="#b09307",text_color="#000000")
        self.confirm_button.place(x=650, y=600)

    def confirm_input(self):
        try:
            # 예상 개수를 가져와 정수로 변환
            estimated_number = int(self.entry.get())
            self.controller.user.set_estimated_number(estimated_number)
            self.controller.switch_frame("EnterWord")
            
        except ValueError:
            # 숫자가 아닌 값이 입력된 경우 오류 메시지 표시
            messagebox.showerror("오류", "유효한 숫자를 입력하세요.")