# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz
class QuizBrain ():

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
    
    def still_has_questions(self):
        return len(self.question_list) > self.question_number           
        
    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        self.Answer = input(f"Q. {self.question_number}: {item.question} (True/False)?: ")
    
    def check_the_answer(self):
        item = self.question_list[self.question_number - 1]
        o_answer = item.answer
        m_answer = self.Answer
        return m_answer.lower() == o_answer.lower() 