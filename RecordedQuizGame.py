print('Welcome to the Quiz Game!')

start = input('Do you want to play a game? ').lower()
if start != 'yes':
    quit()
print("Let's start! \n")

questions = {
    1 : 'What is the capital of France? ',
    2 : 'What is 4 + 6 - 3 * 2? ',
    3 : 'What is the tallest mountain in the world? ',
    4 : 'What is the chemical symbol for gold? ',
    5 : 'Who wrote "Romeo and Juliet"? '
}

answers = [
    'Paris',
    '4',
    'Everest',
    'Au',
    'William Shakespeare'
]

#function that takes user input, compares it with the list of answers and add the correct answers
def quiz():
    score = 0
    for question in questions:
        user_input = input(questions[question])
        if user_input.lower() == answers[question - 1].lower():
            print('You Are Correct!')
            score += 1
        else:
            print('Incorrect!')
    print(f'You got {score} questions correct!')

quiz()