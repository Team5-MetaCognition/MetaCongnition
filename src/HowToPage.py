import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from StartPage import StartPage

class HowToPage(tk.Frame):  # tk.Frame을 상속하여 페이지 생성
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


# "테스트 방법", "1. 화면에 나오는 20개의 단어를 1분간 외운다.\n"
#         "2. 외운단어를 맞추기 전 몇개를 맞출 수 있을지 개수를 적는다.\n"
#         "3. 외운단어를 2분간 적는다.\n"
#         "4. 테스트 전에 몇 개를 맞출지 예상한 개수와 실제 외운 단어 개수를 비교한다.\n"
        

    def backTo(self):
        self.controller.swtich_frame("StartPage") #사용자정보입력 페이지로 넘어가기