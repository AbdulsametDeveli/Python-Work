# 1. QUESTION CLASS: Soruların yapısını belirleyen sınıf
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

# 2. QUIZ CLASS: Quiz'in akışını ve puanlamayı yöneten sınıf
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        # Mevcut index'teki soru objesini getirir
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        # Şıkları ekrana yazdır
        for q in question.choices:
            print('- ' + q)

        answer = input('cevap: ')
        self.guess(answer)
        # Cevap verildikten sonra sıradaki soru yüklenir
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        
        # Cevap doğruysa puanı artır
        if question.checkAnswer(answer):
            self.score += 1
        
        # Her tahminde soru sırasını (index) artır
        self.questionIndex += 1

    def loadQuestion(self):
        # Eğer sorular bittiyse skoru göster, bitmediyse sıradaki soruyu göster
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f' Question {questionNumber} of {totalQuestion} '.center(100,'*'))

# UYGULAMA KISMI

# Soruları oluşturuyoruz
q1 = Question('En iyi programlama dili hangisidir?', ['C#', 'python', 'javascript', 'java'], 'python')
q2 = Question('En popüler programlama dili hangisidir?', ['python', 'java', 'C#', 'javascript'], 'python')
q3 = Question('En çok kazandıran programlama dili hangisidir?', ['C#', 'javascript', 'java', 'python'], 'python')

# Soruları bir listeye koyuyoruz
questions = [q1, q2, q3]

# Quiz'i başlatıyoruz
quiz = Quiz(questions)
quiz.loadQuestion()