def quiz():
    lives = 3
    while True:
      try:
        question = int(input('((5 + 4) * 2 )/ 3 = '))
        if question == 6:
            print('Your are Correct!')
            break
        else:
          lives -= 1
          print('You are Incorrect!', lives , 'tries remaining')
          if lives == 0:
            print('Nice Try!')
            break
      except ValueError:
          lives -= 1
          print('Invalid Input!', lives , 'tries remaining')
          if lives == 0:
            print('Nice Try!')
            break

quiz()