from tkinter import *
import random

# 단어 리스트 100개 일상에서 접하는 단어?
words_list = [
    "비행기", "향수", "국회의사당", "병원", "우유",
    "피타고라스", "까르보나라", "와이파이", "바이러스", "코로나",
    "바디워시", "부동산", "키보드", "백화점", "고글",
    "사이다", "로션", "선풍기", "공무원", "휴대폰",
    "책상", "박람회", "여행", "박스", "지하철",
    "네덜란드", "시계", "지하철", "친구", "음악",
    "인스타그램", "영화", "전화", "시간", "공항",
    "논설", "알람", "애니메이션", "자물쇠", "과제",
    "네이버", "바닐라", "오토바이", "배달의민족", "관악산",
    "타이레놀", "삼성페이", "홈런", "거짓말", "예매",
    "신용카드", "한글", "토스", "소프트웨어", "탄산수",
    "스테이크", "사랑", "횡단보도", "떡볶이", "에어프라이기"
    # 더 추가하기
]

# 단어 리스트에서 20개의 단어를 무작위로 선택
random_words = random.sample(words_list, 20)

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("메타인지 테스트")
        self.window.geometry("1280x1024+100+100")

        self.word_label = Label(self.window, text="20개의 단어를 하나씩 보여드리겠습니다.\n⏰한 단어당 2초\n\n화면에 출력되는 단어를 기억하자!", font=("나눔고딕", 48))
        self.word_label.pack(expand=True) # 단어 글자수가 달라서 상대적 위치를 지정해주는 pack 사용

        self.button_start=Button(self.window,text="START",font=("나눔고딕", 30),command=self.show_word)
        self.button_start.pack(expand=True)

        self.index = 0

        self.window.mainloop()

    def show_word(self):
        self.button_start.pack_forget()  # 시작 버튼 숨기기
        if self.index < 20:
            self.word_label.config(text=random_words[self.index])
            self.index += 1
            self.window.after(100, self.show_word) #빠르게 TEST
            #self.window.after(2000, self.show_word)  # 2초 후에 show_word 함수를 다시 호출
        else:
            self.word_label.config(text="끝!")
            self.button_next = Button(self.window, text="NEXT", font=("나눔고딕", 30)) #다음페이지(예상개수입력)로 넘어가는 커맨드추가하면 됨.
            self.button_next.pack(expand=True)
App()
