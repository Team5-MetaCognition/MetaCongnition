import tkinter as tk
from PIL import Image, ImageTk
from ShowWord import ShowWord
from User import User
from BaseImage import BaseImage
import customtkinter as ctk

class UserInfo(BaseImage): ##BasePage(배경 이미지 설정 클래스) 상속
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 컨트롤러는 주 창(App 클래스)
        self.set_background("src/assets/user_info_background-3rd.png")

        self.entry_name = tk.Entry(self, width=15,font=("나눔고딕", 24))
        self.entry_name.place(x=720,y=260)    

        self.button_gender = tk.StringVar(self)  # 라디오 버튼 값을 저장할 변수
        self.button_gender.set("남성")  # 초기값 설정

        # 라디오 버튼 추가
        self.button_male = tk.Radiobutton(self, text="남성👦🏻", variable=self.button_gender, value="남성",font=("나눔고딕", 24), bg="white")
        self.button_female = tk.Radiobutton(self, text="여성👧🏻", variable=self.button_gender, value="여성",font=("나눔고딕", 24), bg="white")
        self.button_male.place(x=720,y=375)
        self.button_female.place(x=850,y=375)

        self.entry_age = tk.Entry(self, width=15,font=("나눔고딕", 24))
        self.entry_age.place(x=720,y=530)

        # 다음 버튼 추가
        self.next_button = ctk.CTkButton(self, text="입력 완료", font=("나눔고딕", 30, "bold"),command=self.validatioin_user_info, width=150, height=50, fg_color="#fae375", hover_color="#b09307",text_color="#000000")
        self.next_button.place(x=670,y=650)

        # 경고 메시지 라벨 추가 (입력 완료 버튼을 눌렀을 때 빈칸이 있으면 경고 메세지를 출력할수있게)
        self.warning_label = tk.Label(self, text="", font=("나눔고딕", 15), fg="red", bg="white")
        self.warning_label.place(x=820,y=600,anchor="center")


    def validatioin_user_info(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.button_gender.get()
        
        if not name or not age:
            self.warning_label.config(text="⚠️빈 칸이 있습니다.", bg="white") # 경고 메세지 config로 라벨 수정
        elif not age.isdigit(): # 입력한 문자열이 숫자로 입력되었는지 확인하기 위함
            self.warning_label.config(text="⚠️나이를 숫자로 입력해주세요.", bg="white")
        else:
            self.controller.user.setInfo(name, gender, age)
            self.controller.switch_frame("ShowWord")