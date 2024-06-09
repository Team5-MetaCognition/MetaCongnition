import tkinter as tk
from PIL import Image, ImageTk

class BaseImage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None  # 나중에 controller를 설정할 수 있도록 준비
        self.background_label = tk.Label(self)
        self.background_label.place(relwidth=1, relheight=1)  # 프레임 전체에 이미지 채우기

    def set_background(self, image_path):
            image = Image.open(image_path)
            image = image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
            photo = ImageTk.PhotoImage(image)
            
            self.background_label.configure(image=photo)
            self.background_label.image = photo  # PhotoImage가 가비지 컬렉션에 의해 제거되지 않도록 유지
