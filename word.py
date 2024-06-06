from tkinter import *
import random

# 단어 리스트 50개 정의
words_list = [
    "사이다", "로션", "선풍기", "공무원", "휴대폰",
    "책상", "박람회", "여행", "박스", "지하철",
    "비행기", "향수", "국회의사당", "병원", "우유",
    "바디워시", "부동산", "키보드", "백화점", "물컵",
    "네덜란드", "시계", "지하철", "친구", "음악",
    "유튜브", "영화", "전화", "시간", "공항"
    # 더 추가하기
]

# 단어 리스트에서 20개의 단어를 무작위로 선택
random_words = random.sample(words_list, 20)

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("메타인지 테스트")
        self.window.geometry("1280x1024+100+100")

        self.word_label = Label(self.window, text="", font=("Helvetica", 48))
        self.word_label.pack(expand=True)

        self.message_label = Label(self.window, text="", font=("Helvetica", 24))
        self.message_label.pack(expand=True)

        self.index = 0
        self.show_word()

        self.window.mainloop()

    def show_word(self):
        if self.index < len(random_words):
            self.word_label.config(text=random_words[self.index])
            self.message_label.config(text="2초 뒤에 넘어갑니다...")
            self.index += 1
            self.window.after(2000, self.show_word)  # 2초 후에 show_word 함수를 다시 호출
        else:
            self.word_label.config(text="끝!")
            self.message_label.config(text="")

App()
