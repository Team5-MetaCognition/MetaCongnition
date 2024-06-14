import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab, Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.font_manager as fm
import customtkinter as ctk
from BaseImage import BaseImage

class ReportScreen(BaseImage):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.set_background("src/assets/report-bg.png")
        self.user = self.controller.user
        
        # 모든 사용자 정보를 한 줄로 표시
        self.user_info_label = tk.Label(
            self, 
            text=f"이름: {self.user.name}, 성별: {self.user.gender}, 나이: {self.user.age}", 
            font=("나눔고딕", 14),
            bg="white"
        )
        self.user_info_label.place(x=120, y=100)

        # '결과 화면' 레이블 생성 및 배치
        self.label = tk.Label(self, text="당신의 메타인지 능력은 ", font=("나눔고딕", 20), bg="white")
        self.label.place(x=120, y=130)
        
        # 결과 내용을 표시하는 메소드 호출
        self.display_result()
        
        # 메타인지 향상 방법을 표시하는 메소드 호출
        self.display_improvement_tips()
        
        # '이미지로 저장' 버튼 생성 및 배치 (오른쪽 위에 고정)
        self.save_image_button = ctk.CTkButton(self, text="이미지로 저장", command=self.save_as_image, font=("나눔고딕", 10), width=100, height=40, fg_color="#fae375", hover_color="#b09307",text_color="#000000")
        self.save_image_button.place(x=1300, y=30)

         # '종료' 버튼 생성 및 배치
        self.back_button = ctk.CTkButton(self, text="종료", command=self.exit, font=("나눔고딕", 14, "bold"), width=150, height=50, fg_color="#fae375", hover_color="#b09307",text_color="#000000")
        self.back_button.place(x=670, y=740)

    def display_result(self):
        # 점수에 따라 결과 내용 표시
        self.user.calculate_difference_abs()
        if self.user.difference_abs  <= 2:
            result_onelevel_text = "상"
            result_twolevel_text = "높은 인식"
            result_threelevel_text = "이 수준의 개인은 자신의 사고 과정, 학습 전략 및 성과에 대한 높은 수준의 인식을 나타냅니다. 그들은 지속적으로 비판적 성찰에 참여하고, 명확하고 달성 가능한 목표를 설정하고, 해당 목표를 향한 진행 상황을 효과적으로 모니터링합니다. 그들은 작업에 대한 접근 방식에서 높은 수준의 유연성을 보여주고, 피드백과 변화하는 상황에 따라 전략을 쉽게 적용합니다. 학습과 성과 향상을 위해 다양한 자원과 지원 시스템을 적극적으로 모색하고 활용합니다. "
        elif 2 < self.user.difference_abs  <= 5:
            result_onelevel_text = "중"
            result_twolevel_text = "기본 인식"
            result_threelevel_text = "이 수준의 개인은 자신의 사고 과정을 어느 정도 인식하고 있으며 때때로 자신의 학습 경험을 반영할 수 있습니다. 일관되지는 않더라도 스스로 기본 목표를 설정하고 진행 상황을 모니터링하기 위해 어느 정도 노력할 수 있습니다. 그들은 작업에 대한 접근 방식에서 제한된 유연성을 보여줄 수 있으며 심각한 문제에 직면할 때 도움을 구할 수 있습니다. "
        else:
            result_onelevel_text = "하"
            result_twolevel_text = "낮은 인식"
            result_threelevel_text = "이 수준의 개인은 자신의 사고 과정, 학습 전략 또는 성과에 대해 거의 또는 전혀 인식하지 못합니다. 그들은 자신의 학습 경험을 반영하거나 과제에 대한 대안적 접근 방식을 거의 고려하지 않을 수 있습니다. 명확한 목표를 설정하고 진행 상황을 모니터링하거나 피드백을 기반으로 전략을 조정하는 데 어려움을 겪을 수 있습니다."

        # 결과 내용을 표시할 레이블 생성 및 배치
        self.result_label = tk.Label(self, text=result_onelevel_text, font=("나눔고딕", 30), bg="white")
        self.result_label.place(x=220, y=220)

        # 결과 내용 자세하게 표시
        self.detail_label = tk.Label(self, text=result_twolevel_text, font=("나눔고딕", 20), bg="white")
        self.detail_label.place(x=120, y=350)
        
        # result_threelevel_text를 온점 기준으로 분할하여 여러 라벨로 출력
        sentences = result_threelevel_text.split(". ")
        y_position = 400
        for sentence in sentences:
            sentence = sentence.strip()  # 문자열 양쪽 공백 제거
            if sentence:  # 빈 문자열이 아니면 라벨 생성
                # 마지막 문장에 이미 온점이 있다면 추가하지 않음
                if not sentence.endswith("."):
                    sentence += "."
                self.detail_label2 = tk.Label(self, text=sentence, font=("나눔고딕", 14), bg="white")
                self.detail_label2.place(x=120, y=y_position)
                y_position += 30  # 다음 라벨의 y 위치 조정

    def save_as_image(self):
        # 전체 화면을 캡처
        image = ImageGrab.grab()

        # 이미지 저장 경로 선택
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            image.save(file_path, "PNG")

    def display_improvement_tips(self):
        improvement_tips_title = "메타인지 향상 방법"
        improvement_tips = "자신의 사고 과정을 지속적으로 점검하고, 학습 목표 설정 후 주기적으로 성취도를 평가해야합니다"
        self.recommend_label = tk.Label(self, text="추천활동:", font=("나눔고딕", 14), bg="white")
        self.recommend_label.place(x=120, y=660)

        
         # 메타인지 향상 방법을 표시할 레이블 생성 및 배치
        improvement_tips_title_label = tk.Label(self, text=improvement_tips_title, font=("나눔고딕", 20), justify=tk.LEFT, bg="white")
        improvement_tips_title_label.place(x=120, y=570)
        improvement_tips_label = tk.Label(self, text=improvement_tips, font=("나눔고딕", 14), justify=tk.LEFT, bg="white")
        improvement_tips_label.place(x=120, y=620)
        
       # 여러 항목을 한 줄로 일정 간격을 두고 배치
        tips = ["명상(마인드셋)", "일기쓰기", "자기시험", "일정관리"]
        x_position = 120 + self.recommend_label.winfo_reqwidth() + 10  # "추천활동:" 레이블 너비에 10픽셀 간격 추가
        for tip in tips:
            tip_label = tk.Label(self, text=tip, font=("나눔고딕", 14), bg="white")
            tip_label.place(x=x_position, y=660)
            x_position += tip_label.winfo_reqwidth() + 20  # 현재 레이블의 너비에 20픽셀 간격 추가
            
    def exit(self):
        self.controller.exit()

    def draw_graph(self):
        # 한글 폰트 설정
        font_path = 'src/font/GangwonModuBold.ttf'  # 예시 경로, 시스템에 맞게 수정 필요
        font_prop = fm.FontProperties(fname=font_path)

        categories = ['입력 개수', '맞춘 개수', '예상 개수', '총 단어 개수']
        values = [len(self.controller.user.input_words), self.controller.user.matching_word_counts, self.controller.user.estimated_number, 20]  # 예시 값

        y = np.arange(len(categories))

        figure = plt.figure(figsize=(5, 3)) # 크기를 적절히 조정
        ax = figure.add_subplot(111)
        ax.barh(y, values, color='skyblue')
        ax.set_yticks(y)
        plt.xticks(range(0, 25, 5))
        ax.set_yticklabels(categories, fontproperties=font_prop)
        ax.set_title('메타인지 테스트 결과', fontproperties=font_prop)

        canvas_frame = tk.Frame(self, bg='lightblue', width=500, height=300)  # 배경색 설정
        canvas_frame.pack(side='top', anchor='ne', padx=(0,130), pady=(90, 20))

        canvas = FigureCanvasTkAgg(figure, master=canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=3, sticky='ne', padx=10, pady=10)

    def display_user_info(self):
        user = self.controller.user
        self.user_info_label.config(text=f"이름: {user.name}, 성별: {user.gender}, 나이: {user.age}")