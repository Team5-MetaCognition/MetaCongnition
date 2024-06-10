import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from BaseImage import BaseImage
import customtkinter as ctk

class StartPage(BaseImage):  # tk.Frame을 상속하여 페이지 생성
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 컨트롤러는 주 창(App 클래스)
        self.set_background("src/assets/start.png")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.start_button = ctk.CTkButton(self, text="테스트 시작", font=("나눔고딕", 30, "bold"), command=self.start_test, width=230, height=80, fg_color="#fae375", hover_color="#b09307",text_color="#000000")
        self.start_button.grid(row=4, column=1, sticky="wn")
        
        self.method_button = ctk.CTkButton(self, text="테스트 방법", font=("나눔고딕", 30, "bold"), command=self.go_to_how_to_page, width=230, height=80, fg_color="#fae375", hover_color="#b09307",text_color="#000000")   
        self.method_button.grid(row=4, column=1, sticky="en")

    def start_test(self):
        self.controller.switch_frame("UserInfo")

    def go_to_how_to_page(self):
        self.controller.switch_frame("HowToPage")