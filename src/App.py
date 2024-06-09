import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from UserInfo import UserInfo
from StartPage import StartPage
from HowToPage import HowToPage
from ShowWord import ShowWord
from EstimatedNumber import EstimatedNumber
from ReportScreen import ReportScreen
from ResultScreen import ResultScreen
from EnterWord import EnterWord
from User import User

# tk.Tk를 상속받아 창을 생성하고 관리
class MetacognitionTestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("메타인지 테스트")
        self.attributes("-fullscreen", True)
        self.fullScreenState = False

        self.user = User()

        # 모든 Frame을 저장할 딕셔너리
        self.frames = {}

        container = tk.Frame(self)  # 주 창 안에 컨테이너 Frame을 생성
        container.pack(fill="both", expand=True)  # 컨테이너를 화면에 맞게 확장

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for Frame in (StartPage, HowToPage, UserInfo, ShowWord, EstimatedNumber, EnterWord, ResultScreen ,ReportScreen):  # 여러 페이지(Frame)를 초기화
            page_name = Frame.__name__
            frame = Frame(parent=container, controller=self)  # 각 Frame에 부모와 컨트롤러 전달
            self.frames[page_name] = frame  # 딕셔너리에 Frame 저장
            frame.grid(row=0, column=0, sticky="nsew")  # 모든 Frame을 같은 위치에 배치

        self.switch_frame("StartPage")  # 시작 페이지를 표시
    
    def switch_frame(self, page_name):
        frame = self.frames[page_name]  # 전달된 페이지 이름에 해당하는 Frame을 가져옴
        if hasattr(frame, 'show_results'):
            frame.show_results() # 프레임 전환 시 show_results 호출
        frame.tkraise()  # 해당 Frame을 화면에 표시

        if page_name == "EnterWord":
            frame.start_timer()
        elif page_name == "ReportScreen":
            frame.set_user_info()
            frame.draw_graph()

# 블록은 현재 스크립트가 직접 실행될 때만 코드가 실행됩니다.
if __name__ == "__main__":
    # 애플리케이션 인스턴스 생성(MetacognitionTestApp 클래스의 인스턴스를 생성하여 GUI 애플리케이션을 시작합니다.)
    app = MetacognitionTestApp()

    # 메인 이벤트 루프 시작(root.mainloop()를 호출하여 메인 이벤트 루프를 시작하고, 프로그램이 종료될 때까지 윈도우가 열려 있도록 합니다.)
    app.mainloop()