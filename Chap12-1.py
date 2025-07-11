#Chad Collard
#Chapter 12 lab 1
#7/11/2025
# The Capital Game

print("State Capital's Game\n")

states = {'Ohio': 'Columbus',
          'Virginia': 'Richmond',
          'Oregon': 'Salem',
          'Washington': 'Olympia',
          'Kentucky': 'Frankfort'}

correct_answers = 0
incorrect_answers = 0

for state, capital in states.items():
    print(f'What is the capital of {state}?')
    user_answer = input('Type your answer: ')
    if user_answer.lower() == capital.lower():
        print('\nGood Job!\n')
        correct_answers += 1
    else:
        print(f'\nSorry the answer is {capital}.\n')
        incorrect_answers += 1

print(f'You answered {correct_answers} correctly, and {incorrect_answers} incorrectly.')



