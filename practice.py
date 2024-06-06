import tkinter as tk
from tkinter import messagebox

class MetacognitionTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("메타인지 테스트")

        # "메타인지 테스트" 타이틀 라벨
        self.title_label = tk.Label(root, text="메타인지 테스트", font=("Helvetica", 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # 예상 개수 입력 라벨
        self.input_label = tk.Label(root, text="예상 개수를 입력하세요:")
        self.input_label.grid(row=1, column=0, padx=20)

        # 예상 개수 입력 칸
        self.entry = tk.Entry(root)
        self.entry.grid(row=1, column=1, padx=20)

        # 확인 버튼
        self.confirm_button = tk.Button(root, text="확인", command=self.confirm_input)
        self.confirm_button.grid(row=2, column=0, columnspan=2, pady=10)

    def confirm_input(self):
        try:
            # 예상 개수를 가져와 정수로 변환
            estimated_number = int(self.entry.get())
            # 메시지 박스를 통해 확인
            messagebox.showinfo("") #외운단어페이지로 넘어가게
        except ValueError:
            # 숫자가 아닌 값이 입력된 경우 오류 메시지 표시
            messagebox.showerror("오류", "유효한 숫자를 입력하세요.")

if __name__ == "__main__":
    # 메인 윈도우 생성
    root = tk.Tk()
    # 애플리케이션 인스턴스 생성
    app = MetacognitionTestApp(root)
    # 메인 이벤트 루프 시작
    root.mainloop()