
from question_model import question
from data import question_data
from quiz_brain import quiz_brain
question_bank = []

for i in question_data:
    new_q = question(i["text"], i["answer"])
    question_bank.append(new_q)

quiz = quiz_brain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_num}")