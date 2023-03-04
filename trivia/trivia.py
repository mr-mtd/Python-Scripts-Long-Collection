import random

# Define the questions and answers
questions = {
    "What is the capital of France?": {"options": ["1. Paris", "2. Rome", "3. London", "4. Madrid"], "answer": 1},
    "What is the largest planet in the solar system?": {
        "options": ["1. Jupiter", "2. Saturn", "3. Neptune", "4. Earth"], "answer": 1},
    "What is the smallest country in the world?": {
        "options": ["1. Monaco", "2. San Marino", "3. Vatican City", "4. Liechtenstein"], "answer": 3},
    "What is the highest mountain in the world?": {
        "options": ["1. Mount Everest", "2. K2", "3. Mount Kilimanjaro", "4. Mount McKinley"], "answer": 1},
    "What is the largest ocean in the world?": {
        "options": ["1. Pacific Ocean", "2. Atlantic Ocean", "3. Indian Ocean", "4. Southern Ocean"], "answer": 1}
}

# Define the number of questions per round
num_questions = 20

# Initialize the score
score = 0

# Shuffle the questions
question_list = list(questions.keys())
random.shuffle(question_list)

# Iterate through the questions
for i in range(num_questions):
    # Print the question and options
    question = question_list[i]
    print(question)
    for option in questions[question]["options"]:
        print(option)

    # Get the user's answer
    answer = input("Enter your answer (1-4): ")
    while answer not in ["1", "2", "3", "4"]:
        answer = input("Invalid input. Enter your answer (1-4): ")
    answer = int(answer)

    # Check the answer and update the score
    if answer == questions[question]["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# Print the final score
print("Game over. Your score is", score, "out of", num_questions)
