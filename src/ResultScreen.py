from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from user_data import user

class ResultScreen:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title("메타인지 테스트")
        self.window.attributes("-fullscreen", True)
        self.fullScreenState = False
        # 창 고정
        self.window.resizable(False, False)

        # 모든 사용자 정보를 한 줄로 표시
        self.user_info_label = Label(
            self.window, 
            text=f"이름: {self.user.name}, 성별: {self.user.gender}, 나이: {self.user.age}", 
            font=("Arial", 14)
        )
        self.user_info_label.place(x=120, y=100)

        # '결과 화면' 레이블 생성 및 배치
        self.label = Label(self.window, text="당신의 메타인지 능력은 ", font=("Arial", 20))
        self.label.place(x=120, y=130)
        
         # 결과 내용을 표시하는 메소드 호출
        self.display_result()
        
        # 메타인지 향상 방법을 표시하는 메소드 호출
        self.display_improvement_tips()
        
        # 'PDF로 저장' 버튼 생성 및 배치 (오른쪽 위에 고정)
        self.save_pdf_button = Button(self.window, text="PDF로 저장", command=self.save_as_pdf)
        self.save_pdf_button.place(x=1185, y=0)

         # '종료' 버튼 생성 및 배치
        self.back_button = Button(self.window, text="종료", command=self.exit)
        self.back_button.place(x=640, y=1000)
        
        # Tk 이벤트 루프 시작
        self.window.mainloop()  

    def display_result(self):
        # 점수에 따라 결과 내용 표시
        if self.user.score <= 2:
            result_onelevel_text = "상"
            result_twolevel_text = "높은 인식"
            result_threelevel_text = "이 수준의 개인은 자신의 사고 과정, 학습 전략 및 성과에 대한 높은 수준의 인식을 나타냅니다. 그들은 지속적으로 비판적 성찰에 참여하고, 명확하고 달성 가능한 목표를 설정하고, 해당 목표를 향한 진행 상황을 효과적으로 모니터링합니다. 그들은 작업에 대한 접근 방식에서 높은 수준의 유연성을 보여주고, 피드백과 변화하는 상황에 따라 전략을 쉽게 적용합니다. 학습과 성과 향상을 위해 다양한 자원과 지원 시스템을 적극적으로 모색하고 활용합니다. "
        elif 2 < self.user.score <= 5:
            result_onelevel_text = "중"
            result_twolevel_text = "기본 인식"
            result_threelevel_text = "이 수준의 개인은 자신의 사고 과정을 어느 정도 인식하고 있으며 때때로 자신의 학습 경험을 반영할 수 있습니다. 일관되지는 않더라도 스스로 기본 목표를 설정하고 진행 상황을 모니터링하기 위해 어느 정도 노력할 수 있습니다. 그들은 작업에 대한 접근 방식에서 제한된 유연성을 보여줄 수 있으며 심각한 문제에 직면할 때 도움을 구할 수 있습니다. "
        else:
            result_onelevel_text = "하"
            result_twolevel_text = "낮은 인식"
            result_threelevel_text = "이 수준의 개인은 자신의 사고 과정, 학습 전략 또는 성과에 대해 거의 또는 전혀 인식하지 못합니다. 그들은 자신의 학습 경험을 반영하거나 과제에 대한 대안적 접근 방식을 거의 고려하지 않을 수 있습니다. 명확한 목표를 설정하고 진행 상황을 모니터링하거나 피드백을 기반으로 전략을 조정하는 데 어려움을 겪을 수 있습니다."

        # 결과 내용을 표시할 레이블 생성 및 배치
        self.result_label = Label(self.window, text=result_onelevel_text, font=("Arial", 30))
        self.result_label.place(x=220, y=220)

        # 결과 내용 자세하게 표시
        self.detail_label = Label(self.window, text=result_twolevel_text, font=("Arial", 20))
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
                self.detail_label2 = Label(self.window, text=sentence, font=("Arial", 14))
                self.detail_label2.place(x=120, y=y_position)
                y_position += 30  # 다음 라벨의 y 위치 조정

    def save_as_pdf(self):
        # 현재 화면의 스크린샷 찍기
        x = self.window.winfo_rootx()
        y = self.window.winfo_rooty()
        width = x + self.window.winfo_width()
        height = y + self.window.winfo_height()
        image = ImageGrab.grab((x, y, width, height))

        # PDF 저장 경로 선택
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            # 스크린샷을 PNG로 임시 저장
            temp_image_path = "temp_screenshot.png"
            image.save(temp_image_path)

            # PDF 생성
            c = canvas.Canvas(file_path, pagesize=letter)
            width, height = letter

            # 스크린샷을 PDF에 추가
            c.drawImage(temp_image_path, 0, 0, width=width, height=height)

            # PDF 저장
            c.save()
    
    def display_improvement_tips(self):
        improvement_tips_title = "메타인지 향상 방법"
        improvement_tips = ("1. 학습 목표를 명확하게 설정하세요.\n"
                            "2. 학습 과정 중 스스로에게 질문을 던지세요.\n"
                            "3. 학습 후 자신이 배운 내용을 요약해보세요.\n"
                            "4. 피드백을 적극적으로 받아들이고 반영하세요.\n"
                            "5. 다양한 학습 전략을 시도하고 조정하세요.")
        
         # 메타인지 향상 방법을 표시할 레이블 생성 및 배치
        improvement_tips_title_label = Label(self.window, text=improvement_tips_title, font=("Arial", 20), justify=LEFT)
        improvement_tips_title_label.place(x=120, y=550)
        improvement_tips_label = Label(self.window, text=improvement_tips, font=("Arial", 14), justify=LEFT)
        improvement_tips_label.place(x=120, y=620)
        

    def exit(self):
        self.window.destroy()

# 이 파일이 직접 실행될 때, User와 ResultScreen 클래스 인스턴스화
if __name__ == "__main__":
    ResultScreen(user)