import tkinter as tk
from tkinter import messagebox

class MetacognitionTestApp:
    def __init__(self, root):
 # 메인 윈도우 설정
        self.root = root
        self.root.title("메타인지 테스트")
        self.root.geometry("1280x1024+100+100")
 # "메타인지 테스트" 타이틀 라벨
        self.title_label = tk.Label(root, text="메타인지 테스트", font=("Helvetica", 48))
        self.title_label.pack(pady=40)
        self.title_label = tk.Label(root, text="메타인지는 자신의 인지 과정에 대한 인지,\n"
                                    "즉 자신의 사고나 학습 과정을 이해하고\n"
                                    "통제하는 능력을 의미합니다.", font=("Helvetica", 24))    
# "테스트 시작" 버튼
        self.title_label.pack(pady=20)        
        self.start_button = tk.Button(root, text="테스트 시작", font=("Helvetica", 24),command=self.start_test)
        self.start_button.place(x=300, y=500)

# "테스트 방법" 버튼
        self.method_button = tk.Button(root, text="테스트 방법", font=("Helvetica", 24),command=self.show_method)
        self.method_button.place(x=700, y=500)

# "테스트 시작" 버튼 클릭 시 호출
    def start_test(self):
        messagebox.showinfo("테스트 시작", "") #사용자정보입력 페이지로 넘어가기

# "테스트 방법" 버튼 클릭 시 호출 (테스트방법 페이지로 넘어가기)
    def show_method(self):
        messagebox.showinfo("테스트 방법", "1. 화면에 나오는 20개의 단어를 1분간 외운다.\n"
        "2. 외운단어를 맞추기 전 몇개를 맞출 수 있을지 개수를 적는다.\n"
        "3. 외운단어를 2분간 적는다.\n"
        "4. 테스트 전에 몇 개를 맞출지 예상한 개수와 실제 외운 단어 개수를 비교한다.\n")

# 블록은 현재 스크립트가 직접 실행될 때만 코드가 실행됩니다.
if __name__ == "__main__":
# 메인 윈도우 생성(tk.Tk()를 사용하여 메인 윈도우를 생성합니다.)
    root = tk.Tk()
# 애플리케이션 인스턴스 생성(MetacognitionTestApp 클래스의 인스턴스를 생성하여 GUI 애플리케이션을 시작합니다.)
    app = MetacognitionTestApp(root)
# 메인 이벤트 루프 시작(root.mainloop()를 호출하여 메인 이벤트 루프를 시작하고, 프로그램이 종료될 때까지 윈도우가 열려 있도록 합니다.)
    root.mainloop()