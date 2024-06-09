import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox

class StartPage(tk.Frame):  # tk.Frame을 상속하여 페이지 생성
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller  # 컨트롤러는 주 창(App 클래스)

        image = Image.open("src/assets/start.png")
        image = image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
        photo = ImageTk.PhotoImage(image)

        self.background_label = tk.Label(self, image=photo)
        self.background_label.image = photo  # PhotoImage가 가비지 컬렉션에 의해 제거되지 않도록 유지
        self.background_label.place(relwidth=1, relheight=1)  # 프레임 전체에 이미지 채우기

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.start_button = tk.Button(self, text="테스트 시작", font=("Helvetica", 24),command=self.start_ttest)
        self.start_button.grid(row=3, column=1, padx=(10, 20), sticky="w")

        self.method_button = tk.Button(self, text="테스트 방법", font=("Helvetica", 24),command=self.go_to_how_to_page)
        self.method_button.grid(row=3, column=1, padx=(10, 20), sticky="e")

    def start_ttest(self):
        self.controller.switch_frame("UserInfo")

    def go_to_how_to_page(self):
        self.controller.switch_frame("HowToPage")