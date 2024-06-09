import tkinter as tk
from PIL import Image, ImageTk
from ShowWord import ShowWord
from BaseImage import BaseImage


class UserInfo(BaseImage): ##BasePage(배경 이미지 설정 클래스) 상속
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 컨트롤러는 주 창(App 클래스)
        self.set_background("src/assets/user_info_background-2nd.png")


        # label = tk.Label(self, text="사용자 정보 입력")
        # label.pack(side ="top", fill="x", pady=10)

        # self.label_info=tk.Label(self,text="👤정보를 입력하세요.", font=("나눔고딕", 13))
        # self.label_info.place(x=740,y=100)

        # Label 및 Entry 위젯 추가
        # self.label_name = tk.Label(self, text="이름:", font=("나눔고딕", 20), bg="white")
        self.entry_name = tk.Entry(self)
        # self.label_name.place(x=650,y=200)
        self.entry_name.place(x=800,y=210)

        # self.label_gender = tk.Label(self, text="성별:",font=("나눔고딕", 20), bg="white")
        # self.label_gender.place(x=650,y=300)
    

        self.button_gender = tk.StringVar(self)  # 라디오 버튼 값을 저장할 변수
        self.button_gender.set("남성")  # 초기값 설정

        # 라디오 버튼 추가
        self.button_male = tk.Radiobutton(self, text="남성👦🏻", variable=self.button_gender, value="남성",font=("나눔고딕", 15), bg="white")
        self.button_female = tk.Radiobutton(self, text="여성👧🏻", variable=self.button_gender, value="여성",font=("나눔고딕", 15), bg="white")
        self.button_male.place(x=800,y=300)
        self.button_female.place(x=900,y=300)

        # self.label_age = tk.Label(self, text="나이:",font=("나눔고딕", 20), bg="white")
        self.entry_age = tk.Entry(self)
        # self.label_age.place(x=650,y=400)
        self.entry_age.place(x=580,y=510)

        # 다음 버튼 추가
        self.next_button = tk.Button(self, text="입력 완료", font=("나눔고딕", 15),command=self.show_user_info, bg="white")
        self.next_button.place(x=750,y=600)

        # 경고 메시지 라벨 추가 (입력 완료 버튼을 눌렀을 때 빈칸이 있으면 경고 메세지를 출력할수있게)
        self.warning_label = tk.Label(self, text="", font=("나눔고딕", 15), fg="red", bg="white")
        self.warning_label.place(x=820,y=500,anchor="center")


    def show_user_info(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        
        if not name or not age:
            self.warning_label.config(text="⚠️빈 칸이 있습니다.", bg="white") # 경고 메세지 config로 라벨 수정
        elif not age.isdigit(): # 입력한 문자열이 숫자로 입력되었는지 확인하기 위함
            self.warning_label.config(text="⚠️나이를 숫자로 입력해주세요.", bg="white")
        else:
            self.controller.swtich_frame("ShowWord")
