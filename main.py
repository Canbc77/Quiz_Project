from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data["results"]:  # Fixed the typo here
    question_text = question["question"]
    question_answer = question["correct_answer"]  # Fixed the typo here
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    user_answer = quiz.next_question()

print(f"\n|||||||||||||||||||\n\nYour final score was: {quiz.score}/{quiz.question_number}")
