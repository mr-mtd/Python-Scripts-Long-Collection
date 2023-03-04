from msilib.schema import Property

class TriviaSet:
    def __init__(self):
        self.answer = ''
        self.a = ''
        self.b = ''
        self.c = ''
        self.d = ''
        self.questions = ''

    def to_dict(self):
        return {
            'questions': self.questions,
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
            'answer': self.answer
        }

    def questions(self):
        return self.questions

    def a(self):
        return self.a

    def b(self):
        return self.b

    def c(self):
        return self.c

    def d(self):
        return self.d

    def answer(self):
        return self.answer
