from tkinter import *
import numpy as np
#import csv

class App:
    def __init__(self):
        window = Tk()
        window.title("메타인지 테스트")
        window.geometry("1280x1024+100+100")
        
        # Label 및 Entry 위젯 추가
        self.label_name = Label(window, text="이름:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.entry_name = Entry(window)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_gender = Label(window, text="성별:")
        self.label_gender.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        self.gender_var = StringVar(window)  # 라디오 버튼 값을 저장할 변수
        self.gender_var.set("남성")  # 초기값 설정

        # 라디오 버튼 추가
        self.radio_male = Radiobutton(window, text="남성", variable=self.gender_var, value="남성")
        self.radio_male.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        self.radio_female = Radiobutton(window, text="여성", variable=self.gender_var, value="여성")
        self.radio_female.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        self.label_age = Label(window, text="나이:")
        self.label_age.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.entry_age = Entry(window)
        self.entry_age.grid(row=2, column=1, padx=10, pady=5)

        # 다음 버튼 추가
        #self.next_button = Button(window, text="다음", command=self.save_to_csv)
        #self.next_button.grid(row=3, columnspan=2, pady=10) #위치

        window.mainloop()

    # def save_to_csv(self):
    #     # 사용자가 입력한 정보 가져오기
    #     name = self.entry_name.get()
    #     gender = self.gender_var.get()
    #     age = self.entry_age.get()

        # 입력 값이 비어있으면 경고 메세지
        #if not name or not age:
            

        # CSV 파일로 저장
        # user_data = np.array([[name, gender, age]])
        # with open('user_info.csv', 'a', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(user_data)

        # 입력 필드 초기화
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)

App()