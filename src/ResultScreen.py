import tkinter as tk

class ResultScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.show_results()

    def show_results(self):
        # 기존 위젯 제거
        for widget in self.winfo_children():
            widget.destroy()
            
        result_frame = tk.Frame(self)
        result_frame.pack(expand=True)

        words_to_display = self.controller.user.random_words #랜덤으로 나온 20개 단어 호출
        user_input_words = self.controller.user.inputWords #사용자에게 입력 받은 단어 저장
        
        print("user_input_words:", user_input_words)
        count=0

        
        for i, word in enumerate(words_to_display):  # enumerate : 리스트를 인덱스와 함께 반환함 즉 i에는 인덱스 word에는 단어 저장됨
            if word in user_input_words:
                display_text = f"{word} O" #사용자가 맞춘 단어 옆에는 O 표시
                count= count + 1 # 맞춘 개수 저장
                word_color="green" # 맞춘 단어는 초록색
            else:
                display_text = f"{word} X" #사용하자 맞추지 못한 단어 옆에는 X 표시
                word_color="red" # 맞추지 못한 단어는 빨간색
            word_label = tk.Label(result_frame, text=display_text, font=("나눔고딕", 30, "bold"), fg=word_color)
            word_label.grid(row=i//5, column=i%5, padx=20, pady=20)

        self.show_report_button = tk.Button(self, text="자세한 결과보기", command=self.show_report,height=3, width=20,font=("나눔고딕", 14))
        self.show_report_button.pack(pady=10)    
        
    def show_report(self):
        self.controller.switch_frame("ReportScreen")
