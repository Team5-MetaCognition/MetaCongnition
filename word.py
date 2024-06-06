from tkinter import *
import random

# 단어 리스트 50개 정의
words_list = [
    "사이다","로션","선풍기","공무원","휴대폰",
    "책상","박람회","여행","박스","지하철",
    "비행기","향수","국회의사당","병원","우유",
    "바디워시","부동산","키보드","백화점","물컵",
    "네덜란드","시계","지하철","친구","음악",
    "유튜브","영화","전화","시간","공항"
    # 더 추가하기
]

# 단어 리스트에서 20개의 단어를 무작위로 선택
random_words = random.sample(words_list, 20)

class App:
    def __init__(self):
        window = Tk()
        window.title("메타인지 테스트")
        window.geometry("1280x1024+100+100")

        window.mainloop()

App()