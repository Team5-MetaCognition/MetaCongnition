import tkinter as tk
# from tkinter import PhotoImage
# from PIL import Image, ImageTk
# from StartPage import StartPage
from BaseImage import BaseImage

class HowToPage(BaseImage):  
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 컨트롤러는 주 창(App 클래스)
        self.set_background("src/assets/how_to_test.png")

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_rowconfigure(3, weight=1)
        # self.grid_rowconfigure(4, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)


# "테스트 방법", "1. 화면에 나오는 20개의 단어를 1분간 외운다.\n"
#         "2. 외운단어를 맞추기 전 몇개를 맞출 수 있을지 개수를 적는다.\n"
#         "3. 외운단어를 2분간 적는다.\n"
#         "4. 테스트 전에 몇 개를 맞출지 예상한 개수와 실제 외운 단어 개수를 비교한다.\n"
        self.start_test_btn = tk.Button(self, text="테스트 시작", command=self.backTo,height=3, width=20,font=("나눔고딕", 14))
        self.start_test_btn.place(x=650, y=750)

    def backTo(self):
        self.controller.switch_frame("UserInfo") #사용자정보입력 페이지로 넘어가기