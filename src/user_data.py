# user_data.py

class User:
    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = score

# 샘플 사용자 데이터
user = User(name="홍길동", gender="남성", age=25, score=3)
