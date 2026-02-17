from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for row in question_data:
    new_q = Question(row["question"], row["correct_answer"])
    question_bank += [new_q]

quiz = QuizBrain(question_bank)
count = 0
while quiz.still_has_questions():
    quiz.next_question()
    if quiz.check_the_answer() == True:
        count += 1
        print("You got the answer right!")
        print(f"current score {count}/{quiz.question_number}.")
    else:
        print("the answer is wrong!")
        print(f"current score {count}/{quiz.question_number}.")

    print("\n")

print(
    f"You've completed the quiz \n Your final score was: {count}/{quiz.question_number}."
)
