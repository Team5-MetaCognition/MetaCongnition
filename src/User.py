# 사용자 정보
class User:
    input_words = []
    estimated_number = 0
    random_words = []
    matching_word_counts=0
    difference_abs = 0

    def __init__(self, name: str="", gender: str="", age: int=0, score: int=0):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = score

    def setInfo(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def set_estimated_number(self, score):
        self.estimated_number = score

    def inputWord(self, word):
        self.input_words.append(word)
        
    def set_random_words(self, words):
        self.random_words = words
    
    def set_matching_word_count(self, count):
        self.matching_word_counts = count
    
    def calculate_difference_abs(self): #유저가 예상한 개수와 실제 맞춘 개수의 차이를 절대값으로 저장
        self.difference_abs = abs(self.estimated_number - self.matching_word_counts)
