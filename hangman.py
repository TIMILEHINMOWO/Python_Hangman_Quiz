# Open the file and read the contents
with open('quiz_questions.txt') as f:
    content = f.read()

# Split the content into individual questions
questions = content.split('\n\n')

# Initialize the score
score = 0
wrong = 0

# Loop through the questions
for i, question in enumerate(questions, 1):
    # Split the question into the question prompt and the answer choices
    q, choices, answer = question.split('\n')

    # Print the question prompt
    print(f'Question {i}: {q}')

    # Print the answer choices
    for choice in choices.split('/'):
        print(choice)

    # Ask the user for their answer
    user_answer = input('Your answer: ')

    # Check if the user's answer is correct
    if user_answer.upper() == answer.split()[-1]:
        print('Correct! \n')
        score += 1
    else:
        print(f'Incorrect. The correct answer is {answer.split()[-1]} \n')
        wrong -= 1
      
    #Add a stick to form a stichman every time you get an answer wrong
    #Game ends after 7 wrong answers
    if wrong == -1:
      print("\t \t \t 0 \t \t \t")
    elif wrong == -2:
      print("\t \t \t 0 \t \t \t")
      print("\t \t \t/  \t \t")
    elif wrong == -3:
      print("\t \t \t 0 \t \t \t")
      print("\t \t \t/ \ \t \t \t")
    elif wrong == -4:
      print("\t \t \t 0 \t \t \t")
      print("\t \t \t/|\ \t \t \t")
    elif wrong == -5:
      print("\t \t \t 0 \t \t \t")
      print("\t \t \t/|\ \t \t \t")
      print("\t \t \t | \t \t \t")
    elif wrong == -6:
      print("\t \t \t 0 \t \t \t")
      print("\t \t \t/|\ \t \t \t")
      print("\t \t \t | \t \t \t")
      print("\t \t \t/  \t \t \t")
    elif wrong == -7:
      print("\t \t \t 0 \t \t \t")
      print("\t \t \t/|\ \t \t \t")
      print("\t \t \t | \t \t \t")
      print("\t \t \t/ \ \t \t \t \n")
      print("Game over!!!")
      break
      
# Print the final score
print(f'You scored {score} out of {len(questions)}')
