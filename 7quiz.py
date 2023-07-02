class Question:
    
    def __init__(self,text,choises,answer):
        self.text = text
        self.choises = choises
        self.answer = answer
        
    def checkAnswer(self,answer):
        return self.answer == answer



class Quiz:

    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0
        self.totalQuestion = len(questions)
    def getQuestion(self):
        return self.questions[self.questionsIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionsIndex+1} of {self.totalQuestion}".center(50,"*"))
        print(f"Soru {self.questionsIndex + 1}: {question.text}")
        
        for q in question.choises:
            print("-"+q)
    
        answer = input("cevap: ")
        self.guess(answer)
    
    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score +=1
        
        while (self.totalQuestion != self.questionsIndex):
            try:
                self.questionsIndex += 1
                self.displayQuestion()
            except IndexError:
                
                print("Quiz Bitti".center(50,"*"))
                print(f"Score: {self.score}".center(50,"*"))

q1 = Question("En güzel sarki?",["numb", "outlaws", "graveyard"],"numb")
q2 = Question("En güzel renk?",["mavi", "sari", "turqo"],"turqo")
q1 = Question("En güzel mevsim?",["sonbahar","kis","yaz"],"sonbahar")
q2 = Question("En güzel renk?",["mavi", "sari", "turqo"],"turqo")

questions = [q1,q2]
quiz = Quiz(questions)


quiz.displayQuestion()