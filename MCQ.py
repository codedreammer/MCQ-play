# List of questions
questions = [
    "What is the capital of India?",
    "What is the full form of HTML?",
    "How is your life after choosing ENGINEERING!?",
    "What is Happiness as an Engineer?"
]

# List of options for each question
options = [
    ["a) Uttrakhand", "b) Kerla", "c) Delhi", "d) Bihar"],
    ["a) Hyp Markup Language", "b) Hypertext Markup Language", "c) Hypertext Mark Language", "d) Hypertext Markup Program"],
    ["a) Fucked up", "b) All of these", "c) Dont't you dare to ask again", "d) don't know"],
    ["a) Project completed", "b) Date with Crush", "c) Promotion", "d) Work from Home"]
]

# List of correct answers
correct_answers = ["c", "b", "b", "a"]


# Function to run the quiz
def run_quiz(questions, options, correct_answers):
    score = 0
    for i in range(len(questions)):
        print(f"Q{i+1}: {questions[i]}")
        for option in options[i]:
            print(option)
        answer = input("Your answer: ").lower()
        if answer == correct_answers[i]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {correct_answers[i]}\n")
    print(f"Your final score is {score}/{len(questions)}/'Well Done!'")
    if score == 4:
        print("Well Done!")

    if score == 0:
        print("please try AGAIN!")

# Run the quiz
run_quiz(questions, options, correct_answers)