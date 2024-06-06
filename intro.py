#intro

from tkinter import *

class App:
    def __init__(self):
        window = Tk()
        window.title("메타인지 테스트")
        window.geometry("1280x1024+100+100")

        #설명
        self.label = Label(window, text="이름:")
        self.label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        window.mainloop()

App()

