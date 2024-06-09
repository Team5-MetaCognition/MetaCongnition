# 사용자 정보
class User:
    inputWords = []
    estimatedNumber = 0
    random_words = []
    matching_word_counts=0

    def __init__(self, name: str="", gender: str="", age: int=0, score: int=0):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = score

    def setInfo(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def setEstimatedNumber(self, score):
        self.estimatedNumber = score

    def inputWord(self, word):
        self.inputWords.append(word)
        
    def set_random_words(self, words):
        self.random_words = words
    
    def set_matching_word_count(self, count):
        self.matching_word_counts = count
        
# 샘플 사용자 데이터
user = User(name="이예진", gender="여성", age=22, score=1)