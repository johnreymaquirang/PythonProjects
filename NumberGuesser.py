import random

def main():
    try: 
        num_range = int(input('Pick a Number for Range: '))
    except ValueError:
        print('Please Input a Number!')
        quit()

    r = random.randint(1, num_range)
    attempts = 0

    while True:
        attempts += 1
        try:
            user_input = int(input(f'Guess a number from 1 to {num_range}: '))
            if user_input == r:
                print('Your Guess is Right!')
                break
            elif user_input <= 0 or user_input > num_range:
                print('Please Input Within Range Value!')
            else:
                if user_input > r:
                    print('You were above the Number!')
                else:
                    print('You were below the Number!')
        except ValueError:
            print('Invalid Input, Please Input a Number!') 
    return attempts

print(f'Total Attempts: {main()}')