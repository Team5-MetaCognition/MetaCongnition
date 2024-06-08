from tkinter import *
import random

class InputWord:
    def __init__(self):
        self.window = Tk()
        self.window.title("메타인지 테스트")
        self.window.attributes("-fullscreen", True)
        self.fullScreenState = False

        self.word_label = Label(self.window, text="20개의 단어를 하나씩 보여드리겠습니다.\n⏰한 단어당 2초\n\n화면에 출력되는 단어를 기억하자!", font=("나눔고딕", 48))
        self.word_label.pack(expand=True) # 단어 글자수가 달라서 상대적 위치를 지정해주는 pack 사용

        # self.button_start=Button(self.window,text="START",font=("나눔고딕", 30),command=self.show_word)
        # self.button_start.pack(expand=True)

        self.index = 0

        self.window.mainloop()

    
InputWord()
