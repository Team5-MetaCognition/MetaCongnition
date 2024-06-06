import tkinter as tk
from tkinter import messagebox

class MetacognitionTestApp:
    def __init__(self, root):
 # 메인 윈도우 설정
        self.root = root
        self.root.title("메타인지 테스트")
 # "메타인지 테스트" 타이틀 라벨
        self.title_label = tk.Label(root, text="메타인지 테스트", font=("Helvetica", 20))
        self.title_label.pack(pady=20)
        self.title_label = tk.Label(root, text="메타인지는 자신의 인지 과정에 대한 인지,\n"
                                    "즉 자신의 사고나 학습 과정을 이해하고\n"
                                    "통제하는 능력을 의미합니다.", font=("Helvetica", 11))
# "테스트 시작" 버튼
        self.title_label.pack(pady=20)        
        self.start_button = tk.Button(root, text="테스트 시작", command=self.start_test)
        self.start_button.pack(pady=10)

# "테스트 방법" 버튼
        self.method_button = tk.Button(root, text="테스트 방법", command=self.show_method)
        self.method_button.pack(pady=10)

# "테스트 시작" 버튼 클릭 시 호출
    def start_test(self):
        messagebox.showinfo("테스트 시작", "")

# "테스트 방법" 버튼 클릭 시 호출
    def show_method(self):
        messagebox.showinfo("테스트 방법", "1. 화면에 나오는 20개의 단어를 1분간 외운다.\n"
        "2. 외운단어를 맞추기 전 몇개를 맞출 수 있을지 개수를 적는다.\n"
        "3. 외운단어를 2분간 적는다.\n"
        "4. 테스트 전에 몇 개를 맞출지 예상한 개수와 실제 외운 단어 개수를 비교한다.\n")

if __name__ == "__main__":
# 메인 윈도우 생성
    root = tk.Tk()
# 애플리케이션 인스턴스 생성
    app = MetacognitionTestApp(root)
# 메인 이벤트 루프 시작
    root.mainloop()